# GUI Tabs

The CrystoGen interface is organised as a tabbed notebook. Some tabs are always visible; others appear only when a specific mode is selected.

## Always visible

| Tab | Purpose |
|---|---|
| [Energy prediction](energy-prediction.md) | Run OCC to generate interaction-energy files from a CIF |
| [Structure options](structure-options.md) | Select structure/net files and simulation mode |
| [Simulation options](simulation-options.md) | Output paths, temperature, iterations, and memory settings |
| [Supersaturation profile](supersaturation.md) | Define the supersaturation schedule |
| [Crystal colouring](crystal-colouring.md) | Configure layer colouring of the output crystal |

## Mode-specific (conditional)

These tabs appear automatically once the corresponding mode or option is enabled on the **Structure options** tab.

| Tab | Appears when |
|---|---|
| [Net options](net-options.md) | Structure type set to **Net** |
| [Tile options](tile-options.md) | Structure type set to **Tile** |
| [Screw dislocations](screw-dislocations.md) | **Screw** set to **Yes** |
| [Screw stress](screw-stress.md) | Simulation mode set to **screw_stress** |
| [Growth modifier](growth-modifier.md) | Simulation mode set to **growth_modifier** |
| [Diffusion](diffusion.md) | Simulation mode set to **diffusion** |
| [Nucleation](nucleation.md) | Simulation mode set to **nucleation** |
| [Surface](surface.md) | Simulation mode set to **surface** |
| [Seed engineering](seed-engineering.md) | Simulation mode set to **seed_engineering** |
| [Excess supersaturation](excess-supersaturation.md) | **Excess any** set to **Yes** on the Supersaturation tab |
