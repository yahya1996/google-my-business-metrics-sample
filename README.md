#  GMB Metrics (total search views , maps dirctection , etc...) with Python

Before you use Google My Business API, you need to register your application and obtain OAuth 2.0 credentials. For details on how to get started with Google My Business API, complete the following prerequisites:
After completing the prerequisites, you can enable the Google My Business API, request an OAuth 2.0 Client ID; then you can start using your API.
# OAuth 2.0 Credentials and Discovery Document
After the OAuth 2.0 client ID is created download the JSON and copy this file to the directory that contains your Python script and rename this file “client_secrets.json”.

Next, download the “Discovery Document” (https://developers.google.com/my-business/samples/#discovery_document) and save the file as “gmb_discovery.json” in the same directory as your Python script and client credentials. You use the discovery document is conjunctions with Google API Discovery Service.
### Client Library Installation
Next, we will need to install some Google API Client libraries for Python to work with Google’s API.

-Google API Python Client — “pip install google-api-python-client”
-OAuth Client Library — “pip install OAuth2client”
-Google BigQuery Python Client — “pip install google-cloud-bigquery”


# Additional Library (note i use this in my code)
As we will be working on large amounts of data, we need an additional library that is a fast, powerful, flexible and easy to use data analysis and manipulation tool. Yes, I am talking about “pandas”. We will install pandas and be using Dataframes for data manipulation.
-“pip install pandas”
