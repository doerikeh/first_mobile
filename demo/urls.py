from django.urls import path, include

from .views import BookViewSets
from rest_framework import routers

app_name = 'demo'
router = routers.DefaultRouter()
router.register('book', BookViewSets)

urlpatterns = [
    path('', include(router.urls)),
    
]
