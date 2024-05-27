# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
]