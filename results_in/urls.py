from jobs import views  # Check karein ki ye line top par hai
"""
URL configuration for results_in project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from jobs import views  # Check karein ki app ka naam 'jobs' hi hai na

urlpatterns = [
    # 1. Admin Panel
    path('admin/', admin.site.urls),
    
    # 2. Home Page (Website)
    path('', views.home, name='home'),
    
    # 3. Job Details Page
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    
    # 4. MAGIC TOOL (Ye 100% missing hai aapki file mein)
    path('magic-tool/', views.magic_entry_view, name='magic-entry'),
    path('magic-tool/api/', views.fast_entry_api, name='fast-entry-api'),
      # ... purane urls ...
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
