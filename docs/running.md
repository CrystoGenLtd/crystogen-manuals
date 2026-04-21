# Running CrystoGen

## Launching the application

=== "GUI"

    === "Windows"
        Double-click **CrystoGen.exe** in the extracted folder, or create a shortcut to it on your Desktop.

    === "macOS"
        Open **Finder** → **Applications** → double-click **CrystoGen**.

        Alternatively, use Spotlight: press `⌘ Space`, type `CrystoGen`, press `Return`.

    === "Linux"
        ```bash
        ./CrystoGen
        ```
        Or use the desktop shortcut if you created one during installation.

    Once open, the application shows a tabbed workspace and a [side menu](side-menu.md) on the left with file, settings, and tool actions.

=== "Terminal"

    The `crystogen` CLI binary is a separate download included in the CrystoGen download folder (register at [crystogen.org](https://crystogen.org)). Extract the `.tar.gz` for your platform — the binary is in the `bin/` subdirectory. See the installation page for your OS for step-by-step instructions.

    **Licence:** place `CrystoGen.key` in the directory from which you run the simulation (your working directory). See [Licence key](licence-key.md) for all configuration methods including the `CG_LICENSE_KEY` environment variable.

    **OpenMP:** for multi-core HPC nodes, use the `-openmp` variant of the CLI archive.

    **HPC:** SLURM job templates for common workflows (solvent screen, growth rates, parameter sweeps) are included in the **HPC_scripts** folder of the download.

---

## Running a simulation

=== "GUI"

    CrystoGen simulates crystal growth using the interaction energies (from [OCC](occ.md) or manual entries).

    ### Required inputs

    | Input | Description |
    |---|---|
    | Structure file | `_cg.txt` file — auto-populated after OCC, or set manually |
    | Net file / folder | Single `_net.txt` file, or a folder of net files for multi-solvent runs |

    ### Steps

    1. Switch to any CrystoGen tab (not the Energy prediction tab).
    2. Confirm the **Structure file** and **Net file** paths are correct (auto-filled if you ran OCC first).
    3. Set the core simulation parameters:
        - **Temperature** (°C)
        - **Number of iterations**
        - **∆µ** supersaturation values (kcal/mol)
        - **Simulation mode** — `normal`, `diffusion`, `nucleation`, `surface`, etc.
    4. Optionally configure your **[parameters](tabs/index.md)**: for any parameter marked with a vary option, set a start value, end value, and step size. The GUI generates and runs all combinations automatically, placing each in its own numbered subfolder.
    5. Click **Run CG**.

    The simulation runs in a background thread so the GUI remains responsive. Progress is streamed to the log panel and you can stop a run at any time with **Stop**.

    ### Output folder structure

    Each run creates a timestamped folder:

    ```
    <output_path>/
    └── YYYYMMDD_HHMMSS/
        ├── GUI_simulation_data.txt      (full form state snapshot)
        ├── YYYYMMDD_HHMMSS_summary.csv  (varied parameter combinations)
        ├── <prefix>_1/                  (simulation 1)
        │   ├── input.txt
        │   ├── addinput.txt
        │   ├── net.txt
        │   ├── CrystoGen_log.csv
        │   └── ...
        ├── <prefix>_2/
        └── ...
    ```

=== "Terminal"

    The `crystogen` binary reads its main configuration from `input.txt` in the **working directory**, and receives additional mode-specific parameters via **stdin** from `addinput.txt`.

    ### Required files

    | File | Description |
    |---|---|
    | `input.txt` | 27-line configuration file — one value per line |
    | `addinput.txt` | Mode-dependent additional parameters piped via stdin |
    | Structure file | `_cg.txt` file referenced in `input.txt` line 6 |
    | Net / tile file | Referenced by the structure file |

    ### Invocation

    Place `input.txt` and `addinput.txt` in the same folder and run from that folder:

    === "Windows"
        ```bat
        \path\to\bin\crystogen.exe < addinput.txt
        ```

    === "macOS / Linux"
        ```bash
        cd /path/to/simulation/folder
        /path/to/bin/crystogen < addinput.txt
        ```

    Output files are written to the directory specified in `input.txt` line 1. See [Input files](input-files.md) for the full format of `input.txt` and `addinput.txt`.

---

## Log files

Each completed simulation writes a `CrystoGen_log.csv` inside its own output subfolder. After the simulation finishes, the GUI automatically appends that file to a persistent global log.

**Global log location:**

```
~/.crystogen/CrystoGen_log.csv
```

The directory `~/.crystogen/` is created automatically on first use.

**Log save mode** controls where entries are appended and can be changed in the GUI settings:

| Mode | Behaviour |
|---|---|
| Global only (default) | Append to `~/.crystogen/CrystoGen_log.csv` only |
| Custom only | Append to a user-specified file path only |
| Both | Append to both the global log and the custom path |

To set a custom log path, enter the full file path in the **Custom log path** field in the settings panel. If the file does not exist it will be created; if the destination directory does not exist it will be created too.

If no local `CrystoGen_log.csv` is found in a simulation folder (e.g. the simulation was stopped early), a warning is printed to the log panel in orange and no entry is appended.

---

## Troubleshooting

### Application won't start

- **Windows**: Ensure you extracted the full zip — don't run the exe from inside the zip.
- **macOS**: Make sure you completed the [Gatekeeper bypass](installation/macos.md) steps.
- **Linux**: Confirm Tk is installed (`python3-tk` / `tkinter` package for your distro).

### Blank or missing window

On some Linux systems with HiDPI displays, the window may appear off-screen. Try:

```bash
GDK_SCALE=1 ./CrystoGen
```

### Performance issues

CrystoGen bundles its own Python runtime. Startup may take a few seconds on first launch while the OS loads the bundled libraries — this is normal.

### Terminal: "Permission denied" or "Executable not found"

Ensure the `crystogen` binary is executable:

```bash
chmod +x /path/to/crystogen
```

Check that `CG_LICENSE_KEY` points to a valid key file:

```bash
ls ~/.crystogen/CrystoGen.key
```
