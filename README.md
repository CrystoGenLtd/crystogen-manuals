# crystogen-manuals

Documentation for the CrystoGen application, covering installation, the GUI interface, and running simulations.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). The published site is at <https://crystogenltd.github.io/crystogen-manuals/>.

## Structure

```
docs/
├── index.md                  # Home page and quick start
├── occ.md                    # Running OCC to generate energy files
├── running.md                # Running CrystoGen
├── side-menu.md              # Side menu reference
├── installation/             # Platform-specific install guides
└── tabs/                     # GUI tab reference pages
    ├── index.md              # Tab overview
    ├── energy-prediction.md
    ├── structure-options.md
    ├── simulation-options.md
    ├── supersaturation.md
    ├── crystal-colouring.md
    └── ...                   # Mode-specific tabs
```

## Local preview

```bash
pip install mkdocs-material
mkdocs serve
```

Then open <http://127.0.0.1:8000>.
