from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('acervo/', include('acervo.urls')),  
    
   
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from acervo.views import UserRegistrationView 

urlpatterns = [
    path('admin/', admin.site.admin_site if hasattr(admin, 'admin_site') else admin.site.urls),
    path('acervo/', include('acervo.urls')), 
    
    
    path('api/cadastro/', UserRegistrationView.as_view(), name='usuario_cadastro'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]