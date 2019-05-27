from django.urls import path
from .views import ProfileDetailView,ProfileListView


profiles_patterns=([
    path('<username>/',ProfileDetailView.as_view(),name="detail"),
    path('',ProfileListView.as_view(),name="list"),
], "profiles")