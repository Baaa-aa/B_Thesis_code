# Graph Theoretical Descriptors For Chemical Property Predictions

This repository contains the code and data used for the thesis titled **"Graph Theoretical Descriptors For Chemical Property Predictions."**

## Project Overview

The project focuses on evaluating the predictive power of graph-based topological indices for chemical property prediction. It consists of two main parts:

1. **Boiling Point Prediction:**  
   Comparison of various topological indices as descriptors for predicting boiling points of alkanes and perfluoroalkanes.  
   
2. **Melting Point Prediction:**  
   Proposal and testing of a graph transformation approach aimed at predicting melting points of benzene-ring-based hydrocarbons.

## Code and Data Structure

The repository is organized into three main folders, each corresponding to a chemical family:

- `alkanes/`
- `perfluoroalkanes/`
- `benzene_ring_based_hydrocarbons/`

Each folder contains:

- `data/` — raw and processed datasets with data source references listed
- `code/` — Jupyter notebooks and scripts performing the analysis

All data required for running the analyses is included within the respective `data/` folders.

## Usage

- The analysis is implemented in Jupyter notebooks found in each `code/` folder.
- Dependencies are listed in the `environment.yml` file.  
  To create the conda environment, run:  
  ```bash
  conda env create -f environment.yml
  conda activate <env-name>
## Citation
If you use this code or data, please cite the following work:
```
@thesis{curdova2025topological_indices,
  author       = {Barbora Čurdová},
  title        = {Graph Theoretical Descriptors For Chemical Property Predictions},
  school       = {University of Chemistry and Technology, Prague, Faculty of Chemical Technology, Department of Informatics and Chemistry},
  year         = {2025},
  address      = {Prague},
  note         = {bachelor’s thesis},
  language     = {english},
  supervisor   = {Wim Dehaen, M.Sc., Ph.D.}
}
```
