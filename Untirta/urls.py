from django.contrib import admin
from django.urls import path

from .views import Untirta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', Untirta ),
    path('blog/', Untirta ),
    path('faperta/', Untirta ),
    path('feb/', Untirta ),
    path('fh/', Untirta ),
    path('fisip/', Untirta ),
    path('fk/', Untirta ),
    path('fkip/', Untirta ),
    path('ft/', Untirta ),
    path('home/', Untirta ),
    path('pascasarjana/', Untirta ),
    path('static/', Untirta),
    
    
    
]
