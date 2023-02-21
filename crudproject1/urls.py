"""crudproject1 URL Configuration

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
from django.urls import path
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
from enroll.views import GeneratePdf
urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/', views.add_show, name="addandshow"),
    path('cal/<int:id>/', views.calculate, name="calculate"),
    path('calc/<int:id>/', views.calculations, name="calculations"),
    path('inv/<int:id>', views.show_invoice, name="show_invoice"),
    path('qr/<int:id>', views.generate_qr, name="generate_qr"),
    path('geninv/<int:id>', views.generate_inv, name="generate_inv"),
    path('qrnli/<int:id>', views.generate_qr_nli, name="generate_qr_nli"),
    path('invnli/<int:id>', views.generate_inv_nli, name="generate_inv_nli"),
    path('dow/', views.download_invoice, name="download_invoice"),
    path('pdf/<int:id>/', GeneratePdf.as_view(),name='pdf'), 
    path('call/<int:id>/', views.update_data, name="updatedata"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('new/',views.shownewinvoice,name='new'),
    path('calqr/',views.calqr,name='calqr'),
#     from django.contrib import admin
# from django.urls import path, include
# from home import views

# urlpatterns = [
    path('home/',views.home,name="home"),
    path('base2/',views.base2,name="base2"),
    path('', views.landing, name="landing"),
    path('', views.handleSignUp, name="signup"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('lic', views.handeLogin, name="LicenseKey"),
    path('logout', views.handelLogout, name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
