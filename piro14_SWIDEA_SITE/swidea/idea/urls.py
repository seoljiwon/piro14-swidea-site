from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', view=views.idea_detail, name='idea_detail'),
    path('idea/create/', view=views.idea_create, name='idea_create'),
    path('idea/<int:pk>/edit/', view=views.idea_edit, name='idea_edit'),
    path('idea/<int:pk>/delete/', view=views.idea_delete, name='idea_delete'),
    path('devtool/', view=views.devtool_list, name='devtool_list'),
    path('devtool/<int:pk>/', view=views.devtool_detail, name='devtool_detail'),
    path('devtool/create/', view=views.devtool_create, name='devtool_create'),
    path('devtool/<int:pk>/edit/', view=views.devtool_edit, name='devtool_edit'),
    path('devtool/<int:pk>/delete/',
         view=views.devtool_delete, name='devtool_delete'),
]
