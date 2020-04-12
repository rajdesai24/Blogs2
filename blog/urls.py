from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView
urlpatterns = [
 path('', BlogListView.as_view(), name='home'),
 path('post/new/', BlogCreateView.as_view(),name='create'),
 path('post/<int:pk>/', BlogDetailView.as_view(),name='detail'),
 path('post/<int:pk>/edit/',BlogUpdateView.as_view(),name='edit'),
 path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='delete')
]