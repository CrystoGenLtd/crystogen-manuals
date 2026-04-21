# CrystoGen

CrystoGen is a GUI application for crystal growth simulation. Pre-built binaries are available for Windows, macOS (Apple Silicon and Intel), and Linux — no Python installation required.

## Download

Get the latest release from the [GitHub Releases page](https://github.com/CrystoGenLtd/tkinter_gui/releases/latest).

| Platform | File | Notes |
|---|---|---|
| macOS (Apple Silicon) | `CrystoGen-macos-arm64.dmg` | M1/M2/M3/M4 Macs |
| macOS (Intel) | `CrystoGen-macos-x86_64.dmg` | Intel Macs |
| Windows | `CrystoGen-windows-x86_64.zip` | Windows 10/11, 64-bit |
| Linux | `CrystoGen-linux-x86_64.tar.gz` | x86_64 |

## Quick Start

=== "Windows"
    1. Download the `.zip` file
    2. Extract and run `CrystoGen.exe`
    3. If Windows SmartScreen blocks the app, see [Windows installation](installation/windows.md)

=== "macOS"
    1. Download the `.dmg` valid for your CPU architecture
    2. Open the DMG and drag CrystoGen to Applications
    3. If macOS blocks the app, see [macOS installation](installation/macos.md)

=== "Linux"
    1. Download and extract the `.tar.gz`
    2. Run `./CrystoGen`
    3. See [Linux installation](installation/linux.md) for dependencies

## Interface

Once installed, the application opens with a tabbed workspace and a [side menu](side-menu.md) on the left. The side menu gives access to file open/save, defaults, advanced options, log management, and the license. See [Running CrystoGen](running.md) for a step-by-step guide.

## System Requirements

| | Minimum |
|---|---|
| OS | Windows 10, macOS 12, Ubuntu 20.04 |
| Architecture | x86_64 (all platforms), arm64 (macOS only) |
| RAM | 4 GB |
| Disk | 200 MB free |
