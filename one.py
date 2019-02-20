import requests
import pandas as pd
import numpy as np
import csv
from datetime import datetime

###//// Moved to Top
# Index values of Borough


# complainers_index = pd.DataFrame( { ##should be population as denomator
#     'BRONX': 8699/308739931,
#     'BROOKLYN': 14437/308739931,
#     'MANHATTAN': 17/308739931,
#     'QUEENS': 7738/308739931,
#     'STATEN ISLAND': 2061/308739931
# })

Borough
BRONX            2.817582e-05
BROOKLYN         4.676104e-05
Borough          5.506252e-08
MANHATTAN        2.506317e-05
QUEENS           3.597850e-05
STATEN ISLAND    6.675521e-06
Unspecified      3.151520e-06
dtype: float64

#////

complaints_array = ['HEAT/HOT WATER', 'Noise - Residential', 'Illegal Parking', 'Blocked Driveway', 'Request Large Bulky Item Collection', 'PLUMBING', 'Missed Collection (All Materials)', 'UNSANITARY CONDITION', 'PAINT/PLASTER', 'Street Condition']
population = 308739931

# template... will destroy


input_file = pd.read_excel("../../downloads/tocopycitydata.xlsx")
# input_file
(input_file)
df = pd.DataFrame(
     {'Unique Key' : input_file["Unique Key"],
        'Created Date' : input_file["Created Date"],
        'Closed Date' : input_file["Closed Date"],
        'Complaint Type' : input_file["Complaint Type"],
        'Incident Zip' : input_file["Incident Zip"],
        'Status' : input_file["Status"],
        'Borough' : input_file["Borough"],
     })
df
df.groupby("Borough").size()/population
# Index
