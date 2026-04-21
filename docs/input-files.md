# Input files

When running `crystogen` from the terminal, the simulation is configured through two plain-text files: `input.txt` and `addinput.txt`. Both must be present in the working directory when the binary is invoked.

The GUI writes these files automatically before each run. Copies are saved alongside the output for reference.

Template versions of all CLI input files (`input.txt`, `addinput.txt`, `net.txt`, `screw.txt`, `diffusion_input.txt`, `facets.txt`) are included in the **Structure Files/Input_files_CLI** folder of the CrystoGen download.

---

## input.txt

`input.txt` contains 27 values, one per line, followed by blank lines and human-readable comments (ignored by the binary).

| Line | Field | Accepted values | Description |
|------|-------|-----------------|-------------|
| 1 | `output_path` | directory path | Root directory for output; the simulation creates a timestamped subfolder here |
| 2 | `title` | string | Prefix used for the output subfolder name |
| 3 | `checkpoint_yes_no` | `yes` / `no` | Load a checkpoint to resume a previous run |
| 4 | `checkpoint_path` | file path | Path to checkpoint file (required if line 3 is `yes`) |
| 5 | `checkpoint_save` | `yes` / `no` | Save a checkpoint at the end of the run |
| 6 | `structure_file` | file path | Path to the `_cg.txt` structure file |
| 7 | `simulation_mode` | `normal` `growth_modifier` `ordered` `cut` `surface` `screw_stress` `nucleation` `diffusion` | Simulation mode |
| 8 | `screw_yes_no` | `yes` / `no` | Enable screw dislocations |
| 9 | `screw_path` | file path | Path to screw dislocation file (required if line 8 is `yes`) |
| 10 | `checking_sweeps` | integer | Number of checking sweeps; `1` = normal, `2` = clear internal |
| 11 | `entropy_scaling` | `0`–`1` | Entropy scale factor for surface sites; `1` = no scaling |
| 12 | `crystal_type` | `tile` / `net` | Framework crystal (`tile`) or network/molecular crystal (`net`) |
| 13 | `calculate_memory` | `yes` / `no` | Calculate required memory before running |
| 14 | `max_memory` | integer (MBytes) | Maximum memory to use; default `10000` |
| 15 | `temperature` | float (°C) | Simulation temperature in Celsius |
| 16 | `num_iterations` | integer | Number of Monte Carlo iterations |
| 17 | `delmu_mode` | `1`–`8` | Supersaturation schedule mode |
| 18 | `excess_any` | `yes` / `no` | Use excess supersaturation for any component (always `yes` for MOFs) |
| 19 | `starting_delmu` | float (kcal/mol) | Starting ∆µ value |
| 20 | `movie_frames` | integer | Number of movie frames to output |
| 21 | `movie_it_initial` | integer | Iteration number of first movie frame (default `1`) |
| 22 | `movie_it_final` | integer | Iteration number of last movie frame (default = `num_iterations`) |
| 23 | `delmu_frames` | integer | Number of ∆µ data outputs |
| 24 | `delmu_it_initial` | integer | Iteration number of first ∆µ output (default `1`) |
| 25 | `delmu_it_final` | integer | Iteration number of last ∆µ output (default = `num_iterations`) |
| 26 | `tiles_represented` | `yes` / `no` | Visualise crystal terraces |
| 27 | `zebra_path` | file path | Path to crystal terrace colouring file (required if line 26 is `yes`) |

**Minimal example** (`normal` mode, `net` crystal, no checkpoint, memory auto-calculated):

```
/home/user/crystogen_output/
my_run
no
none
no
/home/user/structures/compound_cg.txt
normal
no
/path/to/screw.txt
1
1.0
net
yes
10000
25.0
100000
2
no
-5.0
1
1
100000
1000
1
100000
no
none
```

---

## addinput.txt

`addinput.txt` is piped to the binary via stdin. Its contents are mode-dependent — values are written one per line in the order below. Omit any section that does not apply to your configuration.

### 1. Seed engineering (mode = `cut` only)

| Line | Field | Values | Description |
|------|-------|--------|-------------|
| 1 | `cut_mode` | `slice` `sphere` `rhomb` `hemisphere` | Shape of the seed cut |
| 2+ | Shape parameters | — | See table below |

| `cut_mode` | Additional lines |
|---|---|
| `slice` | `cut_h`, `cut_k`, `cut_l`, `cut_shift` |
| `sphere` | `cut_radius_s` |
| `rhomb` | `cut_rhomb_size` |
| `hemisphere` | `cut_h`, `cut_k`, `cut_l`, `cut_radius_h` |

### 2. Screw dislocations (`screw_yes_no = yes`)

For each screw family of type `spray 25`, add `screwspreadx_N` and `screwspready_N`.  
For monoclinic space groups (3–15), add `unique_axis`.  
For rhombohedral space groups (146, 148, 155, 160, 161, 166, 167), add `hex_rhom`.

