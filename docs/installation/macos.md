# macOS Installation

## 1. Download the right DMG

| Mac type | File to download |
|---|---|
| M1 / M2 / M3 / M4 (Apple Silicon) | `CrystoGen-macos-arm64.dmg` |
| Intel Mac | `CrystoGen-macos-x86_64.dmg` |

Not sure which you have? Click  → **About This Mac**. Look for "Chip" (Apple Silicon) or "Processor" (Intel).

## 2. Install

1. Double-click the downloaded `.dmg` to mount it
2. Drag **CrystoGen** into the **Applications** folder shortcut
3. Eject the disk image

## 3. First launch — bypassing Gatekeeper

Because CrystoGen is ad-hoc signed (not notarized by Apple), macOS Gatekeeper will block the first launch.

### Method A — Right-click open (recommended)

1. Open **Finder** → **Applications**
2. **Right-click** (or Control-click) on **CrystoGen**
3. Select **Open** from the context menu
4. In the dialog that appears, click **Open**

You only need to do this once. After the first approval macOS will remember your choice.

### Method B — System Settings (macOS 13 Ventura and later)

If you already tried double-clicking and got the "can't be opened" error:

1. Open **System Settings** → **Privacy & Security**
2. Scroll down to the **Security** section
3. You will see a message: _"CrystoGen was blocked from use because it is not from an identified developer"_
4. Click **Open Anyway**
5. Authenticate with your password or Touch ID
6. Re-launch CrystoGen from Applications

### Method B — System Preferences (macOS 12 Monterey and earlier)

1. Open **System Preferences** → **Security & Privacy** → **General** tab
2. Click the lock icon and enter your password
3. Click **Open Anyway** next to the CrystoGen message
4. Re-launch CrystoGen

!!! warning "Do not disable Gatekeeper system-wide"
    Commands like `sudo spctl --master-disable` turn off Gatekeeper for all applications. This is unnecessary and reduces your system security. The right-click method above is sufficient and safe.

---

## Uninstalling

Drag **CrystoGen** from Applications to the Trash. To also remove all logs, settings, and licence data, delete the `~/.crystogen/` folder:

```bash
rm -rf ~/.crystogen
```
