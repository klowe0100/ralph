# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import redirect_to

from ralph.cmdb.views import Search as SearchCmdb

from ralph.ui.views import typeahead_roles, unlock_field, logout
from ralph.ui.views.common import Home, BulkEdit, ServerMove, ScanStatus, Scan
from ralph.ui.views.ventures import (
    ReportVenturesDeviceList,
    VenturesAddresses,
    VenturesAsset,
    VenturesComponents,
    VenturesCosts,
    VenturesHistory,
    VenturesInfo,
    VenturesPrices,
    VenturesReports,
    VenturesRoles,
    VenturesSoftware,
    VenturesVenture,
    VenturesScan,
)
from ralph.ui.views.racks import (
    RacksAddDevice,
    RacksAddresses,
    RacksAsset,
    RacksComponents,
    RacksCosts,
    RacksHistory,
    RacksInfo,
    RacksPrices,
    RacksRack,
    RacksReports,
    RacksSoftware,
    RacksScan,
    ReportRacksDeviceList,
)
from ralph.ui.views.search import (
    ReportSearchDeviceList,
    SearchAddresses,
    SearchAsset,
    SearchComponents,
    SearchCosts,
    SearchDeviceList,
    SearchHistory,
    SearchInfo,
    SearchPrices,
    SearchReports,
    SearchSoftware,
    SearchScan,
)
from ralph.ui.views.networks import (
    NetworksAddresses,
    NetworksAsset,
    NetworksComponents,
    NetworksCosts,
    NetworksDeviceList,
    NetworksHistory,
    NetworksInfo,
    NetworksPrices,
    NetworksReports,
    NetworksSoftware,
    ReportNetworksDeviceList,
    NetworksAutoscan,
    NetworksScan,
)
from ralph.ui.views.catalog import (
    Catalog,
    CatalogComponent,
    CatalogDevice,
    CatalogHistory,
    CatalogPricingGroup,
    CatalogPricingNew,
)
from ralph.ui.views.deploy import (
    Deployment,
    PrepareMassDeployment,
    MassDeployment,
)
from ralph.ui.views.ventures import VenturesDeviceList
from ralph.ui.views.racks import RacksDeviceList
from ralph.ui.views.reports import (
    ReportMargins,
    ReportServices,
    ReportVentures,
    ReportDevices,
    ReportDevicePricesPerVenture,
)


