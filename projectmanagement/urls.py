<<<<<<< HEAD
"""
URL configuration for projectmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pma import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.signin),
    path('',views.dashboard),
    path('logout/',views.signout),
    path('caseslists/',views.caseslists),
    path('fiblists/',views.fiblists),
    path('createfibranch/',views.createfibranch),
    path('createcases/',views.createcases),
    path('deletecases/<int:id>',views.deletecases,name='delete_cases'),
    path('updatecases/<int:id>',views.updatecases,name='updatecases'),
    path('deletefibranch/<int:id>',views.deletefibranch,name='deletefibranch'),
    path('updatefibranch/<int:id>',views.updatefibranch,name='updatefibranch'),
    path('employeeslists/',views.employeeslists),
    path('createemployees/',views.createemployees),
    path('updateemployee/<int:id>',views.updateemployee,name='updateemployee'),
    path('deleteemployee/<int:id>',views.deleteemployee,name='deleteemployee'),
    path('activeemployee/<int:id>',views.activeemployee,name='activeemployee'),

]
=======
"""
URL configuration for projectmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pma import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.signin),
    path('',views.dashboard),
    path('logout/',views.signout),
    path('caseslists/',views.caseslists),
    path('fiblists/',views.fiblists),
    path('createfibranch/',views.createfibranch),
    path('createcases/',views.createcases),
    path('deletecases/<int:id>',views.deletecases,name='delete_cases'),
    path('updatecases/<int:id>',views.updatecases,name='updatecases'),
    path('deletefibranch/<int:id>',views.deletefibranch,name='deletefibranch'),
    path('updatefibranch/<int:id>',views.updatefibranch,name='updatefibranch'),
    path('employeeslists/',views.employeeslists),
]
>>>>>>> 6c74325bf6798dfe2e4d30e5b82ef5a029b309d3
