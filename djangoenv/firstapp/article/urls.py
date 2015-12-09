from django.conf.urls import include, url

urlpatterns = [
    url(r'^1/', article.views.basic_one),
]