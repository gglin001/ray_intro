import ray
import ray.data

# https://docs.ray.io/en/latest/data/getting-started.html
ray.init()

# Create a dataset
# dataset = ray.data.read_csv("s3://anonymous@air-example-data/iris.csv")
dataset = ray.data.read_csv("/repos/Github/ray/ray_intro/air-sample-data/iris.csv")

print(type(dataset))
dataset.show(limit=1)

# %%
# Transform the dataset
import pandas as pd


# Find rows with spepal length < 5.5 and petal length > 3.5.
def transform_batch(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["sepal length (cm)"] < 5.5) & (df["petal length (cm)"] > 3.5)]


transformed_dataset = dataset.map_batches(transform_batch)
print(transformed_dataset)

# %%
# Consume the dataset
batches = transformed_dataset.iter_batches(batch_size=8)
print(next(iter(batches)))

# %%
# Save the dataset

import os

transformed_dataset.write_parquet("iris")

print(os.listdir("iris"))
