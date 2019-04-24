from django.urls import path
from .views import FiltragemDetailView, FiltragemListView

urlpatterns = [
    path('', FiltragemListView.as_view(), name='filtragem_list'),
    path('detail/<int:pk>', FiltragemDetailView.as_view(), name='filtragem_detail'),
]
