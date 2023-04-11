from django.urls import path
from .views import CreateStudent, ListStudentView, UpdateStudentView, DeleteStudentView

urlpatterns = [
    path('create/', CreateStudent.as_view(), name='create_student_url'),
    path('list/', ListStudentView.as_view(), name='list_student_url'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update_student_url'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete_student_url'),
]