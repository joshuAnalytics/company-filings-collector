#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd
from pandas.io.json import json_normalize
import json
import math
import warnings
warnings.filterwarnings("ignore")
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--keyword',required=True, help='keyword to search for matching companies',
	)
args = parser.parse_args()

def get_results_df(keyword):
    apiKey = os.environ.get("CH_SECRET_KEY")
    url1 = "https://api.companieshouse.gov.uk/search/companies?q="
    url2 = "&items_per_page=100&start_index="
    #get the first page and number of total results
    index = 0
    url_full = url1+keyword+url2+str(index)
    re = requests.get(url_full, auth=(apiKey, '')).json()
    total_results = re['total_results']
    num_pages = math.ceil(total_results / 100)

    #loop through pages and append results to list
    results_list = []
    for page in range(1,11):
        url_full = url1+keyword+url2+str(index)
        re = requests.get(url_full, auth=(apiKey, '')).json()
        total_results = re['total_results']
        normalized_json = json_normalize(re['items'])
        results_list.append(normalized_json)
        index = page * 100
    results_df = pd.concat(results_list)
    return results_df

results_df = get_results_df(args.keyword)

results_filename = str(args.keyword).replace(' ','_')

results_df.to_csv(f'{results_filename}_results.csv',index=False)