### 3. Surface growth (mode = `surface` only)

| Field | Description |
|-------|-------------|
| `surface_substrate` | Substrate material |
| `surface_thickness` | Substrate thickness |
| `surface_h`, `surface_k`, `surface_l` | Surface Miller indices |
| `surface_energy` | Surface energy |
| `surface_width` | Surface width |
| `surface_seed_x`, `surface_seed_y`, `surface_seed_z` | Seed position |

### 4. Molecular / net parameters (`crystal_type = net`, no checkpoint)

| Field | Description |
|-------|-------------|
| `molecules_grouped` | `yes` / `no` — group symmetry-equivalent molecules |
| `weighting_multiple_bonds` | `yes` / `no` — weight multiple bonds (new-format structure files only) |
| `grouped_coord_I_J` / `ungrouped_coord_I_J` | Coordination values per component and bond index (if `weighting_multiple_bonds = yes`) |

### 5. Tile / zeolite parameters (`crystal_type = tile`)

| Field | Description |
|-------|-------------|
| `qn_same` | `yes` / `no` — use the same Q values for all tiles |
| `q_var_J` | Q value for tile J (one per tile, if `qn_same = no`) |
| `scalings_same` | `yes` / `no` — use the same scaling for all tiles |
| `tile_var_J` | Scaling for tile J (one per tile, if `scalings_same = no`) |
| `baseline_scaling` | Baseline tile scaling factor |
| `ordered_penalty` | Ordering penalty (mode = `ordered` only) |

### 6. Box size (`calculate_memory = no` and no checkpoint)

Three lines: `x_length`, `y_length`, `z_length` (integers, in unit cells).

### 7. Supersaturation schedule (all modes except `nucleation`)

The fields included depend on `delmu_mode`:

| Mode | Additional fields |
|------|-------------------|
| `1` | `iterations_equilibration` |
| `2` | *(none)* |
| `3` | `iterations_equilibration`, `iterations_start` |
| `4` | `iterations_equilibration`, `new_del_mu`, `iterations_start`, `iterations_new_delmu` |
| `5` | `new_del_mu`, `iterations_start` |
| `6` | `iterations_equilibration`, `new_del_mu`, `iterations_start`, `iterations_new_delmu` |
| `7` | `new_del_mu`, `second_new_mu`, `iterations_start`, `iterations_new_delmu` |
| `8` | *(none)* |

If `excess_any = yes`, add for each excess component (except the last):
`excess_end_J`, then per-tile (`excess_tile_J_K`) or per-component (`excess_grouped_J_K` / `excess_ungrouped_J_K`) supersaturation values.

### 8. Growth modifier (mode = `growth_modifier` only)

One `poison_site_N` line per poison site, then `0` as a terminator, then `poison_attach` and `poison_remain`.

### 9. Screw stress (mode = `screw_stress` only)

`radius_stress`, `start_stress`, `length_stress`.

### 10. Nucleation (mode = `nucleation` only)

`nucleation_start_size`, `nucleation_end_size`, `nucleation_step_size`, `nucleation_num_sims`, `nucleation_start_delmu`, `nucleation_end_delmu`, `nucleation_step_delmu`.

### 11. Output grown crystal

`output_grown` (`yes` / `no`) — not used in `seed_engineering`, `nucleation`, `growth_modifier`, `surface`, or `screw_stress` modes.

### 12. Terrace visualisation (`tiles_represented = yes`)

`find_colour_zebra` (`find` / `colour`), then `max_hkl` (if `find`) or `crystal_size` (if `colour`).

### 13. Checkpoint box size (loading a checkpoint only)

`x_length`, `y_length`, `z_length` — appended after all other fields.

---

## Diffusion mode

In diffusion mode, `addinput.txt` contains only the box size (`x_length`, `y_length`, `z_length`) and `diffusion_seed_radius`. All other diffusion parameters go in a separate **`diffusion_input.txt`** file in the same working directory:

| Line | Field | Description |
|------|-------|-------------|
| 1 | `num_threads` | Number of parallel threads (`1` for serial) |
| 2 | `checkpoint_save` | `yes` / `no` |
| 3 | `checkpoint_yes_no` | `yes` / `no` |
| 4 | `checkpoint_path` | File path, or `none` |
| 5 | `bulk_concentration` | Bulk concentration (mol/dm³) |
| 6 | `lambda` | Lambda parameter (default `1`) |
| 7 | `diffusion_coeff` | Diffusion constant (m²/s) |
| 8 | `jump_distance` | Jump distance (Å) |
| 9 | `bulk_dissolution` | Bulk dissolution free energy (kcal/mol, relative to 1 mol/dm³) |
| 10 | `activation` | Free energy of activation (kcal/mol) |
| 11 | `solubility` | Solubility of crystal (mol/dm³) |
| 12 | `molar_volume` | Molar volume of crystal (dm³/mol) |
