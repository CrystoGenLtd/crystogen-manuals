# Running CrystoGen

## Launching the application

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

---

## Running CrystoGen

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
