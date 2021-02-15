from requests import get
from json import dumps
from datetime import datetime
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#now = datetime.now()
#today4pm = now.replace



def getLatestByRegion(ENDPOINT, AREA_TYPE, DATE):


        filters = [
            f"areaType={ AREA_TYPE }",
            f"date={ DATE }",
            
        ]

        structure = {
            "areaName":"areaName",
            "date": "date",
            "newCases": "newCasesByPublishDate",
            "newDeaths": "newDeaths28DaysByPublishDate",
            "cumDeaths" : "cumDeaths28DaysByPublishDateRate"
     
            
        }

        api_params = {
            "filters": str.join(";", filters),
            "structure": dumps(structure, separators=(",", ":"))
        }


        response = get(ENDPOINT, params=api_params, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

        #print(response.url)
        #print(response.json())
        rawJ = response.json()
        df = pd.DataFrame(rawJ["data"])
       # print(df)
        return(df)

def getLatestByNation(ENDPOINT, AREA_TYPE, DATE):
        filters = [
            f"areaType={ AREA_TYPE }",
            f"date={ DATE }",
            
        ]

        structure = {

            "areaName":"areaName",
            "date": "date",
            "newCases": "newCasesByPublishDate",
            "cumulative": "cumCasesByPublishDate",
            "newDeaths": "newDeaths28DaysByPublishDate",
            "cumDeaths" : "cumDeaths28DaysByPublishDateRate"
     
            
        }

        api_params = {
            "filters": str.join(";", filters),
            "structure": dumps(structure, separators=(",", ":"))
        }


        response = get(ENDPOINT, params=api_params, timeout=10)

        if response.status_code >= 400:
            raise RuntimeError(f'Request failed: { response.text }')

       # print(response.url)
        #print(response.json())
        rawJ = response.json()
        df = pd.DataFrame(rawJ["data"])
       # print(df)
        return df

        

        
def latestGraphByRegion():
        ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
        AREA_TYPE = "region"
        #DATE = (datetime.datetime.today().strftime('%Y-%m-%d'))
        DATE = "2021-01-31"
        df = getLatestByRegion(ENDPOINT, AREA_TYPE, DATE)
        print(df)

       
        sns.barplot(data=df, x="areaName", y="newCases");
        plt.xlabel('')
        plt.ylabel('New cases')
        plt
        plt.title('Number of new cases recorded on {} in England by Region'.format(DATE))
        plt.xticks(size=9)
        sns.despine();
        plt.show()



        

        sns.barplot(data=df, x="areaName", y="newDeaths");
        plt.xlabel('')
        plt.ylabel('New Deaths')
        plt
        plt.title('Number of new deaths recorded on {} in England by Region'.format(DATE))
        plt.xticks(size=9)
        sns.despine();
        plt.show()



        

        

def latestGraphByNation():
        ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
        AREA_TYPE = "nation"
        #DATE = (datetime.datetime.today().strftime('%Y-%m-%d'))
        DATE = "2021-01-31"
        df = getLatestByNation(ENDPOINT, AREA_TYPE,DATE)

        
        print(df)

        sns.barplot(data=df, x="areaName", y="newCases");
        plt.xlabel('')
        plt.ylabel('New cases')
        plt
        plt.title('Number of new cases recorded on {} in the UK by nation'.format(DATE))
        plt.xticks(size=9)
        sns.despine();
        plt.show()

        areaName = df['areaName'].values.tolist()
        newCases = df['newCases'].values.tolist()
        print(areaName)
        print(newCases)
        
        

        sns.barplot(data=df, x="areaName", y="newDeaths");
        plt.xlabel('')
        plt.ylabel('New Deaths')
        plt
        plt.title('Number of new deaths recorded on {} in the UK by nation'.format(DATE))
        plt.xticks(size=9)
        sns.despine();
        plt.show()




        

latestGraphByRegion()
latestGraphByNation()



