import pandas as pd
from .prep import weekday_map, shift_time, is_weekend_map

# Default path to cgm data CSV file
LOCAL_PATH_DEFAULT = 'data/cgm_latest.csv'

# CSV fields
LBL_GLUCOSE = 'Historic Glucose mmol/L'
LBL_DEVICE = 'Device'
LBL_SRL_NUM = 'Serial Number'
LBL_TIMSTMP = 'Device Timestamp'
LBL_NOTES = 'Notes'
LBL_RECTYPE = 'Record Type'

# Custom fields
_LBL_DATTIME = '_Datetime'
_LBL_DAY = '_Day'
_LBL_MONTH = '_Month'
_LBL_YEAR = '_Year'
_LBL_DAYWEEK = '_Day Of Week'
_LBL_WEEK = '_Week'
_LBL_HOUR = '_Hour'
_LBL_WEEKEND = '_Is Weekend'
_LBL_DAYWEEK_STR = '_Day of Week str'
_LBL_HOUR_SHIFT = '_Hour Shifted'

# Glucose main columns
main_cols = [LBL_GLUCOSE, LBL_DEVICE, LBL_SRL_NUM, LBL_TIMSTMP, LBL_RECTYPE]


def get_main_cols(df):
    return df[main_cols]


def get_glucose_data_local(storage_path=LOCAL_PATH_DEFAULT, prepared=False):
    """

    :param storage_path: string for glucose csv file
    :param prepared: boolean, defaults to False. 
    if true adds more columns for detail and only selects useful columns
    :return: dataframe with glucose data
    """
    df = get_main_cols(pd.read_csv(storage_path))
    if prepared:
        df = df[[LBL_TIMSTMP, LBL_GLUCOSE, LBL_DEVICE, LBL_SRL_NUM, LBL_RECTYPE, LBL_NOTES]]
        df[_LBL_DATTIME] = pd.to_datetime(df[LBL_TIMSTMP])
        df[_LBL_DAY] = df[_LBL_DATTIME].dt.day
        df[_LBL_YEAR] = df[_LBL_DATTIME].dt.year
        df[_LBL_MONTH] = df[_LBL_DATTIME].dt.month
        df[_LBL_DAYWEEK] = df[_LBL_DATTIME].dt.dayofweek
        df[_LBL_WEEK] = df[_LBL_DATTIME].dt.week
        df[_LBL_HOUR] = df[_LBL_DATTIME].dt.hour

        df[_LBL_DAYWEEK_STR] = df[_LBL_DAYWEEK].map(weekday_map)
        df[_LBL_WEEKEND] = df[_LBL_DAYWEEK].map(is_weekend_map)

        df[_LBL_HOUR_SHIFT] = df[_LBL_HOUR].map(shift_time)
    return df