urlpatterns = patterns(
    '',
    url(r'^typeahead/roles/$', login_required(typeahead_roles),
        {}, 'typeahead-roles'),
    url(r'^unlock-field/$',
        login_required(unlock_field), {}, 'unlock-field'),
    url(r'^$', login_required(Home.as_view()), {}, 'home'),

    url(r'^(?P<section>\w+)/([^/]*/)?(?P<details>bulkedit)/$',
        login_required(BulkEdit.as_view()), {}, 'bulkedit'),
    url(r'^(?P<section>\w+)/([^/]*/)?(?P<details>deploy)/(?P<device>\d+)$',
        login_required(Deployment.as_view()), {}, 'deploy'),
    url(r'^(?P<section>\w+)/([^/]*/)?(?P<details>move)/$',
        login_required(ServerMove.as_view()), {}, 'servermove'),
    url(r'^logout/$', login_required(logout), {}, 'logout'),

    url(r'^search/$',
        login_required(SearchDeviceList.as_view()), {}, 'search'),
    url(r'^search/(?P<details>info)/(?P<device>\d+)$',
        login_required(SearchInfo.as_view()), {}, 'search'),
    url(r'^search/(?P<details>components)/(?P<device>\d+)$',
        login_required(SearchComponents.as_view()), {}, 'search'),
    url(r'^search/(?P<details>software)/(?P<device>\d+)$',
        login_required(SearchSoftware.as_view()), {}, 'search'),
    url(r'^search/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(SearchAddresses.as_view()), {}, 'search'),
    url(r'^search/(?P<details>prices)/(?P<device>\d+)$',
        login_required(SearchPrices.as_view()), {}, 'search'),
    url(r'^search/(?P<details>costs)/(?P<device>\d+)$',
        login_required(SearchCosts.as_view()), {}, 'search'),
    url(r'^search/(?P<details>history)/(?P<device>\d+)$',
        login_required(SearchHistory.as_view()), {}, 'search'),
    url(r'^search/(?P<details>asset)/(?P<device>\d+)$',
        login_required(SearchAsset.as_view()), {}, 'search'),
    url(r'^search/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportSearchDeviceList.as_view()), {'device': ''}, 'search'),
    url(r'^search/(?P<details>reports)/(?P<device>\d+)$',
        login_required(SearchReports.as_view()), {}, 'search'),
    url(r'^search/(?P<details>\w*)/(?P<device>)$',
        login_required(SearchDeviceList.as_view()), {}, 'search'),
    url(r'^search/(?P<details>cmdb)/(?P<device>\d+)$',
        login_required(SearchCmdb.as_view()), {}, 'search'),
    url(r'^search/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(SearchScan.as_view()), {}, 'search'),
    url(r'^ventures/$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>info|components|software|addresses|prices|costs|history|asset|discover|cmdb)/(?P<device>)$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>)(?P<details>info|components|software|addresses|prices|costs|history|asset|discover|cmdb)/(?P<device>)$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportVenturesDeviceList.as_view()), {'device': ''}, 'ventures'),
    url(r'^ventures/(?P<venture>)(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportVenturesDeviceList.as_view()), {'device': ''}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(VenturesInfo.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(VenturesComponents.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>software)/(?P<device>\d+)$',
        login_required(VenturesSoftware.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(VenturesAddresses.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>prices)/(?P<device>\d+)$',
        login_required(VenturesPrices.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>costs)/(?P<device>\d+)$',
        login_required(VenturesCosts.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(VenturesHistory.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(VenturesAsset.as_view()), {}, 'ventures'),

    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>reports)/(?P<device>\d+)$',
        login_required(VenturesReports.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>roles)/(?P<role>[-\w]*)$',
        login_required(VenturesRoles.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>venture)/(?P<device>)$',
        login_required(VenturesVenture.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(VenturesScan.as_view()), {}, 'ventures'),

    url(r'^racks/$',
        login_required(RacksDeviceList.as_view()), {}, 'racks'),
    url(r'^racks/-/rack/$', redirect_to,
        {'url': '/ui/racks/-/info/'}),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>add_device)/(?P<device>)$',
        login_required(RacksAddDevice.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>rack)/(?P<device>)$',
        login_required(RacksRack.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(RacksInfo.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(RacksComponents.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>software)/(?P<device>\d+)$',
        login_required(RacksSoftware.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(RacksAddresses.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>prices)/(?P<device>\d+)$',
        login_required(RacksPrices.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>costs)/(?P<device>\d+)$',
        login_required(RacksCosts.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(RacksHistory.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(RacksAsset.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportRacksDeviceList.as_view()), {'device': ''}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>reports)/(?P<device>\d+)$',
        login_required(RacksReports.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>\w+)/(?P<device>)$',
        login_required(RacksDeviceList.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(RacksScan.as_view()), {}, 'racks'),

    url(r'^networks/$',
        login_required(NetworksDeviceList.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>info)/$',
        login_required(NetworksInfo.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(NetworksComponents.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>software)/(?P<device>\d+)$',
        login_required(NetworksSoftware.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>addresses)/$',
        login_required(NetworksAddresses.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>prices)/(?P<device>\d+)$',
        login_required(NetworksPrices.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>costs)/(?P<device>\d+)$',
        login_required(NetworksCosts.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(NetworksHistory.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(NetworksAsset.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportNetworksDeviceList.as_view()), {'device': ''}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>reports)/(?P<device>\d+)$',
        login_required(NetworksReports.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>autoscan)/$',
        login_required(NetworksAutoscan.as_view()), {'status': 'new'}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>autoscan)/(?P<status>new|changed|dead|buried|all)/$',
        login_required(NetworksAutoscan.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(NetworksScan.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network>[^/]*)/(?P<details>\w+)/(?P<device>)$',
        login_required(NetworksDeviceList.as_view()), {}, 'networks'),

    url(r'^catalog/$',
        login_required(Catalog.as_view()), {}, 'catalog'),
    url(r'^catalog/history/$', login_required(CatalogHistory.as_view()), {},
        'catalog_history'),
    url(r'^catalog/(?P<kind>device)/(?P<type>\d*)/$',
        login_required(CatalogDevice.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>component)/(?P<type>\d*)/$',
        login_required(CatalogComponent.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>device)/(?P<type>\d*)/(?P<group>\d*)/$',
        login_required(CatalogDevice.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>component)/(?P<type>\d*)/(?P<group>\d*)/$',
        login_required(CatalogComponent.as_view()), {}, 'catalog'),
    url(r'^catalog/(?P<kind>pricing)/$',
        login_required(CatalogPricingNew.as_view()), {}, 'catalog_pricing'),
    url(r'^catalog/(?P<kind>pricing)/(?P<year>\d\d\d\d)-(?P<month>\d\d)/$',
        login_required(CatalogPricingNew.as_view()), {}, 'catalog_pricing'),
    url(r'^catalog/(?P<kind>pricing)/(?P<year>\d\d\d\d)-(?P<month>\d\d)/(?P<group>.*)/$',
        login_required(CatalogPricingGroup.as_view()), {}, 'catalog_pricing'),

    url(r'^reports/$', login_required(ReportVentures.as_view()),
        {}, 'reports'),
    url(r'^reports/services/$', login_required(ReportServices.as_view()),
        {}, 'reports_services'),
    url(r'^reports/ventures/$', login_required(ReportVentures.as_view()),
        {}, 'reports_ventures'),
    url(r'^reports/margins/$', login_required(ReportMargins.as_view()),
        {}, 'reports_margins'),
    url(r'^reports/devices/$', login_required(ReportDevices.as_view()),
        {}, 'reports_devices'),
    url(r'^reports/device_prices_per_venture/$',
        login_required(ReportDevicePricesPerVenture.as_view()), {}, 'device_prices_per_venture'),

    url(r'^deployment/mass/start/$',
        login_required(PrepareMassDeployment.as_view())),
    url(r'^deployment/mass/define/(?P<deployment>[0-9]+)/$',
        login_required(MassDeployment.as_view())),

    url(r'^scan/status/(?P<job_id>[a-z0-9-]+)/$',
        login_required(
            ScanStatus.as_view()), {}, 'scan_results',
        ),
    url(r'^scan/status/(?P<address>[0-9.]+)/$',
        login_required(
            ScanStatus.as_view()), {}, 'scan_results',
        ),
    url(r'^scan/.*', login_required(Scan.as_view()), {}, 'scan'),
    url(r'^scan/(?P<address>[0-9.]+)/$',
        login_required(Scan.as_view()), {}, 'scan'),


)
