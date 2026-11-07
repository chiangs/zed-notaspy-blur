# Notaspy Blur for Zed

Terafox from [cange/nightfox.zed](https://github.com/cange/nightfox.zed) (`Terafox - blurred`), with the background blur split into three intensities, modeled on the Espresso variants of [jenslys/zed-catppuccin-blur](https://github.com/jenslys/zed-catppuccin-blur).

| Theme | Main bg alpha | Surface | Active tab / drop target | Scrollbar thumb |
|---|---|---|---|---|
| `Notaspy Blur [Light]` | `99` (60%) | `8c` | `90` | `80` |
| `Notaspy Blur` | `d7` (84%) | `d0` | `b0` | `a0` |
| `Notaspy Blur [Heavy]` | `e0` (88%) | `db` | `d0` | `c0` |

All other colors are identical to Terafox - blurred.

## Install

1. Clone this repo.
2. In Zed: Extensions → **Install Dev Extension** → select the folder.
3. Pick a theme with `theme selector: toggle`.

Blur depends on Zed's window transparency support on your OS.

## Rebuild

```bash
python3 scripts/build.py
```

Edit `LEVELS` in `scripts/build.py` to tune alphas. `scripts/nightfox-source.json` is a copy of upstream `themes/nvim-nightfox.json` (commit 4b15a61); replace it to pull upstream changes.

## License

MIT. Based on Nightfox for Zed © 2024 Christian Angermann.
