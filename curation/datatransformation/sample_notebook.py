# Databricks notebook source
# MAGIC %md
# MAGIC ## Sample Data Transformation Notebook
# MAGIC This notebook demonstrates a simple data transformation in Databricks.

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

# Display the original DataFrame
display(df)

# COMMAND ----------
# Add a new column 'C' which is the sum of columns 'A' and 'B'
df = df.withColumn('C', df['A'] + df['B'])

# Display the transformed DataFrame
display(df)

# COMMAND ----------
# Perform a simple aggregation to calculate the mean of column 'C'
mean_value = df.agg({'C': 'mean'}).collect()[0][0]

# Display the mean value
print(f"The mean value of column C is {mean_value}")
