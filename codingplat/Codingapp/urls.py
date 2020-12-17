
from django.urls import path
from . import views
app_name = "codingApp"
urlpatterns = [
    path('code/',views.CodeAPIview.as_view(),name='code')

]
