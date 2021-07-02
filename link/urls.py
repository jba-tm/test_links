from django.urls import path

from .views import LinkView, LinkCheckView

app_name = 'link'
urlpatterns = [
    path('', LinkView.as_view(), name='index'),
    path('link-check/', LinkCheckView.as_view(), name='link-check')
]
