from django.urls import path
from .views import (
    UserInfoAPIView,
    UserUpdateAPIView,
    login_view,
    logout_view,
    profile_update,
    password_change,
    user_profile_view,
    user_info_page
)

urlpatterns = [
    # REST API
    path('api/user/', UserInfoAPIView.as_view(), name='user_info'),
    path('api/user_update/', UserUpdateAPIView.as_view(), name='user_update'),

    # HTML 페이지
    path('user_info/', user_info_page, name='user_info_page'),
    path('profile/', user_profile_view, name='user_profile_view'),

    # 로그인/정보수정 관련
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/update/', profile_update, name='profile_update'),
    path('password/change/', password_change, name='password_change'),
]
