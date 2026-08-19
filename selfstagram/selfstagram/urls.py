from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # This will require login due to @login_required
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('like/<int:image_id>/', views.toggle_like, name='toggle_like'),
    path('comment/<int:image_id>/', views.add_comment, name='add_comment'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('search/', views.search_users, name='search_users'),
    path('delete/image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('delete/comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
