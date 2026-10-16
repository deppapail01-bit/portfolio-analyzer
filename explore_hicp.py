import pandas as pd

URL = (
    "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/"
    "prc_hicp_minr/M.I15.TOTAL.EL"
    "?format=SDMX-CSV&startPeriod=2015-01"
)

hicp = pd.read_csv(URL)

print(len(hicp))
print(hicp[["TIME_PERIOD", "OBS_VALUE"]].head(3))
print(hicp[["TIME_PERIOD", "OBS_VALUE"]].tail(3))