#
#    Copyright 2019 Google LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
from googleapiclient import sample_tools
from googleapiclient.http import build_http
import sys
import json
import pandas as pd
discovery_doc = "gmb_discovery.json"
SCOPES = [
    "https://www.googleapis.com/auth/business.manage",#this code we are using this one
    "https://www.googleapis.com/auth/bigquery",
    "https://www.googleapis.com/auth/cloud-language"
]
def main(argv):
    print("____argv____")
    print(argv)

    # Use the discovery doc to build a service that we can use to make
    # MyBusiness API calls, and authenticate the user so we can access their
    # account
    service, flags = sample_tools.init(argv, 'mybusiness', 'v4', __doc__, __file__, scope=SCOPES , discovery_filename=discovery_doc)
    print('_____flags______')
    print(flags)
    # Get the list of accounts the authenticated user has access to
    ## STEP 1 - Get the List of all accounts for the authenticated user
    # GMB API call -- Method:accounts.list

    output = service.accounts().list().execute()
    print("List of GMB Accounts: \n\n")
    print(json.dumps(output, indent=2) + "\n")
    # extract the account name which will be used for further API calls
    #GMB may have serverl account each account may have several locations
    gmb_Account = output["accounts"]
    ## STEP 2 - Get the list of all available locations for the specified account (gmbAccount)

    # Limitation - 100 locations fetched per API Call //this is very important

    # we use 'pageToken' - to fetch all the available locations ///we can here get All the locations for all the accounts

    for gmbAccount in gmb_Account:
        print("____accounts__")
        print(gmbAccount)
        try:
            page_token = None
            # Defining empty dataframe and columns names where extracted info will be stored
            loc_df = pd.DataFrame()
            column_names = ['locationId']
            while True:
                print("Fetching list of locations for account test new new " + gmbAccount['name'], "\n\n")
                # GMB API Call - Method:accounts.locations.list
                loclist = service.accounts().locations().list(parent=gmbAccount['name'],pageToken=page_token).execute()
                print(json.dumps(loclist, indent=2))
                # Extracting only the necessary information from the response and append it to dataframe
                for i in loclist['locations']:
                    name = i['name']
                    loc_df = loc_df.append(pd.Series([name]),ignore_index=True)

                # Checking for the 'nextPageToken' in the response
                # if not available then break the loop
                page_token = loclist.get('nextPageToken')
                if not page_token:
                    break

        finally:
            print("All locations fetched for the account")
            print("Next Page Token"+str(page_token))
            loc_df.columns = column_names

        for account_id in loc_df['locationId']:
            body = {
                "locationNames": [
                    account_id
                ],
               "basicRequest": {
                "metricRequests": [
                  {
                  "metric": "ALL"
                  },

               ],
               "timeRange": {
                   "startTime": "2020-10-12T01:01:23.045123456Z",
                   "endTime": "2021-04-21T23:59:59.045123456Z"
                  }
              }
            }
            print("____body_____")
            print(body)

            # GMB API Call - Method:accounts.locations.reportInsights
            invet = service.accounts().locations().reportInsights(name=gmbAccount['name'],body=body).execute()
            print("____reportInsights_______")
            if(len(invet) == 1):

             print(json.dumps(invet['locationMetrics'][0]['metricValues'], indent=2))
            else:
             print('does not have data')



if __name__ == "__main__":
        main(sys.argv)
