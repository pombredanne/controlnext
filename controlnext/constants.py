# Separate file for constants used in the controlnext app,
# so they are easily editable.
# Keep this separate from Django's settings file,
# because this code might need to be reused in a FEWS general adapter.
import datetime
import pytz

jdbc_source_slug = 'controlnext'

rain_filter_id = 'neerslag_combo'    # Neerslag gecombimeerd
rain_location_id = 'OPP1'            # Oranjebinnenpolder Oost
rain_parameter_ids = {
    'min': 'P.min',   # Minimum
    'mean': 'P.gem',  # Gemiddeld
    'max': 'P.max'    # Maximum
}

fill_filter_id = 'waterstand_basins' # Waterstanden
fill_location_id = '467446797569'    # Van der Lans-west, niveau1
fill_parameter_id = 'WNS2820'        # Waterdiepte (cm)

frequency = datetime.timedelta(minutes=15)

min_berging_pct = 20
max_berging_pct = 100
max_berging_m3 = 15527 # in m^3
opp_invloed_regen_m2 = 94000 # in m^2
max_uitstroom_per_tijdstap_m3 = 4.5 # in m^3
bovenkant_bak_cm = 265 # in cm
hoogte_niveaumeter_cm = 265 # in cm

def round_date(date):
    minutes = date.minute - (date.minute % 15)
    return date.replace(minute=minutes, second=0, microsecond=0)

def validate_date(date):
    if date.tzinfo != pytz.utc:
        raise ValueError('can not deal with non-UTC (or timezone-naive) datetime objects')
    if date.second or date.microsecond or date.minute % 15 != 0:
        raise ValueError('please round dates to full quarter hours')

fill_history = datetime.timedelta(days=31)
fill_predict_future = datetime.timedelta(days=5)

fewsjdbc_cache_seconds = 15 * 60

def mktim(year, month, day, hour, minute_quarter):
    if minute_quarter % 15 != 0:
        raise ValueError('not rounded to a quarter hour')
    return datetime.datetime(year, month, day, hour, minute_quarter, tzinfo=pytz.utc)
