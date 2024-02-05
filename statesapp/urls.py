from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('states/', StateListView.as_view(), name='state-list'),
    path('states/<int:pk>/', StateDetailView.as_view(), name='state-detail'),
    path('states/create/', StateCreateView.as_view(), name='state-create'),
    path('states/update/<int:pk>/', StateUpdateView.as_view(), name='state-update'),
    path('states/delete/<int:pk>/', StateDeleteView.as_view(), name='state-delete'),
]
