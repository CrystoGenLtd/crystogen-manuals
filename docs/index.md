# CrystoGen

CrystoGen is a Monte Carlo crystal-growth simulator for predicting crystal habit and nanoscale surface topography. It is available as a **GUI application** for interactive use and as a standalone **CLI binary** for scripted or HPC runs.

CrystoGen is closed-source software with a time-limited licence. Licences and downloads are managed through [crystogen.org](https://crystogen.org). To access the software, **register via the form on [crystogen.org](https://crystogen.org)** to receive a link to the download folder.

## What's included

Each download folder contains platform-specific subfolders (`Windows`, `Linux`, `Mac-ARM`, `Mac-Intel`). Every subfolder includes:

| Component | Description |
|---|---|
| CrystoGen GUI | Graphical application for running simulations interactively |
| CrystoGen CLI | Command-line binary for scripted and HPC workflows |
| OCC | Open Computational Chemistry — DFT energy prediction (required for solvent screens) |
| CGAspects | Data processing and visualisation tool (Zingg diagrams, crystal rendering) |

The download folder also contains:

- **Structure Files** — example `_cg.txt` structure files (tile and net) and CLI input file templates (`input.txt`, `addinput.txt`, `net.txt`, etc.)
- **HPC_scripts** — SLURM job templates for common workflows (solvent screen, growth rates, parameter sweeps)
- **ToposPro_Light** — Windows-only topology analysis tool *(Windows folder only; [being phased out](topospro.md))*
- **CGVisualiser** — Windows-only crystal visualiser *(Windows folder only; [being phased out](cgvisualiser.md))*

## Download files

=== "Windows"

    From the **Windows** folder in the download:

    | File | Description |
    |---|---|
    | `CrystoGen-windows-x86_64.zip` | GUI application |
    | `crystogen-1.5.0-windows-x86_64.tar.gz` | CLI binary |
    | `crystogen-1.5.0-windows-x86_64-openmp.tar.gz` | CLI binary with OpenMP parallelisation |
    | `occ-0.8.8-windows-x86_64.tar.xz` | OCC energy prediction tool |
    | `CGAspects-windows-x86_64.zip` | CGAspects visualisation tool |

=== "macOS (Apple Silicon)"

    From the **Mac-ARM** folder in the download:

    | File | Description |
    |---|---|
    | `CrystoGen-macos-arm64.dmg` | GUI application |
    | `crystogen-1.5.0-macos-arm64.tar.gz` | CLI binary |
    | `crystogen-1.5.0-macos-arm64-openmp.tar.gz` | CLI binary with OpenMP parallelisation |
    | `occ-0.8.8-macos-arm64.tar.xz` | OCC (ARM build, recommended) |
    | `occ-0.8.8-macos-universal.tar.xz` | OCC (universal build) |
    | `CGAspects-macos-arm64.dmg` | CGAspects visualisation tool |

=== "macOS (Intel)"

    From the **Mac-Intel** folder in the download:

    | File | Description |
    |---|---|
    | `CrystoGen-macos-x86_64.dmg` | GUI application |
    | `crystogen-1.5.0-macos-x86_64.tar.gz` | CLI binary |
    | `crystogen-1.5.0-macos-x86_64-openmp.tar.gz` | CLI binary with OpenMP parallelisation |
    | `occ-0.8.8-macos-x86_64.tar.xz` | OCC (Intel build, recommended) |
    | `occ-0.8.8-macos-universal.tar.xz` | OCC (universal build) |
    | `CGAspects-macos-x86_64.dmg` | CGAspects visualisation tool |

=== "Linux"

    From the **Linux** folder in the download:

    | File | Description |
    |---|---|
    | `CrystoGen-linux-x86_64.tar.gz` | GUI application |
    | `crystogen-1.5.0-linux-x86_64.tar.gz` | CLI binary |
    | `crystogen-1.5.0-linux-x86_64-openmp.tar.gz` | CLI binary with OpenMP parallelisation |
    | `occ-0.8.8-linux-x86_64-static.tar.xz` | OCC with static libraries (recommended) |
    | `occ-0.8.8-linux-x86_64.tar.xz` | OCC with dynamic libraries |
    | `CGAspects-linux-x86_64.tar.gz` | CGAspects visualisation tool |

## Quick start

=== "GUI"

    1. Register at [crystogen.org](https://crystogen.org) and download the GUI file for your platform
    2. Install — see the installation guide for your OS: [Windows](installation/windows.md) · [macOS](installation/macos.md) · [Linux](installation/linux.md)
    3. **First launch security warning** — Windows may show a SmartScreen dialog; macOS will block the app via Gatekeeper. See [Bypassing SmartScreen](installation/windows.md#bypassing-windows-smartscreen) or [Bypassing Gatekeeper](installation/macos.md#first-launch--bypassing-gatekeeper) for instructions.
    4. On first launch, click **Update license** and navigate to `CrystoGen.key` from the download folder
    5. See [Running CrystoGen](running.md) for a step-by-step guide

=== "CLI"

    !!! note
        The CLI is recommended only for users comfortable working in the terminal. For HPC use, SLURM job templates are included in the **HPC_scripts** folder of the download.

    1. Register at [crystogen.org](https://crystogen.org) and download the CLI `.tar.gz` for your platform
    2. Extract it — the `crystogen` binary is in the `bin/` subdirectory
    3. Place `CrystoGen.key` in the same folder as the `crystogen` binary
    4. See the installation guide for your OS: [Windows](installation/windows.md) · [macOS](installation/macos.md) · [Linux](installation/linux.md), and [Running CrystoGen](running.md) for invocation details

## Licence

CrystoGen uses a time-limited licence. When a licence expires the software will cease to function. Licences can be renewed at [crystogen.org](https://crystogen.org).

## System requirements

| | Minimum |
|---|---|
| OS | Windows 10, macOS 12, Ubuntu 20.04 |
| Architecture | x86_64 (all platforms), arm64 (macOS only) |
| RAM | 4 GB |
| Disk | 200 MB free |
