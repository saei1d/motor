from django.urls import path

from honda.views import *

urlpatterns = [
    path('honda/', Honda125.as_view()),
    path('group/', GroupLavazem.as_view()),
    path('lavazem/', Lavazem125.as_view())

]
