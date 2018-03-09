from django.conf.urls import url
from .views import gym_home, change_days_delta


urlpatterns = [
    url(r'^$', gym_home, name="gymhome" ),
    url(r'^change-days-delta/(?P<action>[\w\-]+)/$', change_days_delta, name="change_days_delta"),
    # url(r'^emotion-journal/$', add_emotion, name="add_emotion" ),
    # url(r'^get-all-emotions/$', get_all_emotions, name="get_all_emotions" ),
    # url(r'^change-status/(?P<id>[0-9]+)$', change_status, name="change_status" ),
]
