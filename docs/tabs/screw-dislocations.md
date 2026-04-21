# Screw dislocations tab

Appears when **Screw** is set to **Yes** on the [Structure options](structure-options.md) tab.

Defines the screw dislocation geometry used in the simulation.

---

## Screw dislocations section

| Field | Description |
|---|---|
| Screw file | Path to a file containing pre-defined screw dislocation parameters — load with the **read file** button |
| Number of screws | How many screw dislocation families to define; click **Generate fields** to create the corresponding input rows |
| Space group | Space group of the crystal |
| Unique axis | **b** or **c** — the unique axis for monoclinic crystals |
| Hex/Rhom | **h** (hexagonal) or **r** (rhombohedral) setting |

## Per-screw family fields

One section is created per screw family after clicking **Generate fields**.

| Field | Description |
|---|---|
| h, k, l | Miller indices of the dislocation direction |
| Translation | Burgers vector translation component |
| Shifts | Positional shifts for the dislocation core |
| Type | **single** — one dislocation; **family** — symmetry-related set; **spray 25** — spray pattern of 25 |
| Spread | Spatial spread of the dislocation pattern (used for family and spray types) |
