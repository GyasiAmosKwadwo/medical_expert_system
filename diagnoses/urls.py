from django.urls import path
from .views import diagnose_view, kb_manager_view, manual_view

app_name = 'diagnoses'

urlpatterns = [
    path('', diagnose_view, name='index'),
    path('manual/', manual_view, name='manual'),
    path('kb-manager/', kb_manager_view, name='kb_manager'),
]
