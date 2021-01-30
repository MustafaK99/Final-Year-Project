from requests import get
from json import dumps
from datetime import datetime
import datetime
import pandas as pd
import matplotlib.pyplot as plt


ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "nation"
DATE = (datetime.datetime.today().strftime('%Y-%m-%d'))
AREA_NAME = "england"


#now = datetime.now()
#today4pm = now.replace



def latestByRegion(ENDPOINT, AREA_TYPE, DATE):


        filters = [
            f"areaType={ AREA_TYPE }",
            f"date={ DATE }",
            f"areaName={ AREA_NAME }"
        ]

        structure = {
            "areaName":"areaName",
            "date": "date",
            "newCases": "newCasesByPublishDate",
            "cumulative": "cumCasesByPublishDate",
            "newDeaths": "newDeaths28DaysByPublishDate",
            "newTestsByPublishDate": "newTestsByPublishDate"
     
            
        }

        api_params = {
            "filters": str.join(";", filters),
            "structure": dumps(structure, separators=(",", ":"))
        }


        response = get(ENDPOINT, params=api_params, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        print(response.url)
        #print(response.json())
        rawJ = response.json()
        df = pd.DataFrame(rawJ["data"])
        print(df)





        

        
  

latestByRegion(ENDPOINT, AREA_TYPE, DATE)
