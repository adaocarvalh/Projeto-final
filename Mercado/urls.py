from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.mercado, name = "mercado"),
     path('produto/<int:id>',views.produto, name="produto"),
     path('cadastro/',views.produto, name="produto"),
     path('accounts/',include('accounts.urls')),
     path('accounts/',include('django.contrib.auth.urls')),
     path('remove/<int:id>',views.remove, name="remove"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)