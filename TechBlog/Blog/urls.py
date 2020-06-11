from django.conf.urls import url
from Blog import views

urlpatterns=[
url(r'^about/$',views.AboutView.as_view(),name="about"),
url(r'^$',views.PostListView.as_view(),name="post_list"),
url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="post_detail"),
url(r'^post/new/$',views.PostCreateView.as_view(),name="post_create"),
url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name="post_update"),
url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name="post_delete"),
url(r'^draft/$',views.PostDraftListView.as_view(),name="post_draft"),
url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name="add_comment_to_post"),
url(r'^post/(?P<pk>\d+)/approve/$',views.comment_approve,name="approve"),
url(r'^post/(?P<pk>\d+)/remove/$',views.comment_remove,name="remove"),
url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name="post_publish"),


]
