from django.urls import path
from . import views

app_name = 'Portafolio'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('contact/', views.contact_send_mail, name='send-mail'),
]
