# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_transformations.ipynb.

# %% auto 0
__all__ = ['cols', 'load_data', 'is_half_bath']

# %% ../nbs/00_transformations.ipynb 2
from typing import Optional
from hamilton.function_modifiers import tag, extract_columns
import pandas as pd

# %% ../nbs/00_transformations.ipynb 4
cols = ['id', 'url', 'region', 'region_url', 'price', 'type', 'sqfeet', 'beds',
       'baths', 'cats_allowed', 'dogs_allowed', 'smoking_allowed',
       'wheelchair_access', 'electric_vehicle_charge', 'comes_furnished',
       'laundry_options', 'parking_options', 'image_url', 'description', 'lat',
       'long', 'state']
@extract_columns(*cols)
def load_data(path: str, nrows: Optional[int] = None) -> pd.DataFrame:
    df = pd.read_csv(path, nrows=nrows)
    return df

# %% ../nbs/00_transformations.ipynb 5
def is_half_bath(baths: pd.Series) -> pd.Series:
    """A boolean that indicates whether there is a half bath"""
    return baths.apply(lambda x: (x - int(x)) == 0.5)
