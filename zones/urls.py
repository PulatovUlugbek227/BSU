from ctypes import alignment
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index_madaniyot', views.index_madaniyot, name='index_madaniyot'),
    path('trees/create', views.tree_create, name='tree_create'),
    path('student/create', views.student_create, name='student_create'),
    path('group/create', views.group_create, name='group_create'),
    path('tree/edit/<int:id>', views.tree_edit, name='tree_edit'),
    path('tree_delete/<int:id>', views.tree_delete, name='tree_delete'),
    path('trees/detail/<int:id>', views.tree_detail, name='tree_detail'),
    path('index_detail', views.index_detail, name="index_detail"),
    path('index_chek', views.index_chek, name='index_chek'),
    path('groups/search/', views.search, name="search"),
    path('groups/', views.groups, name="groups"),
    path('student/<int:id>/', views.student, name="student"),
    path('login/', views.login_site, name='login_site'),
    path('logout/', views.logout_site, name='logout_url'),
    path('all_area/', views.all_area, name='all_area'),
    path('all_area/<slug:slug>/', views.all_area_detail, name='all_area_detail_url'),
    path('all_area/create', views.all_zones_create, name='all_area_create'),
]