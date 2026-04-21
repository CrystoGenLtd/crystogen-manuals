# ToposPro Light

!!! warning "Being phased out"
    ToposPro Light is being phased out. Its functionality for generating interaction energy inputs for CrystoGen is superseded by [OCC](occ.md), which is cross-platform and actively maintained. New users should use OCC instead. ToposPro Light will continue to function for existing workflows but will not receive further updates.

!!! note "CrystalGrower references"
    Some buttons, menu items, and settings within ToposPro Light may still refer to CrystoGen as **CrystalGrower** — the previous name of the software. These refer to the same program.

ToposPro Light is a stripped-down version of [ToposPro](https://topospro.com) bundled with CrystoGen for topology analysis on **Windows only**. It contains all the functionality needed to operate CrystoGen on Windows; it does not include features from the full ToposPro package.

---

## Installation (Windows only)

ToposPro Light is included in the **ToposPro_Light** folder of the CrystoGen download (register at [crystogen.org](https://crystogen.org) to receive the link).

### 1. Uninstall any existing ToposPro

If a previous version of ToposPro is installed, uninstall it before proceeding.

### 2. Run the installer

Select the installer matching your Windows version:

| File | Windows version |
|---|---|
| `ToposPro_Setup_for_CrystoGen_x64.exe` | 64-bit (recommended) |
| `ToposPro_Setup_for_CrystoGen_x32.exe` | 32-bit |

Double-click to run and follow the installer prompts.

!!! warning "Do not update ToposPro from within the application"
    The in-app update prompt targets the full commercial version of ToposPro, which does not include the CrystoGen-specific features. Updating will replace this light version with an incompatible build. Ignore any update notifications.

### 3. Running both versions side by side

If you need both the full ToposPro and ToposPro Light installed simultaneously, install them into separate folders and create separate desktop or Start Menu shortcuts pointing to each executable. The full version is available at [topospro.com](https://topospro.com) for non-commercial users.

---

## Recommended alternative: OCC

[OCC (Open Computational Chemistry)](occ.md) is the recommended replacement for energy prediction and structure preparation on all platforms. It is included in the CrystoGen download for Windows, macOS, and Linux.
