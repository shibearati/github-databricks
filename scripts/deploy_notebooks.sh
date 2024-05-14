#!/bin/bash

# Define variables
DATABRICKS_WORKSPACE_DIR="/Workspace/latest"
LOCAL_NOTEBOOK_DIR="./notebooks"

# Import notebooks to Databricks workspace
databricks workspace import_dir $LOCAL_NOTEBOOK_DIR $DATABRICKS_WORKSPACE_DIR --overwrite
