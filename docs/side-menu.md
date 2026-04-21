# Side menu

The side menu runs along the left edge of the CrystoGen window. It is divided into three areas: the logo, the action buttons, and the citations.

---

## Action buttons

### Open

Opens a previously saved configuration file and restores all form values to the saved state.

### Save

Saves the current state of all form fields to a configuration file for later use.

### Open output folder

Opens the most recent simulation output folder (or the base output path if no simulation has been run) in the system file explorer.

### Change defaults

Opens a window where you can set the default values used when the form is reset or a new session is started.

### Advanced options

Opens the advanced options panel, which exposes settings not shown in the main tabs.

#### Data output

| Field | Description |
|---|---|
| Final ∆µ | **Yes** / **No** — write the final supersaturation value to the output |
| Number of frames | Number of output frames to retain |
| Initial iteration | Iteration at which output begins |
| Final iteration | Iteration at which output ends |

#### Advanced

| Field | Description |
|---|---|
| Checking sweeps | **1** or **2** — number of lattice-checking sweeps per iteration |
| Parallel mode | **parallel** or **non-parallel** — whether growth steps run concurrently |

#### Log management

| Field | Description |
|---|---|
| Custom log path | Path to a user-specified log file (leave blank to use the global log only) |
| Log save mode | **Global only** — append to `~/.crystogen/CrystoGen_log.csv`; **Custom only** — append to the custom path; **Both** — append to both |
| View global log | Opens the global log file for inspection |

### Help

Opens the help documentation.

### Edit interaction groups

Opens the structure-matching window, which lets you reassign molecules to interaction groups after reading a structure file.

### Update license

Opens the license information popup and lets you enter or update a license key.

### Toggle dark / light

Switches the application theme between light and dark mode.

---

## Citations

The bottom of the side menu lists the papers that should be cited when using CrystoGen:

- M. W. Anderson et al., *Nature*, **544**, 456–459 (2017)
- A. R. Hill et al., *Chem. Sci.*, **12**, 1126–1146 (2021)
- P. R. Spackman et al., *Chem. Sci.*, **14**, 7192–7207 (2023)
