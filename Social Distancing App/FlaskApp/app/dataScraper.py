from requests import get
from json import dumps
from datetime import datetime
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# now = datetime.now()
# today4pm = now.replace


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

    # print(response.url)
    # print(response.json())
    rawJ = response.json()
    df = pd.DataFrame(rawJ["data"])
    # print(df)
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

    # print(response.url)
    # print(response.json())
    rawJ = response.json()
    df = pd.DataFrame(rawJ["data"])
    # print(df)
    return df


def latestGraphByRegion():
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_TYPE = "region"
    # DATE = (datetime.datetime.today().strftime('%Y-%m-%d'))
    DATE = "2021-01-31"
    df = getLatestByRegion(ENDPOINT, AREA_TYPE, DATE)
    # print(df)

def latestGraphByNation():
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    AREA_TYPE = "nation"
    # DATE = (datetime.datetime.today().strftime('%Y-%m-%d'))
    DATE = "2021-03-11"
    df = getLatestByNation(ENDPOINT, AREA_TYPE, DATE)


    areaName = df['areaName'].values.tolist()
    newCases = df['newCases'].values.tolist()
    newDeaths = df['newDeaths'].values.tolist()
    cumulative = df['cumulative'].values.tolist()

    # print(df)


    return areaName, newCases, newDeaths, cumulative
