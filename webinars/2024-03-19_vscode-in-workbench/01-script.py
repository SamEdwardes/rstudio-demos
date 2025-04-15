# You can run this python file by:
#
# (1) Using the play button in the top right. Press the dropdown for more options
# (2) Run `python 01-running-python-file.py` in the terminal
# (3) Use `shift+enter` to run in the interactive window. You can run a single
#     line, or highlight multiple lines to run more than one line.
# (4) Use `# %%` to run a section of the file

import pandas as pd

url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
df = pd.read_csv(url)

print(f"This dataframe has {df.shape[0]} rows.")
df

## %%
print("You can run everything in this chunk with `shift+enter`")
df[["island", "species"]]
