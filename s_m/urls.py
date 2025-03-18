from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user_view', views.user_view, name='user'),
    path('home', views.home_view, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('delete/<int:id>', views.delete_media, name='delete'),
    path('delete', views.delete_user, name='confirm_delete'),
    path('searched', views.search_bar, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


