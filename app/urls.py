from django.urls import path

from app import views

app_name: str = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('update_students_name/<int:pk>/', views.update_student_name, name='update_students_name'),
    path('update_students_grades/<int:pk>/', views.update_student_grade, name='update_students_grades'),
    path('update_grade/<int:pk>/', views.update_grade, name='update_grade'),
    path('delete_grade/<int:pk>/', views.delete_grade, name='delete_grade'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
]
