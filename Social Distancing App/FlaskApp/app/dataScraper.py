from requests import get
from json import dumps
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pytz





def getLatestByRegion(ENDPOINT, AREA_TYPE, DATE):
    filters = [
        f"areaType={AREA_TYPE}",
        f"date={DATE}",

    ]

    structure = {
        "areaName": "areaName",
        "date": "date",
        "newCases": "newCasesByPublishDate",
        "newDeaths": "newDeaths28DaysByPublishDate",
        "cumDeaths": "cumDeaths28DaysByPublishDateRate"

    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }

    response = get(ENDPOINT, params=api_params, timeout=25)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')


    rawJ = response.json()
    df = pd.DataFrame(rawJ["data"])
    return (df)


def getLatestByNation(ENDPOINT, AREA_TYPE, DATE):
    filters = [
        f"areaType={AREA_TYPE}",
        f"date={DATE}",

    ]

    structure = {

        "areaName": "areaName",
        "date": "date",
        "newCases": "newCasesByPublishDate",
        "cumulative": "cumCasesByPublishDate",
        "newDeaths": "newDeaths28DaysByPublishDate",
        "cumDeaths": "cumDeaths28DaysByPublishDateRate"

    }

    api_params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }

    response = get(ENDPOINT, params=api_params)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')


    rawJ = response.json()
    df = pd.DataFrame(rawJ["data"])
    return df


def latestGraphByRegion():
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_TYPE = "region"
    Now = (datetime.now(pytz.timezone('Europe/London')))
    currentNow = Now.strftime("%H:%M:%S")
    #if (currentNow >= "16:00:00"):
      #  DATE = (datetime.today().strftime('%Y-%m-%d'))
    #else:
    DATE = datetime.now() - timedelta(days=1)
    DATE = DATE.strftime('%Y-%m-%d')

    df = getLatestByRegion(ENDPOINT, AREA_TYPE, DATE)
    areaName = df['areaName'].values.tolist()
    newCases = df['newCases'].values.tolist()
    newDeaths = df['newDeaths'].values.tolist()
    cumulative = df['cumDeaths'].values.tolist()

    return areaName, newCases, newDeaths, cumulative



def latestGraphByNation():
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_TYPE = "nation"

    Now = (datetime.now(pytz.timezone('Europe/London')))
    currentNow = Now.strftime("%H:%M:%S")
    #if(currentNow >= "16:00:00"):
       # DATE = (datetime.today().strftime('%Y-%m-%d'))
    #else:
    DATE = datetime.now() - timedelta(days=1)
    DATE = DATE.strftime('%Y-%m-%d')
    df = getLatestByNation(ENDPOINT, AREA_TYPE, DATE)


    areaName = df['areaName'].values.tolist()
    newCases = df['newCases'].values.tolist()
    newDeaths = df['newDeaths'].values.tolist()
    cumulative = df['cumulative'].values.tolist()


    return areaName, newCases, newDeaths, cumulative
