# macOS Installation

Download files from the appropriate folder of the download — **Mac-ARM** for Apple Silicon, **Mac-Intel** for Intel Macs (register at [crystogen.org](https://crystogen.org) to receive the link).

Not sure which you have? Click  → **About This Mac**. Look for "Chip" (Apple Silicon) or "Processor" (Intel).

## GUI

### 1. Download

| Mac type | File |
|---|---|
| Apple Silicon (M1/M2/M3/M4) | `CrystoGen-macos-arm64.dmg` |
| Intel | `CrystoGen-macos-x86_64.dmg` |

### 2. Install

1. Double-click the downloaded `.dmg` to mount it
2. Drag **CrystoGen** into the **Applications** folder shortcut
3. Eject the disk image

### 3. First launch — bypassing Gatekeeper

Because CrystoGen is ad-hoc signed (not notarized by Apple), macOS Gatekeeper will block the first launch.

#### Method A — Right-click open (recommended)

1. Open **Finder** → **Applications**
2. **Right-click** (or Control-click) on **CrystoGen**
3. Select **Open** from the context menu
4. In the dialog that appears, click **Open**

You only need to do this once. After the first approval macOS will remember your choice.

#### Method B — System Settings (macOS 13 Ventura and later)

If you already tried double-clicking and got the "can't be opened" error:

1. Open **System Settings** → **Privacy & Security**
2. Scroll down to the **Security** section
3. You will see a message: _"CrystoGen was blocked from use because it is not from an identified developer"_
4. Click **Open Anyway**
5. Authenticate with your password or Touch ID
6. Re-launch CrystoGen from Applications

#### Method B — System Preferences (macOS 12 Monterey and earlier)

1. Open **System Preferences** → **Security & Privacy** → **General** tab
2. Click the lock icon and enter your password
3. Click **Open Anyway** next to the CrystoGen message
4. Re-launch CrystoGen

!!! warning "Do not disable Gatekeeper system-wide"
    Commands like `sudo spctl --master-disable` turn off Gatekeeper for all applications. This is unnecessary and reduces your system security. The right-click method above is sufficient and safe.

### 4. First launch — licence

On first launch, click **Update license** in the GUI and navigate to `CrystoGen.key` from the download folder.

---

## CLI

!!! note
    The CLI is recommended only for users comfortable working in the terminal. For HPC use, SLURM job templates are included in the **HPC_scripts** folder of the download.

### 1. Download

Two variants are available for each architecture:

| Mac type | File | Description |
|---|---|---|
| Apple Silicon | `crystogen-1.5.0-macos-arm64.tar.gz` | Standard build |
| Apple Silicon | `crystogen-1.5.0-macos-arm64-openmp.tar.gz` | OpenMP parallelised build |
| Intel | `crystogen-1.5.0-macos-x86_64.tar.gz` | Standard build |
| Intel | `crystogen-1.5.0-macos-x86_64-openmp.tar.gz` | OpenMP parallelised build |

### 2. Extract

```bash
tar -xzf crystogen-1.5.0-macos-arm64.tar.gz   # adjust filename as needed
```

The archive extracts to a versioned folder. The `crystogen` binary is inside the `bin/` subdirectory alongside `cg-preprocess` and `cg-decrypt-key`.

### 3. Make executable (if needed)

```bash
chmod +x path/to/bin/crystogen
```

### 4. Licence

Place `CrystoGen.key` in the same directory as the `crystogen` binary. See [Licence key](../licence-key.md) for all configuration methods.

### 5. Run

```bash
cd /path/to/simulation/folder
/path/to/bin/crystogen < addinput.txt
```

See [Running CrystoGen](../running.md) and [Input files](../input-files.md) for details on preparing `input.txt` and `addinput.txt`. Template input files are included in the **Structure Files/Input_files_CLI** folder of the download.

---

## Uninstalling

Drag **CrystoGen** from Applications to the Trash. To also remove logs, settings, and licence data:

```bash
rm -rf ~/.crystogen
```
