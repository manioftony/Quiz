"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from masterdata.views import index,login_data,QuestionAnswerView, createuser,logout_request,question_answer
from rest_framework.authtoken.views import obtain_auth_token


# from django
urlpatterns = [
  #  url(r'^$',index),
    # url(r'^$',login_data),
    # url(r'^usercreation/$',createuser),
    url(r'^index/$',index),
    url(r'^question-answer/$', QuestionAnswerView.as_view(), name='question'),
    url(r'^api-token-auth/$', obtain_auth_token, name='api_token_auth'),
    url(r'^admin/', admin.site.urls),

    url(r'^logout/$',logout_request),


    url(r"^question_answer/$", question_answer, name="logout"),


]
