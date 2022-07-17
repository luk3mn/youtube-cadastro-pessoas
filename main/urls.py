from django.urls import path
from .views import HomeView
from django.contrib.auth.decorators import login_required # solicta login para execuatr a ação

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'), # busca a classe 'HomeView' no arquivo 'views'
]