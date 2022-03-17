from django.urls import path
from blog.views import BlogTop, BlogDetail, BlogCategory, BlogTag

urlpatterns = [
    path('', BlogTop.as_view(), name="Top"),
    path('category/<str:slug>', BlogCategory.as_view(), name="Category"),
    path('tag/<str:slug>', BlogTag.as_view(), name="Tag"),
    path('detail/<int:pk>/', BlogDetail.as_view(), name="Detail"),
]