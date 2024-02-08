"""Module containing models representing lightcurves.

   For now only for loading datasets which is a cvs file.
"""

import pandas as pd

def load_dataset(filename):
    """Load a table from CSV file.
    
    :param filename: The name of the .csv file to load.
    :raises Eror: when the file is not CSV/
                  no file was given as an inut/
                  the file or directory was not found
    :returns: pd.DataFrame with the data from the file.
    """
    return pd.read_csv(filename)
