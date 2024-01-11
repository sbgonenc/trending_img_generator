#connect google trends api
from pytrends.request import TrendReq


def get_trending_terms(country):
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_searches_df = pytrends.trending_searches(pn=country)
    return list(trending_searches_df)

