from django.urls import path

from honda.views import *

urlpatterns = [
    path('honda/', Honda125.as_view()),
    path('group/<int:pk>/', GroupLavazem.as_view()),
    path('lavazem/<int:pk>/', Lavazem125.as_view())

]
