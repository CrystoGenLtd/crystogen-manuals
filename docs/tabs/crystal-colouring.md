# Crystal colouring tab

Configures the layer-colouring scheme applied to the output crystal visualisation.

---

## Layer colouring

| Field | Description |
|---|---|
| Tiles represented | **Yes** / **No** — colour by tile type |
| Mode | **Find** — auto-detect layer planes; **Colour** — apply colours to defined planes |
| Zebra path | Path to the colouring definition file (`.zebra`) |
| Max HKL | Maximum Miller index to consider when searching for layer planes |
| Crystal size | **Yes** / **No** — scale colouring by crystal size |

## Edit colouring file

Use these controls to create or modify a `.zebra` colouring file without leaving the GUI.

| Control | Description |
|---|---|
| Zebra edit path | Path to the file being edited — load with the **read layer file** button |
| Save changes | Writes the current edits back to the zebra edit path |
| Zebra all path | Path used by **add missing plane** — appends any uncoloured planes to the file |
