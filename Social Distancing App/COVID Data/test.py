from requests import get
import pandas as pd
from datetime import datetime




def get_data(url):
    response = get(endpoint, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':

    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation 
        'structure={"areaName":"areaName","date":"date","newCases":"newCasesByPublishDate"}'
    )
    
    data = get_data(endpoint)

    df = pd.DataFrame(data["data"])
    print(df.head())


    
    for p in data['data']:
        print('area: ' + p['areaName'])
        print('date: ' + p['date'])
        print('New Cases: ' + str(p['newCases']))


    areaNames = df['areaName'].values.tolist()
    print(areaNames)
    newCases = df('newCases'].values.tolist()
    print(newCases)


    
    #print(data)
