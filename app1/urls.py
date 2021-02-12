from django.urls import path
from .views import stu_data,home,stu_del,stu_up

urlpatterns = [
    path('', home , name='home'),
    path('save/', stu_data, name='save'),
    path('delete/', stu_del , name='delete'),
    path('update/', stu_up , name='update'),
]