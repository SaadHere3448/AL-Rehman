"""
URL configuration for AlRehman_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from interface.views import *
from add.views import *
from contact.views import *
from about.views import *
from buy.views import *
from AdminProfile.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', interface, name="interface"),
    path('Fill-Storage/', Fill_Storage , name="Fill-Storage"),
    path('Add-Product/', Add_Product, name="Add-Product"),
    path('Contact/', contact, name="Contact"),
    path('About/', About, name="Abou-Page"),
    path('buy/', Buy, name="Buy"),
    path('admin-profile/', AdminProfile, name="Admin-profile"),
    path('fulfil/<id>/', Fulfil, name="Fulfil"),
    path('hide/<id>/', Hide, name="Hide-It"),
    path('display/<id>/', Display, name="Display-It"),
    path('update/<id>/', Update, name="Update")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
