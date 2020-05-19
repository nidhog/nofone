import pandas as pd

weekday_map = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}

is_weekend_map = {i: i > 4 for i in range(7)}

shift_time = lambda x: x - 24 + 1 if x >= 12 else x + 1


def get_detail_from_timestamp(timestamps_series):
    """Returns the Datetime, Days, Years, Months and Other detail series
    for a timestamp series

    :param timestamps_series: a numpy series or a dataframe column
    :return: datetimes, days, years, months, day_of_week, day_of_week_str, is_weekend:
    tuple of series

    """
    datetimes = pd.to_datetime(timestamps_series)
    days = datetimes.dt.day
    years = datetimes.dt.year
    months = datetimes.dt.month
    day_of_week = datetimes.dt.dayofweek
    day_of_week_str = day_of_week.map(weekday_map)
    is_weekend = day_of_week.map(is_weekend_map)

    return datetimes, days, years, months, day_of_week, day_of_week_str, is_weekend


def get_tz_from_timestamp(time_series, time_zone='UTC', get_hours=False, get_shifted=False):
    """Returns timestamp in specified timezone, UTC by default
    Shifted hours only returned if get hours

    :param time_series: 
    :param get_hours: 
    :param get_shifted: 
    :return: res: list where the first element is the utc time series, 
    second is hours, third shifted hours. These last two will not be 
    there if not specified
    """
    res = [time_series.apply(lambda x: pd.to_datetime(x).tz_convert(time_zone))]
    if get_hours:
        res.append(res[0].dt.hour)
        if get_shifted:
            res.append(res[1].map(shift_time))
    return res
