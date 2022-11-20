from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from ditzelshotel_fe import settings
from hoteladmin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]
""" Index """
urlpatterns += [
    path("", overview, name="home"),
    path("list/customer/", customer_list, name="customer-list"),
    path("list/employee/", employee_list, name="employee-list"),
    path("list/reservation/", reservation_list, name="reservation-list"),
    path("list/room/", room_list, name="room-list"),
    path("customer/<int:customer_id>/checkout/", customer_checkout, name="customer-checkout"),
    path("reservation/<int:reservation_id>/cancel/", reservation_cancel, name="reservation-cancel"),
    path("employee/<int:employee_id>/dismiss/", employee_dismiss, name="employee-dismiss"),
]
""" Authentication """
urlpatterns += [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
