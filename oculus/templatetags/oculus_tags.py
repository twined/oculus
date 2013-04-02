import datetime

from django import template

from oculus.utils import (
    get_browserdata, get_referals, get_keywords,
    get_search_engines, get_top_content, get_pageviews,
    get_pageviews_per_day
)

register = template.Library()


@register.inclusion_tag(
    'oculus/admin/templatetags/get_stats.html',
    takes_context=True)
def get_stats(context):
    """
    Renders latest posts overview
    """
    return {
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/popular_posts.html',
    takes_context=True)
def browsers(context):
    """
    Renders latest posts overview
    """

    data = get_browserdata()

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/popular_posts.html',
    takes_context=True)
def popular_posts(context):
    """
    Renders latest posts overview
    """
    data = get_top_content(10)

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/referals.html',
    takes_context=True)
def referals(context):
    """
    Renders latest posts overview
    """
    data = get_referals(25)

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/top_content.html',
    takes_context=True)
def top_content(context):
    """
    Renders latest posts overview
    """

    data = get_top_content(10)

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/search_engines.html',
    takes_context=True)
def search_engines(context):
    """
    Renders latest posts overview
    """

    data = get_search_engines()

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/keywords.html',
    takes_context=True)
def keywords(context):
    """
    Renders latest posts overview
    """

    data = get_keywords(10)

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/pageviews.html',
    takes_context=True)
def pageviews(context):
    """
    Renders latest posts overview
    """

    data = get_pageviews()

    return {
        'data': data,
    }


@register.inclusion_tag(
    'oculus/admin/templatetags/hits_this_week.html',
    takes_context=True)
def hits_this_week(context):
    """
    Renders latest posts overview
    """
    date_to = datetime.datetime.now().strftime('%Y-%m-%d')
    date_from = (datetime.datetime.now() -
                 datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    data = get_pageviews_per_day(date_from, date_to)

    labels = data.keys()
    labels = [datetime.datetime.strptime(l, '%Y%m%d').strftime('%d/%m')
              for l in labels]

    values = data.values()
    pageviews = [int(v['pageviews']) for v in values]
    visits = [int(v['visits']) for v in values]

    max_pv = max(pageviews)
    max_v = max(visits)
    max_value = max_pv if max_pv > max_v else max_v
    steps = max_value / 50
    steps = steps if steps > 3 else 4

    return {
        'labels': labels,
        'data': values,
        'pageviews': pageviews,
        'visits': visits,
        'steps': steps,
    }
