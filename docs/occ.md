# Running OCC

OCC (Open Computational Chemistry) calculates the intermolecular interaction energies that CrystoGen uses as input. This step is only required if you do not already have pre-calculated `.txt` energy files.

## Required inputs

| Input | Description |
|---|---|
| CIF file | Crystal structure in CIF format |
| OCC executable | Path to the `occ` binary — auto-discovered from `PATH` if available |
| Basis path | Directory containing the OCC basis set files |

## Steps

1. Open the **Energy prediction** tab in the GUI.
2. Load your CIF file using the file browser.
3. Select one or more **solvents** from the list. Each selected solvent produces a separate `_net.txt` interaction-energy file.
4. Configure the calculation parameters as needed — see the [Energy prediction tab](tabs/energy-prediction.md) for a full description of all settings.
5. Click **Run OCC**.

Output is streamed live to the log panel. A `.stdout` file is saved alongside the output for each solvent.

## Output files

When the calculation finishes, two types of files are written for each solvent:

- `<name>_cg.txt` — crystal structure file used by CrystoGen
- `<name>_<solvent>_net.txt` — interaction energies for that solvent

If you selected multiple solvents, the net files are collected inside a `NETs/` subfolder. On completion, the GUI automatically populates the CrystoGen structure and net file fields so you can proceed directly to the next step.
