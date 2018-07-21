from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailForm.as_view(), name='post-detail'),
    path('post/vote/', views.PostVote.as_view(), name='post-vote'),
    # url(r'^snippets/$', views.snippet_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
