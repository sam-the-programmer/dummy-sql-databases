# %%
import sqlite3 as sq
from random import randint

import numpy as np
import pandas as pd

# %%
raw = pd.read_csv("CSV/user.txt")
raw

# %%

with open("CSV/names.txt") as file:
    names = file.read().splitlines()

# %%

new_df =  pd.DataFrame(
    np.array([
        names,
        raw.phone.values.tolist(),
        [randint(18, 60) for _ in range(10000)]
    ]).T,
    columns=["names", "phone", "age"]
)
# %%

raw.to_sql("userbase", sq.connect("userbase.db"))
new_df.to_sql("names", sq.connect("userbase.db"))
