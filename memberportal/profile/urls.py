from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/password/reset', views.reset_password, name='reset_password'),
    path('profile/password/reset/<uuid:reset_token>', views.reset_password, name='reset_password'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/access/view/', views.access_permissions, name='access_permissions'),
    path('profile/theme/edit/', views.edit_theme_song, name='edit_theme_song'),
    path('members/list/', views.member_list, name='member_list'),
    path('members/recent/', views.recent_swipes, name='recent_swipes'),
    path('members/lastseen/', views.last_seen, name='last_seen'),
    path('member/<int:member_id>/edit/', views.admin_edit_member, name='admin_edit_member'),
    path('api/member/<int:member_id>/state/<str:state>/', views.set_state, name='set_state'),
    path('api/member/<int:member_id>/edit/', views.admin_edit_member, name='admin_edit_member'),
    path('api/member/<int:member_id>/access/', views.admin_edit_access, name='admin_edit_access'),
    path('api/member/<int:member_id>/logs/', views.admin_member_logs, name='admin_member_logs'),
    path('api/member/<int:member_id>/email/welcome', views.resend_welcome_email, name='resend_welcome_email'),
    path('api/member/<int:member_id>/xero/add', views.add_to_xero, name='add_to_xero'),
    path('api/member/<int:member_id>/spacebucks/transactions/', views.admin_spacebucks_transactions, name="admin_spacebucks_transactions"),
    path('api/member/<int:member_id>/spacebucks/add/<int:amount>', views.admin_add_spacebucks, name='admin_add_spacebucks_amount'),
    path('api/member/<int:member_id>/spacebucks/add/', views.admin_add_spacebucks, name='admin_add_spacebucks'),
    path('api/member/create', views.create_account_api, name='create_account_api'),
]
