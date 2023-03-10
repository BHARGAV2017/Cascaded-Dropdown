
from django.contrib import admin
from django.urls import path
from ddapp.views import dependantfield
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dependantfield, name = 'dependantfield')
    # path('', )
]
