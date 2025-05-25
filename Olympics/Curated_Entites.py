# Databricks notebook source
# MAGIC %md
# MAGIC ### DELTA LIVE TABLES - GOLD LAYER

# COMMAND ----------

# MAGIC %md
# MAGIC ### Coaches DELTA PIPELINE

# COMMAND ----------

import dlt
from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### Expectations for Data Quality

# COMMAND ----------

expec_coaches = {
                        "rule1" : "code is not null",
                        "rule2" : "current is True"
                }

# COMMAND ----------

expec_nocs = {
                        "rule1" : "code is not null",
            }

# COMMAND ----------

expec_events = {
                        "rule1" : "event is not null",
                }

# COMMAND ----------

@dlt.table

def source_coaches():

  df = spark.readStream.table("olympics.silver.coaches")
  return df

# COMMAND ----------

@dlt.view

def view_coaches():

  df = spark.readStream.table("LIVE.source_coaches")
  return df

# COMMAND ----------

@dlt.table

@dlt.expect_all(expec_coaches)
def coaches():

    df = spark.readStream.table("LIVE.view_coaches")
    return df

# COMMAND ----------

# MAGIC %md
# MAGIC ### NOCS DLT PIPELINE

# COMMAND ----------

@dlt.view

def source_nocs():

    df = spark.readStream.table("olympics.silver.nocs")

    return df

# COMMAND ----------

@dlt.table

@dlt.expect_all_or_drop(expec_nocs)
def nocs():

    df = spark.readStream.table("LIVE.source_nocs")

    return df

# COMMAND ----------

# MAGIC %md
# MAGIC ### EVENTS DLT PIPELINE

# COMMAND ----------

@dlt.view

def source_events():

    df = spark.readStream.table("olympics.silver.events")
    return df

# COMMAND ----------

@dlt.table

def events():

    df = spark.readStream.table("LIVE.source_events")

    return df