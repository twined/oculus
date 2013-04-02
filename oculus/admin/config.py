from django.core.urlresolvers import reverse_lazy

APP_ADMIN_URLS = {
    'url_base': 'statistikk',
    'namespace': 'oculus',
}

APP_ADMIN_MENU = {
    'Statistikk': {
        'Oversikt': {
            'url': reverse_lazy('admin:oculus:index'),
            'icon': 'icon-th-list',
            'order': 0,
        },
    }
}
