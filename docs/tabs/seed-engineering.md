# Seed engineering tab

Appears when the simulation mode is set to **seed_engineering** on the [Structure options](structure-options.md) tab.

Defines the initial seed shape used at the start of a simulation.

---

## Seed mode

Select one of the four mode buttons to choose the seed geometry. The fields below change to match the selected shape.

### Slice

Cuts the crystal along a plane.

| Field | Description |
|---|---|
| h, k, l | Miller indices of the cutting plane |
| Cut shift | Fractional shift of the cut plane along the normal direction |

### Sphere

Initialises a spherical seed.

| Field | Description |
|---|---|
| Radius | Radius of the sphere (Å) |

### Rhomb

Initialises a rhomboidal seed.

| Field | Description |
|---|---|
| Rhomb size | Edge length of the rhombus |

### Hemisphere

Initialises a hemispherical seed.

| Field | Description |
|---|---|
| h, k, l | Miller indices defining the flat face of the hemisphere |
| Radius | Radius of the hemisphere (Å) |
