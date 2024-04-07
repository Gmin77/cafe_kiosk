from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from cafe.views import MenuLV, MenuDV

urlpatterns = [
    path('cafe/', MenuLV.as_view(), name = 'index'),
    path('cafe/<int:pk>/', MenuDV.as_view(), name='detail'),
    path('cafe/result', MenuLV.as_view(), name='result'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
