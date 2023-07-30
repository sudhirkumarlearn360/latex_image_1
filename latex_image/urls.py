
from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include,re_path
from latex_image_1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('media/img/latex/', views.media),
    path('', views.home),
    # path('latex/',views.latex_check)latex_image
    # path('latex/',views.latex_check1),
    path('latex_1/',views.latex_check),
    path('latex_image/',views.latex_image),
    path('latex_save/',views.latex_save),
    path('latex_check_cache/',views.latex_check_cache),
    url(r'^latex-image/$', views.latex_image),
    url(r'^latex-image_1/$', views.latex_check),
    # re_path(r'^latex-image1/$',views.latex_image),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)