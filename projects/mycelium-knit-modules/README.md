# Mycelium Knit Modules

This repository contains the source code for the knitted formworks used in the "16 Cubits" mycelium shelter project.

## Structure

*   **`module_A/`**: The standard structural unit.
*   **`module_B/`**: Corner unit for wall turning.
*   **`module_C/`**: Cap unit for top finishing.

Each directory contains:
*   `.knitout` file: Low-level machine instructions for Shima Seiki machines.
*   `.dat` file: Geometry data used for visualization and simulation.

## Usage

These patterns were generated using a custom parametric pipeline. To knit them:
1.  Load the `.knitout` file into your knitting machine software.
2.  Adjust carrier settings and tensions for your specific yarn.
3.  Process via the standard Knitout backend.
