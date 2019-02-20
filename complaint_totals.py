from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
from sodapy import Socrata

directorytwo = '../../desktop/Zip_Code_ZCTA20190.xlsx' # data for zipcode

df = pd.read_excel(directorytwo)

mostPopularcodes = ['60629', '79936', '11368', '90650', '90011', '91331', '11226', '90201', '11373', '11220']

# use comparator for zipcodes and top complaints for 2017. needs to qualify based on 2017 and then they need to match off


totalpopulation = df['2010 Census Population'].sum()
