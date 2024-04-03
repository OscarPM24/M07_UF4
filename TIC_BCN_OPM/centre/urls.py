from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),

    path('teachers/teacher/<int:pk>/', views.teacher, name='teacher'),
    path('students/student/<int:pk>/', views.student, name='student'),

    path('form/', views.user_form, name='form'),
    path('update_user/<int:pk>', views.update_user, name='update_user'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
]