import requests
import pandas as pd
import numpy as np

endpoint = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json"

def get_all_complain_types():
	endpoint = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$where=complaint_type IS NOT NULL"
	response = requests.get(endpoint)
	complaint_types = []
	for entry in response.json():
		complaint_types.append(entry['complaint_type'])
	return complaint_types

def get_entries_by_year(year):
	endpoint = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$where=created_date between "%s-01-01T00:00:00" and "%s-12-31T23:59:59"' % (year, year)
	response = requests.get(endpoint)
	return response.json()

if __name__ == "__main__":
	complaint_types = get_all_complain_types()
	ct_series = pd.Index(complaint_types)
	ct_dict = ct_series.value_counts()
	print(ct_dict)

	entries = get_entries_by_year(2017)
	e_df = pd.DataFrame(entries)
	print(e_df)
