#!/usr/bin/env python3
"""Generate Notaspy Blur variants from Nightfox's "Terafox - blurred".

Only the background-layer alpha channels change between variants; every other
color is copied verbatim from Terafox - blurred. Alpha levels mirror the
Espresso variants of jenslys/zed-catppuccin-blur.
"""
import copy, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "scripts" / "nightfox-source.json"
OUT = ROOT / "themes" / "notaspy-blur.json"
BASE = "Terafox - blurred"

# key -> alpha per level (same values as Catppuccin Espresso Blur)
LEVELS = {
    "Light": {"main": "99", "surface": "8c", "active": "90", "thumb": "80"},
    "":      {"main": "d7", "surface": "d0", "active": "b0", "thumb": "a0"},
    "Heavy": {"main": "e0", "surface": "db", "active": "d0", "thumb": "c0"},
}
KEYS = {
    "background": "main",
    "status_bar.background": "main",
    "title_bar.background": "main",
    "surface.background": "surface",
    "drop_target.background": "active",
    "tab.active_background": "active",
    "scrollbar.thumb.background": "thumb",
}

def main():
    src = json.loads(SOURCE.read_text())
    base = next(t for t in src["themes"] if t["name"] == BASE)
    themes = []
    for level, alphas in LEVELS.items():
        t = copy.deepcopy(base)
        t["name"] = "Notaspy Blur" + (f" [{level}]" if level else "")
        for key, slot in KEYS.items():
            t["style"][key] = t["style"][key][:7] + alphas[slot]
        themes.append(t)
    OUT.write_text(json.dumps({
        "$schema": src["$schema"],
        "name": "Notaspy Blur",
        "author": "chiangs",
        "themes": themes,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUT} ({len(themes)} themes)")

if __name__ == "__main__":
    main()
