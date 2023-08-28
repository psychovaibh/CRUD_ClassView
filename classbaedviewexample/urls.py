# from django.contrib import admin
# from django.urls import path
# from django.views.generic import TemplateView



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',TemplateView.as_view(template_name="index.html"),name="home")
# ]



from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.homePage,name="home"),
    path("",views.DisplayClassView.as_view(),name="home"),
    path("add/",views.EmployeePostClassView.as_view(),name="add"),
    path("delete/<int:id>/",views.EmployeeDeleteView.as_view(),name="delete"),
    path("update/<int:id>/",views.EmployeeUpdateView.as_view(),name="update"),
    path("search",views.EmployeeSearchView.as_view(),name="search"),
]
