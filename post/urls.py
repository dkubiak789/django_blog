from django.conf.urls import patterns, include, url
# from article.views import ArticleDetailView
from post import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.PostListView.as_view(), name='posts'),
    url(r'^add/$', views.PostCreateView.as_view(), name='add_post'),
    url(r'^edit/(?P<pk>\d+)/$', views.PostEditView.as_view(), name='edit_post'),
    
    # url(r'^create/', views.PostCreate.as_view()),
    # url(r'^success/', views.Red.as_view(), name='red'),
    # url(r'^update/(?P<pk>\d+)/$', views.PostUpdate.as_view(), name='update'),
    # url(r'^detail/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/comment/(?P<post_pk>\d+)/$', views.CommentCreateView.as_view(), name='add_comment'),
)