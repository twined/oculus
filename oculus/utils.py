import datetime
from collections import OrderedDict

from django.conf import settings

import gdata.analytics.client
from gdata.sample_util import CLIENT_LOGIN, SettingsUtil


gdata_client = gdata.analytics.client.AnalyticsClient(
    source=settings.GOOGLE_ANALYTICS_APP_NAME
)


def _login():
    settings_util = SettingsUtil(prefs={
        "email": settings.GOOGLE_ANALYTICS_LOGIN,
        "password": settings.GOOGLE_ANALYTICS_PASSWORD,
    })
    settings_util.authorize_client(
        gdata_client,
        service=gdata_client.auth_service,
        auth_type=CLIENT_LOGIN,
        source=settings.GOOGLE_ANALYTICS_APP_NAME,
        scopes=['https://www.google.com/analytics/feeds/']
    )


def get_views(year, week):
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2010-10-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:customVarValue3,ga:customVarValue4,ga:week',
        'metrics': 'ga:pageviews',
        'filters': 'ga:customVarValue4==Job,ga:customVarValue4==Profile;ga:week==%s;ga:year==%s' % (str(week), str(year)),
        'max-results': "10000"
    })

    return gdata_client.GetDataFeed(data_query)


def get_browserdata():
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:operatingSystem,ga:browser,ga:browserVersion',
        'metrics': 'ga:visits',
        'sort': '-ga:visits',
        'max-results': "10000",
    })
    xml = gdata_client.GetDataFeed(data_query)

    browser_visits = OrderedDict()
    for entry in xml.entry:
        browser = entry.get_object('ga:browser').value
        browser_version = entry.get_object('ga:browserVersion').value
        os = entry.get_object('ga:operatingSystem').value
        visits = entry.get_object('ga:visits').value

        if not os in browser_visits:
            browser_visits[os] = OrderedDict()
            browser_visits[os][browser] = OrderedDict()
            browser_visits[os][browser][browser_version] = visits
        else:
            if not browser in browser_visits[os]:
                browser_visits[os][browser] = OrderedDict()
                browser_visits[os][browser][browser_version] = visits

            else:
                if not browser_version in browser_visits[os][browser]:
                    browser_visits[os][browser][browser_version] = visits
                else:
                    browser_visits[os][browser][browser_version] += visits

    return browser_visits


def get_referals(count=15):
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:source,ga:referralPath',
        'metrics': 'ga:pageviews,ga:timeOnSite,ga:exits',
        'filters': 'ga:medium==referral',
        'sort': '-ga:pageviews',
        'max-results': str(count),
    })
    xml = gdata_client.GetDataFeed(data_query)

    referals = OrderedDict()

    for entry in xml.entry:
        source = entry.get_object('ga:source').value
        path = entry.get_object('ga:referralPath').value
        pageviews = entry.get_object('ga:pageviews').value
        time_on_site = entry.get_object('ga:timeOnSite').value
        exits = entry.get_object('ga:exits').value

        referals[source] = OrderedDict(
            pageviews=pageviews,
            time_on_site=str(datetime.timedelta(seconds=float(time_on_site))),
            exits=exits,
            path=path
        )

    return referals


def get_search_engines():
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:source',
        'metrics': 'ga:pageviews,ga:timeOnSite,ga:exits',
        'filters': 'ga:medium==cpa,ga:medium==cpc,ga:medium==cpm,ga:medium==cpp,ga:medium==cpv,ga:medium==organic,ga:medium==ppc',
        'sort': '-ga:pageviews',
        'max-results': "20",
    })
    xml = gdata_client.GetDataFeed(data_query)

    search_engines = OrderedDict()

    for entry in xml.entry:
        source = entry.get_object('ga:source').value
        pageviews = entry.get_object('ga:pageviews').value
        time_on_site = entry.get_object('ga:timeOnSite').value
        exits = entry.get_object('ga:exits').value

        search_engines[source] = OrderedDict(
            pageviews=pageviews,
            time_on_site=time_on_site,
            exits=exits
        )
    return search_engines


def get_keywords(count=5):
    """
    20 most popular get_keywords
    """
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:keyword',
        'metrics': 'ga:visits',
        'sort': '-ga:visits',
        'max-results': str(count),
    })
    xml = gdata_client.GetDataFeed(data_query)

    keywords = OrderedDict()

    for entry in xml.entry:
        keyword = entry.get_object('ga:keyword').value
        visits = entry.get_object('ga:visits').value

        keywords[keyword] = visits

    return keywords


def get_top_content(count=5):
    """
    20 most popular get_keywords
    """
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:pagePath',
        'metrics': 'ga:pageviews,ga:uniquePageviews,ga:timeOnPage,ga:bounces,ga:entrances,ga:exits',
        'sort': '-ga:pageviews',
        'max-results': str(count),
    })
    xml = gdata_client.GetDataFeed(data_query)

    data = OrderedDict()

    for entry in xml.entry:
        pagepath = entry.get_object('ga:pagePath').value
        pageviews = entry.get_object('ga:pageviews').value
        unique_pageviews = entry.get_object('ga:uniquePageviews').value
        time_on_page = entry.get_object('ga:timeOnPage').value
        bounces = entry.get_object('ga:bounces').value
        entrances = entry.get_object('ga:entrances').value
        exits = entry.get_object('ga:exits').value

        data[pagepath] = OrderedDict(
            pageviews=pageviews,
            unique_pageviews=unique_pageviews,
            time_on_page=time_on_page,
            bounces=bounces,
            entrances=entrances,
            exits=exits
        )

    return data


def get_pageviews():
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'metrics': 'ga:visits,ga:pageviews',
        'max-results': "10",
    })
    xml = gdata_client.GetDataFeed(data_query)

    data = {}
    for entry in xml.entry:
        data['pageviews'] = entry.get_object('ga:pageviews').value
        data['visits'] = entry.get_object('ga:visits').value

    return data


def get_pageviews_per_day(start, end):
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': str(start),
        'end-date': str(end),
        'dimensions': 'ga:date',
        'metrics': 'ga:visits,ga:pageviews',
        'max-results': "33",
        'sort': 'ga:date',
    })
    xml = gdata_client.GetDataFeed(data_query)

    data = OrderedDict()
    for entry in xml.entry:
        date = entry.get_object('ga:date').value
        data[date] = OrderedDict(
            pageviews=entry.get_object('ga:pageviews').value,
            visits=entry.get_object('ga:visits').value,
        )

    return data


def get_country_visits():
    _login()
    data_query = gdata.analytics.client.DataFeedQuery({
        'ids': settings.GOOGLE_ANALYTICS_TABLE_ID,
        'start-date': '2005-01-01',
        'end-date': '2100-01-01',
        'dimensions': 'ga:country',
        'metrics': 'ga:visits',
        'sort': '-ga:visits',
        'max-results': "10000",
    })
    xml = gdata_client.GetDataFeed(data_query)

    country_visits = {}
    for entry in xml.entry:
        country = entry.get_object('ga:country').value
        visits = entry.get_object('ga:visits').value
        if country in country_visits:
            country_visits[country] += visits
        else:
            country_visits[country] = visits

    return country_visits
