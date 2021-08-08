from django.contrib import admin
from django.urls import path, include
from .views import view_all_orphange, view_index, view_dashboard, view_child,add_new_child_form, view_child_detials,upload_image_child,update_child,search_child,register_orphange,update_profile_orphange,more_info_orphange

urlpatterns = [
    path('', view_index, name="orphange"),
    path('dashboard/', view_dashboard, name="dashboard"),
    # add_new_child
    path('child/', view_child, name="child"),
    path('add_new_child/', add_new_child_form, name="add_new_child"),
    path('child_details/<int:pk>', view_child_detials, name="child_details"),
    path('upload_image_child/', upload_image_child, name="upload_image_child"),
    path('update_child/<int:pk>', update_child, name="update_child"),
    path('search_child/', search_child, name="search_child"),
    path('login_orphange/', register_orphange, name="login_orphange"),
    path('update_profile_orphange/', update_profile_orphange, name="update_profile_orphange"),
    path('more_info_orphange/', more_info_orphange, name="more_info_orphange")
]
