"""
URL configuration for mail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('',views.loginUser,name="loginUser"),
    path('compose/',views.compose,name="compose"),
    path('newUser/',views.newUser,name="newUser"),
    
    path('sentmails/',views.list_sent_emails,name="sentmails"),
    path('inbox/',views.get_inbox_emails,name="inbox"),
    path('trash/',views.view_trash,name="trash"),
    # path('drafts/',views.get_draft_emails,name="get_draft_emails"),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('success/', views.success_page, name='success_page'),
    path('drafts/', views.drafts, name='drafts'),  # Define the URL pattern for success_page
    path('stared/', views.stared, name='stared'),
    path('delete_trash/<int:record_id>/', views.delete_record_trash, name='delete_record_trash'),
    path('starred_message/<int:record_id>/', views.starred_message, name='starred_message'),
    path('success_starred/', views.success_page_starred, name='success_page_starred'),
    path('starred_trash/<int:record_id>/', views.starred_trash, name='starred_trash'),
    path('remove_draft/<int:record_id>/',views.remove_draft,name="remove_draft"),

]
