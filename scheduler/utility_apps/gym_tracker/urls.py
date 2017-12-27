from django.conf.urls import url
from .views import gym_home


urlpatterns = [
    url(r'^$', gym_home, name="gymhome" ),
    # url(r'^emotion-journal/$', add_emotion, name="add_emotion" ),
    # url(r'^get-all-emotions/$', get_all_emotions, name="get_all_emotions" ),
    # url(r'^change-status/(?P<id>[0-9]+)$', change_status, name="change_status" ),
]
