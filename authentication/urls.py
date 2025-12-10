from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserProfielView, UserProfieUpdatelView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfielView.as_view(), name='user_profile'),
    path('profile/update', UserProfieUpdatelView.as_view(), name='user_profile'),
]
