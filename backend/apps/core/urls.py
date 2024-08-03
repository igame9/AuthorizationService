from django.urls import include, path
from .views import set_csrf
from apps.accounts import urls as accounts_urls


urlpatterns = [
    path("api/csrf/", set_csrf, name="csrf"),
    path("api/accounts/", include(accounts_urls)),
]
