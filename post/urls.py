from django.urls import path

from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_info/<int:post_id>', views.post_info, name='post_info'),
    path('post_info/<int:post_id>/post_add', views.add_comment, name='add_comment'),
    path('post_info/<int:post_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('add_post', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]