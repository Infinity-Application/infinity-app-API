from django.urls import path
from .views import CryptoList, CryptoDetail

urlpatterns = [
    path("", CryptoList.as_view(), name="crypto_list"),
    path("<int:pk>/", CryptoDetail.as_view(), name="crypto_detail"),
]
