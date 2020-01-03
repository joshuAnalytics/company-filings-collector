# company-filings-collector
retrieving data from company filings APIs


### `companies_house_searcher.py`

A python script for retrieving data from the Companies House API

A valid Companies House API key is required. This is loaded as an environmental variable in conda, as per [these instructions](https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0). 

The script can be run from the terminal as follows: 

`$python companies_house_searcher.py --keyword "company name search"`

This will return a csv file with data on all the companies matched via the keyword search, as per the [documentation here](https://developer.companieshouse.gov.uk/api/docs/search/companies/companysearch.html).

### next steps:

* add geolocation lookup
* add folium map displaying locations