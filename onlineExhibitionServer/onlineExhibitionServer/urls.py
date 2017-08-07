from django.conf.urls import include, url


from django.contrib import admin
from art.views import artist, artists, achievement, introduction, exhibit, exhibits
from art.views import exhibition, exhibitions, exhibit_readings,exhibition_readings,\
    exhibit_image_text_readings, exhibit_vedio_readings, exhibition_image_text_readings,\
    exhibition_vedio_readings, get_signature, motified_signature
from art.views import home_html, exhibition_html, exhibit_html, artist_html, exhibit_ratings, \
    image_text_readings_html, video_readings_html,attention

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
    url(r'^exhibit_ratings/(\d+)/$', exhibit_ratings),
    # url(r'^exhibit_image_ratings/(\d+)/$', exhibit_image_ratings),
    url(r'^exhibit_image_text_readings/(\d+)/$', exhibit_image_text_readings),
    url(r'^exhibit_vedio_readings/(\d+)/$', exhibit_vedio_readings),

    url(r'^achievement/$', achievement),
    url(r'^introduction/$', introduction),

    url(r'^exhibitions/(\d+)/$', exhibition),
    url(r'^exhibitions/$', exhibitions),
    url(r'^exhibition_readings/(\d+)/$', exhibition_readings),
    url(r'^exhibition_image_text_readings/(\d+)/$', exhibition_image_text_readings),
    url(r'^exhibition_vedio_readings/(\d+)/$', exhibition_vedio_readings),

    # url(r'^get_signature/$', get_signature),
    # url(r'^motified_signature/$', motified_signature),

    url(r'^attention/$', attention),

    url(r'^home_html/$', home_html),
    url(r'^exhibition_html/$', exhibition_html),
    url(r'^exhibit_html/$', exhibit_html),
    url(r'^artist_html/$', artist_html),
    url(r'^image_text_readings_html/$', image_text_readings_html),
    url(r'^video_readings_html/$', video_readings_html),

    # url(r'^server_manage/$', server_manage)
]
