from django.urls import path 

from .views.course import (
    home, list_course, 
    add_course, create_course, 
    edit_course, update_course
)

from .views.category import (
    list_categories, 
    add_category, create_category, 
    edit_category, update_category
)

from .views.employee import (
    list_employees, 
    add_employee, create_employee, 
    edit_employee, update_employee
)

from .views.trainee import (
    list_trainees,
    add_trainee, create_trainee,
)

from .views.trainee_course import (
    list_trainee_course,
    add_trainee_course,
    create_trainee_course
)

urlpatterns = [

    # course UrlConf
    path('course/list/', list_course, name="list_course"),
    path('course/add/', add_course, name="add_course"),
    # path('course/add/<input_data>/', add_course, name="add_course"),
    path('course/create/', create_course, name="create_course"),
    path('course/<int:pk>/edit/', edit_course, name="edit_course"),
    path('course/<int:pk>/update/', update_course, name="update_course"),

    # Category UrlConf
    path('category/list/', list_categories, name="list_categories"),
    path('category/add/', add_category, name="add_category"),
    path('category/create/', create_category, name="create_category"),
    path('category/<int:pk>/edit/', edit_category, name="edit_category"),
    path('category/<int:pk>/update/', update_category, name="update_category"),

    # Employee UrlConf
    path('employee/list/', list_employees, name="list_employees"),
    path('employee/add/', add_employee, name="add_employee"),
    path('employee/create/', create_employee, name="create_employee"),
    path('employee/<int:pk>/edit/', edit_employee, name="edit_employee"),
    path('employee/<int:pk>/update/', update_employee, name="update_employee"),

    # Trainee UrlConf
    path('trainee/list/', list_trainees, name="list_trainee"),
    path('trainee/add/', add_trainee, name="add_trainee"),
    path('trainee/create/', create_trainee, name="create_trainee"),

    # Trainee Course UrlConf
    path('trainee_course/list/', list_trainee_course, name="list_trainee_course"),
    path('trainee_course/add/', add_trainee_course, name="add_trainee_course"),
    path("trainee_course/create/", create_trainee_course, name="create_trainee_course")
    
]
