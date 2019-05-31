from django.urls import re_path, include
from link import views

# router = routers.DefaultRouter()
# router.register(r'links', views.LinksView, base_name="links")
# router.register(r'category', views.CategoryView, base_name="category")

urlpatterns = [
    re_path('(?P<version>[v1|v2]+)/links/', views.HomeView.as_view(), name='home'),
]
