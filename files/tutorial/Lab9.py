#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-10-14

@author: Yongjun Zhang

Use Google BigQuery to extract protest events from GDELT Project

"""

# Before running the following code, you need to set up a service account and download credentials
# Following the tutorial to set up your service account:
# https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries
# once you download your json file, open your terminal and run this:
# export GOOGLE_APPLICATION_CREDENTIALS="/Your path to/client_secrets.json"

import os
# replace the path to your PATH
os.chdir("/users/joshzyj/google drive/gdelt/")

# You need to install google.cloud.bigquery first
# pip install google.cloud.bigquery

from google.cloud import bigquery

client = bigquery.Client()

#####################################
# The following codes query events_partitioned table and save a protest table
# Note that we have not yet saved a table into local.
# We remotely access bigquery and save a table into bigquery

# Here is the webpage for gdelt v2
# https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/
# It provdes some explanations about the database
# Here is the codebook:
# http://data.gdeltproject.org/documentation/GDELT-Event_Codebook-V2.0.pdf
# Here is the codebook for GKG:
# http://data.gdeltprojec.org/documentation/GDELT-Global_Knowledge_Graph_Codebook-V2.1.pdf

# Define the query syntax.
# Note Year is the event year.
# Event root code 14 indicates protests
QUERY1 = ("""
    SELECT
        GLOBALEVENTID,
        EventCode,
        EventBaseCode,
        Actor1CountryCode,
        Actor2CountryCode,
        MonthYear,
        Year,
        AvgTone,
        GoldsteinScale,
        NumMentions,
        NumArticles
    FROM
        `gdelt-bq.gdeltv2.events_partitioned`
    WHERE
        Actor1CountryCode IS NOT NULL
        AND YEAR<=2020
        AND YEAR>=2014
        AND EventRootCode="14"
    """
    )
    
# TODO(developer): Set table_id to the ID of the destination table.
# PLS replace the "integral-nimbus-160315" with "Your own project id"
# also create a database "gdelt" to store our tables...
table_id_1 = "integral-nimbus-160315.gdelt.protest"
job_config_1 = bigquery.QueryJobConfig(destination=table_id_1)
# Perform the query
query_job_1 = client.query(QUERY1,job_config=job_config_1)  # API request
query_job_1.result()  # Waits for query to finish
print("Query results loaded to the table {}".format(table_id_1))
# So now we have a table sitting in our own big query. if you use your own browser to log into your google cloud, you should be able to see a table named protest under gdelt project...

##########################

# We need to export tables by logging into google cloud service
# save them to your storage
# and then download CSVs
