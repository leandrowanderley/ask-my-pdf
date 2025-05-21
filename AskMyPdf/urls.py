from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importe a view 'index' diretamente do seu aplicativo 'myapp'
from myapp import views as myapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Serve a página inicial (index.html) na raiz do site
    path('', myapp_views.index, name='home'),
    # Inclui as URLs do seu aplicativo 'myapp' sob o prefixo '/api/'
    # Isso significa que 'ask-pdf/' do myapp/urls.py será acessível em '/api/ask-pdf/'
    path('api/', include('myapp.urls')),
]

# Apenas para desenvolvimento: servir arquivos estáticos e de mídia
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)