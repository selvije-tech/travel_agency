
from django.contrib import admin
from django.urls import path, include
from tours.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tours/', include('tours.urls', namespace='tours')),
    path('', LandingPageView.as_view(),name='landing-page' ),
]
