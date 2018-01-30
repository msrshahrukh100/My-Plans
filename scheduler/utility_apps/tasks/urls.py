from django.conf.urls import url
from .views import (daily_tasks, 
	change_status, 
	history, 
	AnalysisData, 
	analysis, 
	get_todays_score, 
	time_bound_tasks,
	change_tbt_status,
    change_tbt_subtask_done)


urlpatterns = [
    url(r'^daily-tasks/$', daily_tasks, name="daily_tasks" ),
    url(r'^change-status/(?P<id>[0-9]+)$', change_status, name="change_status" ),
    url(r'^history/$', history, name="history"),
    url(r'^time-bound-tasks/$', time_bound_tasks, name="time_bound_tasks"),
    url(r'^your-analysis/$', analysis, name="analysis" ),
    url(r'^get-todays-score/$', get_todays_score, name="get_todays_score" ),
   	url(r'^change-tbt-status/(?P<id>[0-9]+)/(?P<action>[\w\-]+)/$', change_tbt_status, name="change_tbt_status" ),
    url(r'^change-tbt-subtask-done/(?P<id>[0-9]+)/$', change_tbt_subtask_done, name="change_tbt_subtask_done" ),
    url(r'^get-analysis-data/$', AnalysisData.as_view(), name="get_analysis_data"),

]
