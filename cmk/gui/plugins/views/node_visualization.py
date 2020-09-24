#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from . import multisite_builtin_views

multisite_builtin_views.update({
    'topology_filters': {
        'browser_reload': 30,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description':
            _('Configures the number of available filters in the network topology view.'),
        'group_painters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'hidden': True,
        'hide_filters': [],
        'layout': 'table',
        'mustsearch': False,
        'name': 'allhosts',
        'num_columns': 3,
        'owner': '',
        'painters': [('host_state', None)],
        'play_sounds': False,
        'public': True,
        'show_filters': [
            'hoststate',
            'hostalias',
            'siteopt',
            'hostregex',
            'hostgroups',
            'host_labels',
            'opthost_contactgroup',
            'host_tags',
        ],
        'sorters': [],
        'title': _('Topology filters'),
        'topic': _('Topology'),
    },
    'bi_map_hover_host': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _("Host hover menu shown in BI visualization"),
        'hidden': True,
        'hidebutton': True,
        'hide_filters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'show_filters': [],
        'group_painters': [],
        'icon': None,
        'layout': 'dataset',
        'linktitle': u'Hover Host',
        'mobile': False,
        'mustsearch': False,
        'name': 'bi_map_hover_host',
        'num_columns': 1,
        'owner': '',
        'painters': [(('host', {
            'color_choices': []
        }), 'hoststatus', None), ('host_state', None, None), ('host_plugin_output', None, None)],
        'play_sounds': False,
        'public': True,
        'single_infos': ['host'],
        'sorters': [],
        'title': _('BI host details'),
    },
    'bi_map_hover_service': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'services',
        'description': _("Service hover menu shown in BI visualization"),
        'hidden': True,
        'hidebutton': True,
        'hide_filters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'show_filters': [],
        'group_painters': [],
        'icon': None,
        'layout': 'dataset',
        'linktitle': u'Hover service',
        'mobile': False,
        'mustsearch': False,
        'name': 'bi_map_hover_service',
        'num_columns': 1,
        'painters': [(('host', {
            'color_choices': []
        }), 'hoststatus', None), ('service_description', 'service', None),
                     ('service_state', None, None), ('host_check_age', None, None),
                     ('svc_acknowledged', None, None), ('svc_in_downtime', None, None)],
        'play_sounds': False,
        'public': True,
        'single_infos': ['service', 'host'],
        'sorters': [],
        'title': _("BI service details"),
    },
    'topology_hover_host': {
        'browser_reload': 0,
        'column_headers': 'pergroup',
        'datasource': 'hosts',
        'description': _("Host hover menu shown in topolgoy visualization"),
        'hidden': True,
        'hidebutton': True,
        'hide_filters': [],
        'hard_filters': [],
        'hard_filtervars': [],
        'show_filters': [],
        'group_painters': [],
        'icon': None,
        'layout': 'dataset',
        'linktitle': u'Hover Host',
        'mobile': False,
        'mustsearch': False,
        'name': 'topology_hover_host',
        'num_columns': 1,
        'owner': '',
        'painters': [(('host', {
            'color_choices': []
        }), 'hoststatus', None), ('host_state', None, None), ('host_plugin_output', None, None),
                     ("host_parents", None, None), ("host_childs", None, None)],
        'play_sounds': False,
        'public': True,
        'single_infos': ['host'],
        'sorters': [],
        'title': _('Toplogy host details'),
    },
})
