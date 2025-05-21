from django.urls import path
from . import views

urlpatterns = [
    # Define a URL para o endpoint da API que o frontend chamará
    # Agora, esta URL será acessível em /api/ask-pdf/
    path('ask-pdf/', views.ask_pdf_view, name='ask_pdf'),
]
