# Linux Installation

## 1. Download

Download `CrystoGen-linux-x86_64.tar.gz` from the [latest release](https://github.com/CrystoGenLtd/tkinter_gui/releases/latest).

## 2. Extract

```bash
tar -xzf CrystoGen-linux-x86_64.tar.gz
cd CrystoGen-linux-x86_64
```

## 3. Make executable (if needed)

```bash
chmod +x CrystoGen
```

## 4. Run

```bash
./CrystoGen
```

---

## Dependencies

The binary bundles Python and most libraries, but requires system Tk/Tcl libraries:

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

## Optional: Add to PATH

To launch CrystoGen from anywhere:

```bash
sudo ln -s /path/to/CrystoGen-linux-x86_64/CrystoGen /usr/local/bin/crystogen
```

Then run with `crystogen` from any terminal.

## Uninstalling

Delete the extracted folder. To also remove all logs, settings, and licence data, delete the `~/.crystogen/` folder:

```bash
rm -rf ~/.crystogen
```

If you created a symlink or desktop shortcut, remove those too:

```bash
sudo rm /usr/local/bin/crystogen
rm ~/.local/share/applications/crystogen.desktop
```

---

## Optional: Desktop shortcut

Create `/home/$USER/.local/share/applications/crystogen.desktop`:

```ini
[Desktop Entry]
Name=CrystoGen
Exec=/path/to/CrystoGen-linux-x86_64/CrystoGen
Icon=/path/to/CrystoGen-linux-x86_64/cg_logo.png
Type=Application
Categories=Science;
```
