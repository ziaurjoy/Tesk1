from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('user/post/list/<user_name>', views.user_filtering_post, name='user-filtering-post'),
    path('category/post/list/<category_name>', views.category_filtering_post, name='caregory-filtering-post'),
    path('post/details/<int:pk>', views.post_details, name='post-details'),
]