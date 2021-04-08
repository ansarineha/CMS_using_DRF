from django.conf.urls import url, include
from django.urls import path
from drf_api.views import userList, contentList, contentDetail, contentCreate, contentUpdate, contentDelete, ContentSearchView


urlpatterns = [
    url(r'^auth/', include('rest_auth.urls')),
    path('users/users-list', userList),
    path('contents/content-list', contentList),
    path('contents/content-detail/<str:pk>', contentDetail),
    path('contents/content-create', contentCreate),
    path('contents/content-update/<str:pk>', contentUpdate),
    path('contents/content-delete/<str:pk>', contentDelete),
    path('contents/content-search/', ContentSearchView.as_view()),
]