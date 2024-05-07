# Introduction
This script calculates the areal quantum capacitance and the charge storage of a material based on the given energy distribution and density of states.

## Authors
- Maryam Masoudi
- Fatemeh Shirvani
- Aliasghar Shokri
- M.S. Akhoundi Khezrabad

## Date
- Year: 2024
- Month: May
## DOI:
10.5281/zenodo.11130644
# Instructions
1. Run the script.
2. Enter the paths to the E.txt and dos.txt files which contain the energy of density states and density of states, respectively.
3. Enter the value of the surface of the structure in which the lattice constants should be considered in Angstrom. For example, for a cubic structure if a and b are 10 Angstrom then you should put 100 when the code asks you for the value of the surface. 

# Requirements
- Python 3.x
- NumPy
- pandas

# Usage
1. Clone the repository: `git clone https://github.com/FatemehShirvani1986/areal-quantum-capacitance-charge-storage.git`
2. Navigate to the directory: `cd areal-quantum-capacitance-charge-storage`
3. Run the script: `python areal quantum capacitance-charge storage.py`

# Input Files
- **E.txt**: File containing the energy density of states.
- **dos.txt**: File containing the density of states.

# Output Files
- **V.txt**: Electric potential.
- **CQ.txt**: areal quantum capacitance.
- **q.txt**:  areal charge storage.

# Notes
- Ensure that the input files are correctly formatted and accessible.
