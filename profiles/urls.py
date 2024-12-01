from django.urls import path, include
from profiles import views

app_name='profiles'

urlpatterns = [
    path('<int:profile_id>/', views.profile_detail, name='profile'),
    path('filtered/', views.filter_profiles, name='filter_profiles'),
    path('directions/<int:direction_id>/', views.direction_detail, name='directions'),
    path('faculties/<int:faculty_id>/', views.faculty_detail, name='faculties'),
]
