# CSV Merge Utility

## Overview
The `csv_utils.py` module provides a function to merge, reorganize, and clean CSV files.

## Function: mesclar_reorganizar_limpar

### Description
Merges two CSV files, reorganizes the data, and performs cleanup operations.

### Parameters
- `caminho_arq1` (str): Path to the first CSV file
- `caminho_arq2` (str): Path to the second CSV file  
- `caminho_saida` (str): Path for the output CSV file
- `coluna_id` (str): Name of the ID column to sort by

### Usage Example

```python
from csv_utils import mesclar_reorganizar_limpar

# Merge and clean two CSV files (relative paths)
mesclar_reorganizar_limpar(
    "arq1.csv", 
    "arq2.csv", 
    "saida.csv", 
    "CD_LCTO_CONTABIL"
)

# Windows paths - use raw strings (r"") or double backslashes
mesclar_reorganizar_limpar(
    r"C:\Users\Documents\arq1.csv", 
    r"C:\Users\Documents\arq2.csv", 
    r"C:\Users\Documents\saida.csv", 
    "CD_LCTO_CONTABIL"
)

# Or with double backslashes
mesclar_reorganizar_limpar(
    "C:\\Users\\Documents\\arq1.csv", 
    "C:\\Users\\Documents\\arq2.csv", 
    "C:\\Users\\Documents\\saida.csv", 
    "CD_LCTO_CONTABIL"
)
```

### What it does
1. Reads both CSV files
2. Removes the first data row from each file (after header row)
3. Standardizes columns between files
4. Merges files vertically (concatenation)
5. Sorts by the specified ID column
6. Removes the first row and first column from the final result
7. Saves the cleaned output

### Requirements
- pandas==2.2.2 (added to requirements.txt)
