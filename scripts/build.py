#!/usr/bin/env python3
"""Generate the Notaspy theme families.

Notaspy Blur   <- Nightfox "Terafox - blurred", plus Noctis-style italics.
Notaspy Darker <- Notaspy Blur with darker background colors (same hue).
Notaspy Noctis <- Noctis "Noctis Obscuro", made translucent.

Between blur levels only background-layer alpha channels change. Levels mirror
the Espresso variants of jenslys/zed-catppuccin-blur.
"""
import colorsys, copy, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
THEMES = ROOT / "themes"

LEVELS = {
    "Light": {"main": "99", "surface": "8c", "active": "90", "thumb": "80"},
    "":      {"main": "d7", "surface": "d0", "active": "b0", "thumb": "a0"},
    "Heavy": {"main": "e0", "surface": "db", "active": "d0", "thumb": "c0"},
}
# Background layers that carry the blur, and which alpha slot they get.
LEVEL_KEYS = {
    "background": "main",
    "status_bar.background": "main",
    "title_bar.background": "main",
    "surface.background": "surface",
    "drop_target.background": "active",
    "tab.active_background": "active",
    "scrollbar.thumb.background": "thumb",
}
# Layers drawn on top of the window background; fully transparent so the blur
# shows through (same set Terafox - blurred clears).
CLEAR_KEYS = [
    "editor.background",
    "editor.gutter.background",
    "panel.background",
    "terminal.background",
    "tab_bar.background",
    "tab.inactive_background",
    "toolbar.background",
]
# Noctis italicizes these scopes (and, via Zed's prefix fallback, every
# sub-scope under them, e.g. keyword.import, type.builtin).
ITALIC_PREFIXES = ("keyword", "type", "comment", "link_text")


# Notaspy Darker: Terafox's two background colors (bg1, bg0) with HSL
# lightness scaled by this factor. Hue, saturation and alpha are unchanged.
DARKEN = 0.65
TERAFOX_BGS = ("#152528", "#0f1c1e")


def darken_hex(rgb, factor):
    r, g, b = (int(rgb[i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb(h, l * factor, s)
    return "#" + "".join(f"{round(c * 255):02x}" for c in (r, g, b))


def darken_backgrounds(style):
    for key, value in style.items():
        if ("background" in key and isinstance(value, str)
                and value[:7].lower() in TERAFOX_BGS):
            style[key] = darken_hex(value[:7].lower(), DARKEN) + value[7:]


def italicize(syntax):
    for name, style in syntax.items():
        if name.split(".")[0] in ITALIC_PREFIXES:
            style["font_style"] = "italic"


def blur_variants(base, family, clear=False, extra=None):
    themes = []
    for level, alphas in LEVELS.items():
        t = copy.deepcopy(base)
        t["name"] = family + (f" [{level}]" if level else "")
        style = t["style"]
        style["background.appearance"] = "blurred"
        for key, slot in LEVEL_KEYS.items():
            style[key] = style[key][:7] + alphas[slot]
        if clear:
            for key in CLEAR_KEYS:
                style[key] = style[key][:7] + "00"
        if extra:
            extra(style)
        themes.append(t)
    return themes


def write(path, schema, family, themes):
    path.write_text(json.dumps({
        "$schema": schema,
        "name": family,
        "author": "chiangs",
        "themes": themes,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {path.relative_to(ROOT)} ({len(themes)} themes)")


def main():
    nf = json.loads((SCRIPTS / "nightfox-source.json").read_text())
    terafox = next(t for t in nf["themes"] if t["name"] == "Terafox - blurred")
    write(THEMES / "notaspy-blur.json", nf["$schema"], "Notaspy Blur",
          blur_variants(terafox, "Notaspy Blur",
                        extra=lambda s: italicize(s["syntax"])))

    def darker(style):
        italicize(style["syntax"])
        darken_backgrounds(style)

    write(THEMES / "notaspy-darker.json", nf["$schema"], "Notaspy Darker",
          blur_variants(terafox, "Notaspy Darker", extra=darker))

    nx = json.loads((SCRIPTS / "noctis-obscuro-source.json").read_text())
    obscuro = next(t for t in nx["themes"] if t["name"] == "Noctis Obscuro")
    write(THEMES / "notaspy-noctis.json", nx["$schema"], "Notaspy Noctis",
          blur_variants(obscuro, "Notaspy Noctis", clear=True))


if __name__ == "__main__":
    main()
