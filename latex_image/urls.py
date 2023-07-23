
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from latex_image_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('latex/',views.latex_check)latex_image
    # path('latex/',views.latex_check1),
    path('latex_1/',views.latex_check),
    path('latex_check_cache/',views.latex_check_cache),
    url(r'^latex-image/$', views.latex_image),
    url(r'^latex-image_1/$', views.latex_check),
    # re_path(r'^latex-image1/$',views.latex_image),

]
