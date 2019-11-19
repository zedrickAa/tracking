from rest_framework import routers
from app.viewsets import LocationViewSet, EmployeeViewSet, CustomerViewSet, PackageViewSet
router = routers.DefaultRouter()
router.register(r'app', LocationViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'package',  PackageViewSet)