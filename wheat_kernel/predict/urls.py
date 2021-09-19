from django.conf.urls import url
from .views import predict_kernel

urlpatterns = [
    url('', predict_kernel)
]