# Linux Installation

Download files from the **Linux** folder of the download (register at [crystogen.org](https://crystogen.org) to receive the link).

## GUI

### 1. Download

Download `CrystoGen-GUI-linux-x86_64.tar.gz`.

### 2. Extract

```bash
tar -xzf CrystoGen-GUI-linux-x86_64.tar.gz
cd CrystoGen-GUI-linux-x86_64
```

### 3. Make executable (if needed)

```bash
chmod +x CrystoGen-GUI
```

### 4. First launch — licence

On first launch, click **Update license** in the GUI and navigate to `CrystoGen.key` from the download folder.

### 5. Run

```bash
./CrystoGen-GUI
```

---

## CLI

!!! note
    The CLI is recommended only for users comfortable working in the terminal. For HPC use, SLURM job templates are included in the **HPC_scripts** folder of the download.

### 1. Download

Two variants are available:

| File | Description |
|---|---|
| `crystogen-1.5.0-linux-x86_64.tar.gz` | Standard build |
| `crystogen-1.5.0-linux-x86_64-openmp.tar.gz` | OpenMP parallelised build (recommended for multi-core HPC nodes) |

### 2. Extract

```bash
tar -xzf crystogen-1.5.0-linux-x86_64.tar.gz
```

The archive extracts to a versioned folder. The `crystogen` binary is inside the `bin/` subdirectory alongside `cg-preprocess` and `cg-decrypt-key`.

### 3. Make executable (if needed)

```bash
chmod +x path/to/bin/crystogen
```

### 4. Licence

Place `CrystoGen.key` in the directory from which you will run the simulation (your working directory). See [Licence key](../licence-key.md) for all configuration methods.

### 5. Run

```bash
cd /path/to/simulation/folder
/path/to/bin/crystogen < addinput.txt
```

See [Running CrystoGen](../running.md) and [Input files](../input-files.md) for details on preparing `input.txt` and `addinput.txt`. Template input files are included in the **Structure Files/Input_files_CLI** folder of the download.

---

## GUI Dependencies

The GUI binary bundles Python and most libraries, but requires system Tk/Tcl libraries:

=== "Debian / Ubuntu"
    ```bash
    sudo apt-get install python3-tk
    ```

=== "Fedora / RHEL"
    ```bash
    sudo dnf install python3-tkinter
    ```

=== "Arch"
    ```bash
    sudo pacman -S tk
    ```

---

## Antivirus / security warnings

Some security tools flag PyInstaller-packaged executables as false positives. If the GUI or CLI binary is blocked, add an exclusion for the relevant folder.

---

## Optional: Add GUI to PATH

```bash
sudo ln -s /path/to/CrystoGen-GUI-linux-x86_64/CrystoGen-GUI /usr/local/bin/crystogen
```

## Optional: Desktop shortcut

Create `/home/$USER/.local/share/applications/crystogen.desktop`:

```ini
[Desktop Entry]
Name=CrystoGen
Exec=/path/to/CrystoGen-GUI-linux-x86_64/CrystoGen-GUI
Icon=/path/to/CrystoGen-GUI-linux-x86_64/cg_logo.png
Type=Application
Categories=Science;
```

## Uninstalling

Delete the extracted folder(s). To also remove logs, settings, and licence data:

```bash
rm -rf ~/.crystogen
```

If you created a symlink or desktop shortcut, remove those too:

```bash
sudo rm /usr/local/bin/crystogen
rm ~/.local/share/applications/crystogen.desktop
```
