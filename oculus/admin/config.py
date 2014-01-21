from django.core.urlresolvers import reverse_lazy

APP_ADMIN_URLS = {
    'url_base': 'statistikk',
    'namespace': 'oculus',
}

APP_ADMIN_MENU = {
    'Statistikk': {
        'anchor': 'stats',
        'bgcolor': '#2EAC42',
        'icon': 'fa fa-eye icon',

        'menu': {
            'Oversikt': {
                'url': reverse_lazy('admin:oculus:index'),
                'icon': 'icon-th-list',
                'order': 0,
            },
        }
    }
}
