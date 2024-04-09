from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('',views.loginUser,name="loginUser"),
    path('login/',views.loginUser,name="loginUser"),
    path('login/',views.login,name="login"),
    path('compose/',views.compose,name="compose"),
    path('newUser/',views.newUser,name="newUser"),
    path('logout/',views.logout,name="logout"),
    path('sentmails/',views.list_sent_emails,name="sentmails"),
    path('inbox/',views.get_inbox_emails,name="inbox"),
    path('trash/',views.view_trash,name="trash"),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('success/', views.success_page, name='success_page'),
    path('drafts/', views.drafts, name='drafts'),
    path('stared/', views.stared, name='stared'),
    path('delete_trash/<int:record_id>/', views.delete_record_trash, name='delete_record_trash'),
    path('starred_message/<int:record_id>/', views.starred_message, name='starred_message'),
    path('success_starred/', views.success_page_starred, name='success_page_starred'),
    path('starred_trash/<int:record_id>/', views.starred_trash, name='starred_trash'),
    path('remove_draft/<int:record_id>/',views.remove_draft,name="remove_draft"),
]
