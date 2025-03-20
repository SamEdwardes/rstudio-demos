import polars as pl

# Eager API --------------------------------------------------------------------

df = pl.read_csv("https://j.mp/iriscsv")
print(df)

(df.filter(pl.col("sepal_length") > 5).groupby("species").agg(pl.all().sum()))

# Lazy API ---------------------------------------------------------------------

(
    df.lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.all().sum())
    .collect()
)
