# Notaspy Blur for Zed

Two theme families, each in three blur intensities modeled on the Espresso variants of [jenslys/zed-catppuccin-blur](https://github.com/jenslys/zed-catppuccin-blur).

| Family | Based on |
|---|---|
| `Notaspy Blur` | `Terafox - blurred` from [cange/nightfox.zed](https://github.com/cange/nightfox.zed), with Noctis-style italics |
| `Notaspy Noctis` | `Noctis Obscuro` from [sidwachche/noctis-port](https://github.com/sidwachche/noctis-port), made translucent |

Each family has `[Light]`, default and `[Heavy]` variants:

| Variant | Main bg alpha | Surface | Active tab / drop target | Scrollbar thumb |
|---|---|---|---|---|
| `[Light]` | `99` (60%) | `8c` | `90` | `80` |
| default | `d7` (84%) | `d0` | `b0` | `a0` |
| `[Heavy]` | `e0` (88%) | `db` | `d0` | `c0` |

Syntax colors are untouched in both families.

- **Notaspy Blur** adds italics to keywords, types and comments (including all their sub-scopes), as Noctis does. Terafox's own italics (attributes, emphasis, link URIs) are kept.
- **Notaspy Noctis** keeps Obscuro's colors and italics. The editor, gutter, panels, terminal, tab bar and toolbar backgrounds are made fully transparent so the blur shows through; popovers stay opaque.

## Install

1. Clone this repo.
2. In Zed: Extensions → **Install Dev Extension** → select the folder.
3. Pick a theme with `theme selector: toggle`.

Blur depends on Zed's window transparency support on your OS. Italics need a font with a real italic face.

## Rebuild

```bash
python3 scripts/build.py
```

Tune alphas in `LEVELS` and italic scopes in `ITALIC_PREFIXES` in `scripts/build.py`. Upstream sources are vendored in `scripts/`:

- `nightfox-source.json`: `themes/nvim-nightfox.json` from cange/nightfox.zed (commit 4b15a61)
- `noctis-obscuro-source.json`: `themes/obscuro.json` from sidwachche/noctis-port (commit f3ad43e)

## License

MIT. Based on Nightfox for Zed © 2024 Christian Angermann, and on Noctis by Liviu Schera via the noctis-port Zed port by Siddha Wachche.
