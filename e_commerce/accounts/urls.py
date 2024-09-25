from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile_view,signup
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path("", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("profile/", profile_view, name="profile"),
    path("signup/", signup, name="signup"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)