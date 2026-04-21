# Simulation options tab

Controls output locations, core simulation parameters, memory usage, and trajectory output.

---

## Output files

| Field | Description |
|---|---|
| Simulation title prefix | String prepended to each output subfolder name |
| Output path | Base folder where timestamped run folders are created |
| Visualiser file storage | Controls whether visualiser files are kept, compressed, or discarded |
| Output grown XYZ | **Yes** / **No** — write a final `.xyz` coordinate file of the grown crystal |

## Simulation setup

| Field | Description |
|---|---|
| Molecules grouped | **Yes** / **No** — treat molecules as rigid groups during growth |
| Temperature | Simulation temperature (°C) |
| Entropy scaling | Scaling factor applied to the entropic contribution |
| Number of iterations | Total number of Monte Carlo growth steps |

## Memory

| Field | Description |
|---|---|
| Calculate memory | **Yes** / **No** — pre-calculate memory requirements before running |
| Max memory (MB) | Upper limit on memory use; the simulation is partitioned to stay within this budget |
| X / Y / Z length | Explicit box dimensions (used when memory calculation is enabled) |

## Output frames

| Field | Description |
|---|---|
| Output mode | **Single frame** — save only the final state; **Movie** — save frames throughout the run |
| Movie frames | Total number of frames to capture (movie mode only) |
| Movie start iteration | Iteration at which frame capture begins |
| Tie final frame | **Yes** / **No** — ensure the last frame coincides with the final iteration |
| Movie final iteration | Iteration of the last captured frame (when not tied to the run end) |
