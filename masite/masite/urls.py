"""ma site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect('/blog')


urlpatterns = [
    path('', redirect),
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    # book styles include wasnt working with django 3.0
    # fix reference :https://docs.djangoproject.com/en/3.0/topics/http/urls/#namespaces-and-include
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
]



