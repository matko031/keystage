from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name='register'),
    path('regstud/', views.register_student, name='register_student'),
    path('regcom/', views.register_company, name='register_company'),
    path('logout/', views.logout_request, name="logout"),
    path('login/', views.login_request, name='login'),
    path('account/', views.account, name='account'),
    path('account_edit/', views.account_edit, name='account_edit'),
    path('add_internship/', views.add_internship, name='account_edit'),
    path('internships/', views.internships, name='internships'),
    path('delete/internship/<internship_id>', views.delete_internship, name='delete_internship'),
    path('find_internship', views.find_internship, name='find_internship')
]
