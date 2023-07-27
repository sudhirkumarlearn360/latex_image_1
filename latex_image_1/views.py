from django.shortcuts import render
from django.core.files import File

import datetime, random, urllib, requests
from django.core.cache import cache

from django.http import HttpResponse
from django.core.files.temp import NamedTemporaryFile

from .models import LatexImage

# Create your views here.
try:
	# For Python 3.0 and later
	from urllib.request import urlopen
except ImportError:
	# Fall back to Python 2's urllib2
	from urllib2 import urlopen #type: ignore


def save_latex_image(image_path):
	try:
		latex_path = "https://latex.codecogs.com/png.image?%s" % (image_path)
		latex_image_obj,created = LatexImage.objects.get_or_create(server_image_path=image_path)
		
		return HttpResponse(latex_image_obj +" "+ created)

	except Exception as e:
		return HttpResponse(e)



def home(request):
	return HttpResponse('<h2><p>Latex Image Testing</p><p><a href="http://127.0.0.1:8000/latex_1/?A_2">Link 1 : latex_1</a><br /><a href="http://127.0.0.1:8000/latex-image/?A_2">Link 2 : latex-image</a><br /><a href="http://127.0.0.1:8000/latex-image_1/?A_2">Link 3 : latex-image_1</a></p></h2>')


def health_check(request):
	return HttpResponse("OK")


	
def health_check1(request):
	return HttpResponse("OK")

def latex_check1(request):
	image_path = request.get_full_path().split('?')
	print("image_path............%s %s",image_path,len(image_path) )
	if image_path and len(image_path) > 1:
		image_path = image_path[1]
	HttpResponse("ok")

def latex_check(request):
    image_path = request.get_full_path().split('?')
    print("image_path............%s %s",image_path,len(image_path))
    if image_path and len(image_path) > 1:
        image_path=image_path[1]
        latex_image_obj,created = LatexImage.objects.get_or_create(server_image_path=image_path)    
        latex_path_png = "https://latex.codecogs.com/png.image?%s" % (image_path)
        latex_path_gif = "https://latex.codecogs.com/gif.latex?%s" % (image_path)
        latex_path_svg = "https://latex.codecogs.com/svg.latex?%s" % (image_path)
        return HttpResponse('<p><br>Image ID: '+ str(latex_image_obj.pk)+' <br><br><br><img src="'+latex_path_png+'"> <br><br><img src="'+latex_path_gif+'"><br><br><img src="'+latex_path_svg+'"><br><br>  New Creation Status:  '+ str(created)+'</p>')
    return HttpResponse('No Code, Please add code after "http://127.0.0.1:8000/latex_1/?____"')




def latex_check_cache(request):
    image_path = request.get_full_path().split('?')
    # print("image_path............%s %s",image_path,len(image_path))
    if image_path and len(image_path) > 1:
        image_path=image_path[1]
	
    # # Testing for cache
    #     cache.set('image_path_%s'%(image_path),image_path)
    #     image_path_local = cache.get(('image_path_%s'%(image_path)))
    #     print("image_path_local________ "+str(image_path_local))
    
		
        latex_image_obj,created = LatexImage.objects.get_or_create(server_image_path=image_path)    
        latex_path_png = "https://latex.codecogs.com/png.image?%s" % (image_path)
        latex_path_gif = "https://latex.codecogs.com/gif.latex?%s" % (image_path)
        latex_path_svg = "https://latex.codecogs.com/svg.latex?%s" % (image_path)
        return HttpResponse('<p><br>Image ID: '+ str(latex_image_obj.pk)+' <br><br><br><img src="'+latex_path_png+'"> <br><br><img src="'+latex_path_gif+'"><br><br><img src="'+latex_path_svg+'"><br><br>  New Creation Status:  '+ str(created)+'</p>')
    return HttpResponse('No Code, Please add code after "http://127.0.0.1:8000/latex_1/?____"')

def latex_image(request):
	image_path = request.get_full_path().split('?')
	print("image_path............%s %s",image_path,len(image_path) )

	if image_path and len(image_path) > 1:
		image_path = image_path[1]
		if LatexImage.objects.filter(server_image_path=image_path).exists():
			print("Not Created........exists")
			image = LatexImage.objects.filter(server_image_path=image_path).last()
			latex_path_svg = "https://latex.codecogs.com/svg.latex?%s" % (image.server_image_path)
			created = "Not Created"            
			return HttpResponse('<p><br><br> Image ID: '+str(image.id)+'<br><br><img src="'+latex_path_svg+'"><br><br>  '+ str(created)+'</p>' )
		else:
			print("Created........Not exists")
			image = LatexImage.objects.create(server_image_path=image_path)
			latex_path_svg = "https://latex.codecogs.com/svg.latex?%s" % (str(image.server_image_path))
			created = "Created"
			return HttpResponse('<p><br><br> Image ID: '+str(image.id)+'<br><br><img src="'+latex_path_svg+'"><br><br>  '+ str(created)+'</p>' )
	return HttpResponse("No Code")