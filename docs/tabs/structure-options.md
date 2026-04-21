# Structure options tab

This is the first of the core CrystoGen tabs. It defines the input files and the simulation mode, which determines which additional [parameter tabs](index.md) appear.

---

## Structure section

| Field | Description |
|---|---|
| Structure type | **Tile** or **Net** — determines which energy representation is used and which of the [Tile options](tile-options.md) or [Net options](net-options.md) tabs appears |
| Structure file | Path to the `_cg.txt` crystal structure file — auto-populated after running OCC, or set manually with the file browser |

## NET selection

| Option | Description |
|---|---|
| Single | Use a single `_net.txt` interaction-energy file |
| Multiple | Use a folder of net files for multi-solvent runs |

| Field | Description |
|---|---|
| NET file (single) | Path to a single `_net.txt` file |
| NET folder (multiple) | Path to a folder containing multiple `_net.txt` files |

## Optional features

| Field | Description |
|---|---|
| Screw | **Yes** / **No** — enable screw dislocations; shows the [Screw dislocations](screw-dislocations.md) tab when set to Yes |
| Simulation mode | Selects the growth algorithm — see table below |
| Ordered penalty | Penalty value used in **ordered** mode (appears only when that mode is selected) |

### Simulation modes

| Mode | Description |
|---|---|
| `normal` | Standard crystal growth simulation |
| `growth_modifier` | Introduces poison/modifier sites — enables the [Growth modifier](growth-modifier.md) tab |
| `ordered` | Growth with an ordering penalty |
| `screw_stress` | Stress field around a screw dislocation — enables the [Screw stress](screw-stress.md) tab |
| `diffusion` | Diffusion-limited growth — enables the [Diffusion](diffusion.md) tab |
| `nucleation` | Nucleation routine — enables the [Nucleation](nucleation.md) tab |
| `seed_engineering` | Custom seed shape — enables the [Seed engineering](seed-engineering.md) tab |
| `surface` | Surface/substrate growth — enables the [Surface](surface.md) tab |
| `solid_solution` | Solid-solution growth |

## Checkpoint

| Field | Description |
|---|---|
| Use checkpoint | **Yes** / **No** — resume from a saved checkpoint |
| Checkpoint file | Path to the checkpoint file (shown when enabled) |
| Save checkpoint | **Yes** / **No** — write a checkpoint at the end of the run |
