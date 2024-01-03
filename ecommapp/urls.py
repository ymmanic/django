from django.contrib import admin
from django.urls import path
from ecommapp import views
from ecommapp.views import SimpleView
from ecommapp.views import NewView
from ecommapp.views import OldView
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('contact',views.contact),
    path('login',views.login),
    path('home',views.home),
    path('edit/<rid>',views.edit),
    path('del1/<pid>',views.del1),
    path('myview',SimpleView.as_view()),
    path('hisview',NewView.as_view()),
    path('oldview',OldView.as_view()),
    path('index',views.newhome),
    path('page1',views.page2),
    path('page2',views.page1),
    path('newpath',views.oldpath),
    path('oldpath',views.newpath),
    path('hello',views.hello),
    path('city',views.city),
]