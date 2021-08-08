from django.contrib import admin
from django.urls import path,include
from .views import view_index,view_about,view_contact_us,view_child,view_team_work,view_all_child,logout,detials_requests,sponser_login,update_profile,sponser_child_details,view_sponser_child,view_all_request
from orphanage.views import  view_all_orphange,orphange_detials,detials_child
from sponser.views import make_request

urlpatterns = [
    path('', view_index, name='home_index'),
    path('about',view_about, name="about"),
    path('team_work', view_team_work, name="team_work"),
    path('contact_us', view_contact_us, name="contact_us"),
    path('all_child', view_child, name="all_child"),
    path('all_orphange', view_all_orphange, name="all_orphange"),
    path('orphange_details/<int:pk>',orphange_detials, name="orphange_details"),
    path('detials_child/<int:pk>', detials_child, name="detials_child"),
    path('all_child/', view_all_child, name="all_child"),
    path('sponser_login/', sponser_login, name="sponser_login"),
    path('update_profile/', update_profile, name="update_profile"),
    path('make_request/', make_request, name="make_request"),
    path('view_all_request/', view_all_request, name="view_all_request"),
    path('view_sponser_child/', view_sponser_child, name="view_sponser_child"),
    path('sponser_child_details/<int:pk>', sponser_child_details, name="sponser_child_details"),
    path('view_detials_requests/<int:pk>', detials_requests, name="view_detials_requests"),
    path('logout', logout, name="logout"),


]