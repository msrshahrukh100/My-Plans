from django.conf.urls import url
from .views import home, change_status, history, AnalysisData, analysis, get_todays_score, time_bound_tasks


urlpatterns = [
    url(r'^$', home, name="home" ),
    url(r'^change-status/(?P<id>[0-9]+)$', change_status, name="change_status" ),
    url(r'^history/$', history, name="history"),
    url(r'^time-bound-tasks/$', time_bound_tasks, name="time_bound_tasks"),
    url(r'^your-analysis/$', analysis, name="analysis" ),
    url(r'^get-todays-score/$', get_todays_score, name="get_todays_score" ),

    url(r'^get-analysis-data/$', AnalysisData.as_view(), name="get_analysis_data"),

]
