"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myapi.views import *
from .views import *
from categories.views import *
from products.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='Home'),
    path('api/', include('myapi.urls')),
    path('prod-list-fun/', prouducts_list_fun, name='prod-list-fun'),
    path('about/', about, name='About'),
    # path('login/', Login, name='Login'),
    #path('register/', Register, name='Register'),
    path("Cats", include('categories.urls' ) , name='Cats'),
    path("Prouducts/", include('products.urls' ) , name='Prouducts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', Login, name='Login'),
    path('register/', Register, name='Register'),
    path('logout/',Logout, name='Logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
