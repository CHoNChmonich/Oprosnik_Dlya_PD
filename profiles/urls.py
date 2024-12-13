from django.urls import path, include
from profiles import views

app_name='profiles'

urlpatterns = [
    path('<int:profile_id>/', views.profile_detail, name='profile'),
    path('profiles_list', views.profiles_list, name='profiles_list'),
    path('filtered/', views.filter_profiles, name='filter_profiles'),
    path('directions/<int:direction_id>/', views.direction_detail, name='directions'),
    path('faculties/', views.faculties_list, name='faculties_list'),
    path('faculties/<int:faculty_id>/', views.faculty_detail, name='faculties'),
]
