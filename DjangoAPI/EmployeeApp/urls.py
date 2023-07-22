# ✅ new import (alias re_path as url)
from django.urls import re_path as url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^department/$", views.departmentApi),
    url(r"^department/([0-9]+)$", views.departmentApi),
    url(r"^employees/$", views.employeesApi),
    url(r"^employees/([0-9]+)$", views.employeesApi),
    url(r"^SaveFile", views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
