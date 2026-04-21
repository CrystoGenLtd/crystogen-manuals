# Net options tab

Appears when **Structure type** is set to **Net** on the [Structure options](structure-options.md) tab.

Configures how the intermolecular interaction energies from the net file are weighted and scaled.

---

## Weightings

| Field | Description |
|---|---|
| Weightings for multiple bonds | **Yes** / **No** — apply coordination-dependent weightings to interactions |

## Interaction scalings

A set of scaling entries (interaction energies) is generated automatically based on the interaction groups found in the loaded net file. Each entry scales the energy contribution of one interaction group.

| Field | Description |
|---|---|
| Scaling (per group) | Multiplicative factor applied to the interaction energy for that group |

## Weightings for multiple bonds

Shown when **Weightings for multiple bonds** is enabled. Entries are generated per coordination number found in the structure.

| Field | Description |
|---|---|
| Weighting (per coordination) | Weighting factor for interactions at each coordination level |
