# Databricks notebook source
# MAGIC %md
# MAGIC ## Sample Notebook
# MAGIC This notebook creates a simple DataFrame and displays it.

# COMMAND ----------
import pandas as pd
import numpy as np

# Create a pandas DataFrame
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10)
}
pdf = pd.DataFrame(data)

# Convert to a Spark DataFrame
df = spark.createDataFrame(pdf)

# Display the DataFrame
display(df)
