"""club_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from club_app.views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('new/', new, name='new'),
    path('detail/<int:club_id>/', detail, name='detail'),
    path('comment/<int:club_id>/', comment, name='comment',),
    path('update/<int:club_id>/', update, name='update'),
    path('delete/<int:club_id>/', delete, name='delete'),
    path('comment_delete/<int:club_id>/<int:comment_id>', comment_delete, name='comment_delete'),

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup', signup, name='signup')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
