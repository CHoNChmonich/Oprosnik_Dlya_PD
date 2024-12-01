from django.urls import path, include
from questions import views

app_name='questions'

urlpatterns = [
    path('<int:question_id>/', views.test_view, name='test'),
    path('result/<int:direction_id>/', views.result_view, name='result'),
]
