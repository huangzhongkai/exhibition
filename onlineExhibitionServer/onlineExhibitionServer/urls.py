from django.conf.urls import include, url


from django.contrib import admin
from art.views import artist, artists, achievement, introduction, exhibit, exhibits
from art.views import exhibition, exhibitions, exhibit_readings,exhibition_readings,image_text_readings,vedio_readings
from art.views import home_html, exhibition_html, production_html, artist_html

admin.autodiscover()

urlpatterns = [
# Examples:
    # url(r'^$', 'onlineExhibitionServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^artists/(\d+)/$', artist),
    url(r'^artists/$', artists),

    url(r'^exhibits/(\d+)/$', exhibit),
    url(r'^exhibits/$', exhibits),

    url(r'^exhibit_readings/(\d+)/$', exhibit_readings),

    url(r'^achievement/$', achievement),
    url(r'^introduction/$', introduction),

    url(r'^exhibitions/(\d+)/$', exhibition),
    url(r'^exhibitions/$', exhibitions),

    url(r'^exhibition_readings/(\d+)/$', exhibition_readings),

    url(r'^image_text_readings/(\d+)/$', image_text_readings),
    url(r'^vedio_readings/(\d+)/$', vedio_readings),

    # url(r'^attention/$', attention),

    url(r'^home_html/$', home_html),
    url(r'^exhibition_html/$', exhibition_html),
    url(r'^production_html/$', production_html),
    url(r'^artist_html/$', artist_html),

    # url(r'^server_manage/$', server_manage)
]
