from django.urls import path
from .views import ProductRuList, ProductUzList


urlpatterns = [
    path('ru/list', ProductRuList.as_view()),
    path('uz/list', ProductUzList.as_view()),
]