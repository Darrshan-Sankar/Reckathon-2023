from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_form, name='main'),
    path('idea/list/', views.idea_list, name='idea_list'),
    path('idea/submit/', views.idea_submit, name='idea_submit'),
    path('idea/submit/success/', views.idea_submit_success, name='idea_submit_success'),
    path('login_signup/', views.login_signup, name='login_signup'),
    path('idea/', views.idea, name='idea'),
    path('chat', views.chat, name='chat'),
    #path('signup/', views.signup, name='signup'),
    #path('login/', views.login_view, name='login'),
]