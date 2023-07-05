from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from clients.views import SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls', namespace="clients")),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/',  SignupView.as_view(), name='signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)