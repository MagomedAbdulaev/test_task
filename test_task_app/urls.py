from django.urls import path
from .views import *

app_name = 'test_task_app'


urlpatterns = [
    path('', home, name='home'),
    path('login_user/', login_user, name='login_user'),
    path('client_status_fetch/', client_status_fetch),
    path('logout/', logout_user, name='logout'),
]
