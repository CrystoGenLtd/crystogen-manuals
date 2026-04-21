# Licence key

CrystoGen is time-limited software. The licence key file (`CrystoGen.key`) is included in the download folder and is required for the CLI binary to run. Licences can be renewed at [crystogen.org](https://crystogen.org).

The CLI binary tries to find the key in this order:

1. The `CG_LICENSE_KEY` environment variable
2. A file named `CrystoGen.key` in the working directory where the simulation is run

The GUI sets `CG_LICENSE_KEY` automatically to `~/.crystogen/CrystoGen.key` whenever it launches a simulation subprocess, so no manual configuration is needed for GUI use after the initial setup.

---

## Method 1 — Place the key in the simulation directory (simplest)

Copy `CrystoGen.key` into the folder from which you run the simulation (i.e. the working directory when you invoke `crystogen`). The binary will find it automatically with no further configuration.

```
my-simulation/
├── addinput.txt
├── input.txt
└── CrystoGen.key
```

---

## Method 2 — Environment variable pointing to a file path

Set `CG_LICENSE_KEY` to the full path of the key file. This is useful when you want to keep the key in a central location and share it across multiple CLI installations, or when running on HPC systems.

=== "macOS / Linux"

    ```bash
    export CG_LICENSE_KEY=~/.crystogen/CrystoGen.key
    ```

    To make this permanent, add the line to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.).

    For SLURM jobs, add it to the job script:

    ```bash
    #SBATCH ...
    export CG_LICENSE_KEY=/path/to/CrystoGen.key
    /path/to/bin/crystogen < addinput.txt
    ```

=== "Windows"

    In Command Prompt:

    ```bat
    set CG_LICENSE_KEY=C:\path\to\CrystoGen.key
    ```

    In PowerShell:

    ```powershell
    $env:CG_LICENSE_KEY = "C:\path\to\CrystoGen.key"
    ```

    To set it permanently, add it as a system or user environment variable via **System Properties** → **Environment Variables**.

---

## Method 3 — Environment variable containing the key content directly

`CG_LICENSE_KEY` can also hold the key string itself rather than a path to a file. The binary will try to parse it as a file path first; if that fails, it treats the value as key content.

This is useful for CI/CD pipelines or containerised environments where writing files is inconvenient:

=== "macOS / Linux"

    ```bash
    export CG_LICENSE_KEY="<paste key content here>"
    ```

=== "Windows"

    ```powershell
    $env:CG_LICENSE_KEY = "<paste key content here>"
    ```

---

## GUI first-time setup

The GUI stores the key at `~/.crystogen/CrystoGen.key` and reads it from there on every run. To set it up:

1. Open CrystoGen
2. Click **Update license** in the side menu
3. Navigate to `CrystoGen.key` from the download folder

The file is copied to `~/.crystogen/CrystoGen.key`. No further action is needed unless the licence expires.

---

## Licence expiry

CrystoGen licences are time-limited. When a licence expires the binary will stop running. To renew, visit [crystogen.org](https://crystogen.org), then repeat the setup steps above with the new key file.
