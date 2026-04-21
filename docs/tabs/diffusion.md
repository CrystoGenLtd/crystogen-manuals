# Diffusion tab

Appears when the simulation mode is set to **diffusion** on the [Structure options](structure-options.md) tab.

Configures the diffusion-limited growth model, including bulk transport parameters and per-facet settings.

---

## Memory options

| Field | Description |
|---|---|
| Parallel threads | Number of threads for the diffusion calculation |

## Simulation options

| Field | Description |
|---|---|
| Bulk concentration | Solute concentration in the bulk solution |
| Lambda | Dimensionless supersaturation parameter |
| Diffusion coefficient | Molecular diffusion coefficient (m²/s) |
| Jump distance | Mean free path for a diffusion jump (Å) |
| Bulk dissolution | Rate constant for dissolution into the bulk |
| Activation energy | Activation energy for the surface attachment step (kcal/mol) |
| Solubility | Equilibrium solubility of the compound |
| Molar volume | Molar volume of the crystal (cm³/mol) |
| Seed radius | Initial seed crystal radius (Å) |

## Facets

| Field | Description |
|---|---|
| Number of facets | How many crystal facets to define; click **Generate fields** to create the rows, or **Read from file** to load from a file |

### Per-facet fields

One section is created per facet after generating fields.

| Field | Description |
|---|---|
| h, k, l | Miller indices of the facet |
