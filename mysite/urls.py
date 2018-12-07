from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import HomeView  # 추가!!!

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),  # 추가!!!
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^notice/', include('notice.urls', namespace='notice')),
    # notice.urls를 적용하고, 이름공간을 'notice'로 지정
]