# Supersaturation profile tab

Defines the driving force schedule (∆µ) for the simulation. CrystoGen supports eight profile modes, selected with the numbered mode buttons.

---

## Supersaturation section

| Field | Description |
|---|---|
| Excess any | **Yes** / **No** — whether to apply an excess supersaturation schedule; shows the [Excess supersaturation](excess-supersaturation.md) tab when enabled |
| Mode buttons (1–8) | Select the profile shape — the settings below change depending on the mode chosen |

---

## Profile modes

### Mode 1 — Constant

A single fixed ∆µ for the entire run.

| Field | Description |
|---|---|
| ∆µ | Supersaturation value (kcal/mol) |

### Mode 2 — Two-stage

Two sequential ∆µ values.

| Field | Description |
|---|---|
| ∆µ (stage 1) | First supersaturation value |
| Iterations (stage 1) | Number of iterations at the first value |
| ∆µ (stage 2) | Second supersaturation value |

### Mode 3 — Multi-stage ramp

Full control over a three-stage profile.

| Field | Description |
|---|---|
| Starting ∆µ | Initial supersaturation |
| Iterations start | Iterations at the starting value |
| New ∆µ | Second supersaturation value |
| Iterations new ∆µ | Iterations at the second value |
| Second new ∆µ | Third supersaturation value |
| Iterations equilibration | Iterations in the equilibration stage |
| Iterations temperature | Iterations in the final temperature stage |

### Modes 4–7

Intermediate profile shapes. Each mode exposes the subset of fields relevant to its specific ramp pattern.

### Mode 8 — Annealing

A hardwired annealing schedule. All fields are disabled — the profile is generated automatically.

---

Each mode displays a schematic diagram of the ∆µ profile for reference.
