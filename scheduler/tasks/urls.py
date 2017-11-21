from django.conf.urls import url
from .views import home, change_status, history, AnalysisData, analysis

urlpatterns = [
    url(r'^$', home, name="home" ),
    url(r'^change-status/(?P<id>[0-9]+)$', change_status, name="change_status" ),
    url(r'^history/$', history, name="history" ),
    url(r'^your-analysis/$', analysis, name="analysis" ),

    url(r'^get-analysis-data/$', AnalysisData.as_view(), name="get_analysis_data"),

]
