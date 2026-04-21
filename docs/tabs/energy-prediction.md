# Energy prediction tab

This tab is the interface to [OCC](../occ.md). Use it to generate the interaction-energy files that CrystoGen requires as input.

The tab contains two sub-tabs: **Settings** and **Run**.

---

## Settings sub-tab

### Input file

| Field | Description |
|---|---|
| Input CIF path | Path to the crystal structure file in CIF format |

### Output folder

| Option | Description |
|---|---|
| Save in same folder as CIF | Output files are written next to the input CIF (default) |
| Save in different output folder | Choose a separate destination folder |

### Program settings

| Field | Description |
|---|---|
| OCC executable | Path to the `occ` binary — auto-discovered from `PATH` if present |
| OCC basis path | Directory containing the OCC basis set files |
| Parallel threads | Number of threads OCC may use (integer) |
| Verbosity | Controls how much detail OCC writes to the log |

### Calculation parameters

| Field | Description |
|---|---|
| Energy model | `ce-b3lyp` (default), `ce-1p`, or `gfn2-xtb` |
| Maximum radius | Cutoff distance for interactions (Å, default 30.0) |
| CG radius | Radius passed to CrystoGen (Å, default 3.8) |
| Convergence threshold | SCF convergence criterion |

### Solvent settings

| Field | Description |
|---|---|
| Asymmetric solvent contribution | Include the asymmetric part of the solvent contribution (checkbox) |
| Solvent list | Multi-select widget — choose one or more solvents; each produces a separate `_net.txt` file. Use the search box to filter, and toggle between list and grid views. |

### XTB settings

Shown when the `gfn2-xtb` energy model is selected.

| Field | Description |
|---|---|
| Use XTB | Enable the XTB semi-empirical method |
| XTB solvation model | Solvation model string passed to XTB |

---

## Run sub-tab

| Control | Description |
|---|---|
| Program output | Live log of OCC output streamed during the calculation |
| Clear | Clears the log display |
| Open calculation folder | Opens the output folder in the system file explorer |
| Run OCC | Starts the calculation |
| Stop | Cancels a running calculation |

When the calculation completes, the GUI automatically fills in the structure file and net file fields on the **Structure options** tab.
