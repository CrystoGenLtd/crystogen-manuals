# Windows Installation

## 1. Download

Download `CrystoGen-windows-x86_64.zip` from the [latest release](https://github.com/CrystoGenLtd/tkinter_gui/releases/latest).

## 2. Extract

Right-click the `.zip` file and select **Extract All**, then choose a destination folder (e.g. `C:\Program Files\CrystoGen` or your Desktop).

## 3. Run

Open the extracted folder and double-click **CrystoGen.exe**.

---

## Bypassing Windows SmartScreen

CrystoGen is not code-signed with a commercial certificate, so Windows SmartScreen may display a warning on first launch.

### "Windows protected your PC" dialog

If you see this dialog:

1. Click **More info** (below the warning text)
2. Click **Run anyway**

<!-- ![SmartScreen dialog](../img/windows-smartscreen.png){ loading=lazy } -->

!!! info "Why does this happen?"
    SmartScreen flags executables that are new or have low download counts. This is expected for self-distributed software without a paid code-signing certificate. The application is safe to run.

### Antivirus false positives

Some antivirus tools flag PyInstaller-packaged executables. If your AV quarantines the file:

1. Restore it from quarantine
2. Add an exclusion for the CrystoGen folder

---

## Uninstalling

Delete the extracted folder. CrystoGen does not write to the Windows registry or create system-level files. To also remove all logs, settings, and licence data, delete the `.crystogen` folder in your home directory:

```
C:\Users\<YourName>\.crystogen\
```
