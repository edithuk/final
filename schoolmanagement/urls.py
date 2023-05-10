
from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('teacherclick', views.teacherclick_view),
    path('studentclick', views.studentclick_view),
    path('frenchiseclick', views.frenchiseclick_view),


    path('adminsignup', views.admin_signup_view),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('teachersignup', views.teacher_signup_view),
    path('frenchisesignup', views.frenchise_signup_view),
    path('adminlogin', LoginView.as_view(template_name='school/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='school/studentlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='school/teacherlogin.html')),
    path('frenchiselogin', LoginView.as_view(template_name='school/frenchiselogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='school/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view,name='admin-add-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view,name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view,name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>', views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),
    path('admin-view-teacher-salary', views.admin_view_teacher_salary_view,name='admin-view-teacher-salary'),

    path('admin-frenchise', views.admin_frenchise_view,name='admin-frenchise'),
    path('admin-view-frenchise', views.admin_view_frenchise_view,name='admin-view-frenchise'),
    path('admin-add-frenchise', views.admin_add_frenchise_view,name='admin-add-frenchise'),
    path('admin-approve-frenchise', views.admin_approve_frenchise_view,name='admin-approve-frenchise'),
    path('approve-frenchise/<int:pk>', views.approve_frenchise_view,name='approve-frenchise'),
    path('delete-frenchise/<int:pk>', views.delete_frenchise_view,name='delete-frenchise'),
    path('delete-frenchise-from-school/<int:pk>', views.delete_frenchise_from_school_view,name='delete-frenchise-from-school'),
    path('update-frenchise/<int:pk>', views.update_frenchise_view,name='update-frenchise'),
    path('admin-view-frenchise-salary', views.admin_view_frenchise_salary_view,name='admin-view-frenchise-salary'),

    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view,name='admin-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    path('admin-view-student-fee', views.admin_view_student_fee_view,name='admin-view-student-fee'),


    path('admin-attendance', views.admin_attendance_view,name='admin-attendance'),
    path('admin-take-attendance/<str:cl>', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance/<str:cl>', views.admin_view_attendance_view,name='admin-view-attendance'),


    path('admin-fee', views.admin_fee_view,name='admin-fee'),
    path('admin-view-fee/<str:cl>', views.admin_view_fee_view,name='admin-view-fee'),

    path('admin-notice', views.admin_notice_view,name='admin-notice'),



    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('teacher-attendance', views.teacher_attendance_view,name='teacher-attendance'),
    path('teacher-take-attendance/<str:cl>', views.teacher_take_attendance_view,name='teacher-take-attendance'),
    path('teacher-view-attendance/<str:cl>', views.teacher_view_attendance_view,name='teacher-view-attendance'),
    path('teacher-notice', views.teacher_notice_view,name='teacher-notice'),

    path('frenchise-dashboard', views.frenchise_dashboard_view,name='frenchise-dashboard'),

    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('student-attendance', views.student_attendance_view,name='student-attendance'),




    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
]
