# Tile options tab

Appears when **Structure type** is set to **Tile** on the [Structure options](structure-options.md) tab.

Configures the Q-value and scaling settings for tile-based energy representations.

---

## Tile settings

| Field | Description |
|---|---|
| Q values same | **Yes** / **No** — use a single Q value for all tile types |
| Scalings same | **Yes** / **No** — use a single energy scaling for all tile types |
| Baseline scaling | Global scaling factor applied before any per-tile scalings |

## Energy scalings

Entries are generated dynamically based on the tile types found in the loaded structure file.

| Field | Description |
|---|---|
| Q variable (per tile) | Q value for this tile type (shown when **Q values same** is No) |
| Tile variable (per tile) | Energy scaling factor for this tile type (shown when **Scalings same** is No) |
