from django.contrib import admin
from django.urls import path
from pollapp.views import home,create,poll,question,addpoll,addquestion,view,result,ans,viewans
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("create/",create,name="create"),
    path("poll/",poll,name="poll"),
    path("question/",question,name="question"),
    path("addpoll/",addpoll,name="addpoll"),
    path("addquestion/",addquestion,name="addquestion"),
    path("view/<int:i>",view,name="view"),
    path("result/<int:i>",result,name="result"),
    path("ans/",ans,name="ans"),
    path("viewans/",viewans,name="viewans"),

]
