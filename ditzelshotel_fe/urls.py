from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ditzelshotel_fe import settings
from hoteladmin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]
""" Index """
urlpatterns += [
    path("", overview, name="overview"),
    path("customer/<int:customer_id>/checkout/", customer_checkout, name="customer-checkout"),
    path("reservation/<int:reservation_id>/cancel/", reservation_cancel, name="reservation-cancel"),
    path("employee/<int:employee_id>/dismiss/", employee_dismiss, name="employee-dismiss"),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
