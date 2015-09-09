import os
import json
import matplotlib
# Get data
path = os.path.join("usagov_bitly_data2012-03-16-1331923249.txt")
records = [json.loads(line) for line in open(path)]
# Sample output
# List of dictionaries
'''
{u'a': u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11', u'c': u'US', u'nk': 1, u'tz': u'America/New_York', u'gr': u'MA', u'g': u'A6qOVH', u'h': u'wfLQtf', u'cy': u'Danvers', u'l': u'orofrog', u'al': u'en-US,en;q=0.8', u'hh': u'1.usa.gov', u'r': u'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf', u'u': u'http://www.ncbi.nlm.nih.gov/pubmed/22415991', u't': 1331923247, u'hc': 1331822918, u'll': [42.576698, -70.954903]}
'''
# Get time_zones column
# time_zones = [rec['tz'] for rec in records] results in error due to incomplete
# The following will check if tz a key in the row
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

from pandas import DataFrame, Series
import pandas as pd
# Create dataframe of records
# Tabular 2-by-2 spreadsheet table
frame = DataFrame(records)
# Get histogram (counts) easily
tz_counts = frame['tz'].value_counts()
# Check output 
# print tz_counts[:10]
# Data Munging (Clean the data)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
# Check output
# print clean_tz.value_counts()[:10]
# Getting a plot
import matplotlib.pyplot as plt 
tz_counts[:10].plot(kind='barh', rot=0)
# show all plots
# plt.show()

# PARSING DATA
# Example of data below 
# u'GoogleMaps/RochesterNY'
# u'Mozilla/5.0 (Windows NT 5.1; rv:10.0.2) Gecko/20100101 Firefox/10.0.2'
# u'Mozilla/5.0 (Linux; U; Android 2.2.2; en-us; LG-P925/V10e Build/FRG83G) AppleWebKit/533.1 (KHTML,
# nan
# frame.a --> accesses key a of dataframe
# .dropna() --> ignores values where nan
# .split() --> results in a list of the values split by whitespaces
results = Series([x.split()[0] for x in frame.a.dropna()])
# print results[:10]
print results.value_counts()[:8]