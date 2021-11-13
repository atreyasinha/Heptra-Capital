from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from .forms import LoginForm

urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('dashboard/<int:pk>', views.Dashboard.as_view(), name='dashboard'),
    path('administrator/', views.Admin.as_view(), name='administrator'),
    path('accounts/login/', auth.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth.LogoutView.as_view(next_page='home'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)