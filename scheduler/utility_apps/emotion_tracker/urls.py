from django.conf.urls import url
from .views import emotion, add_emotion, get_all_emotions


urlpatterns = [
    url(r'^$', emotion, name="emotion" ),
    url(r'^emotion-journal/$', add_emotion, name="add_emotion" ),
    url(r'^get-all-emotions/$', get_all_emotions, name="get_all_emotions" ),
    # url(r'^change-status/(?P<id>[0-9]+)$', change_status, name="change_status" ),
]
