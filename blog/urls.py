from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('group/', views.BlogGroupListView.as_view(), name='group_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    #path('createpost/', views.PostCreateView.as_view(), name='create_post'),
    path('createpost/', views.post_create_view, name='create_post'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('creategroup/', views.BlogGroupCreateView.as_view(), name='create_group'),
    path('group/<int:pk>/', views.BlogGroupDetailView.as_view(), name='group_detail'),

]

