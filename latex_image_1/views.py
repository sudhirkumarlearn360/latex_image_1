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
		latex_image_obj,created = LatexImage.objects.get_or_create(server_image_path=image_path)
		
		return HttpResponse(latex_image_obj +" "+ created)

	except Exception as e:
		return HttpResponse(e)
	

# async def open_image(img):
# 	return await urlopen(img).read()
	
def latex_save(request):
	image_path = request.get_full_path().split('?')
	return latex_save1(image_path)

def latex_save1(image_path):

	# image_path = request.get_full_path().split('?')
	# print("image_path............%s %s",image_path,len(image_path))
	if image_path and len(image_path) > 1:
		image_path=image_path[1]
		latex_image_obj,created = LatexImage.objects.get_or_create(server_image_path=image_path)    
		latex_path_png = "https://latex.codecogs.com/png.image?%s" % (image_path)
		latex_path_gif = "https://latex.codecogs.com/gif.latex?%s" % (image_path)
		latex_path_svg = "https://latex.codecogs.com/svg.latex?%s" % (image_path)


		if created:

			try:

				img_temp = NamedTemporaryFile()

				image_content = urlopen(latex_path_svg).read()
				count_while =0
				while(str(image_content).find("xml")<0):
					image_content = urlopen(latex_path_svg).read()
					print("IMAGE ISSUE............. ",latex_path_svg)
					count_while +=1
					if(count_while >3):
						break

				img_temp.write(image_content)
				img_temp.flush()

				# print("img_temp.......",img_temp)
				# print("image_content.......",image_content)


				img_filename = 'latex_%s_file.svg' % (latex_image_obj.id)
				latex_image_obj.local_image.save(img_filename, File(img_temp))

				# print("img_filename.......",img_filename)


				latex_image_obj.save()
				image_path_local = latex_image_obj.local_image.url

			except Exception as e:
				image_path_local = ""
				print("image_path_local............ ", e)

				# # if image not rendered properly then it will delete that id and create new
				# latex_image_obj.delete()
				# created = str(created )*2
				# # latex_save()
			
		else:
			image_path_local = latex_image_obj.local_image.url
		

		return HttpResponse('<p><br><br> Image Path: '+str(image_path_local)+'<br><br><img src="'+image_path_local+'"'+'<br><br><br> Image ID: '+str(latex_image_obj.id)+'<br><br><br><img src="'+latex_path_gif+'"<br><br><br><img src="'+latex_path_png+'"<br><br><br><img src="'+latex_path_svg+'"><br><br>  '+ str(created)+'</p>' )
	return HttpResponse('No Code, Please add code after "http://127.0.0.1:8000/latex_save/?____"')





def home(request):
	images = LatexImage.objects.all().values()
	# print(images)
	data=""

	for img in images:
		data = data +" <a href='/latex_save/?"+str(img['server_image_path'])+ "' target='_blank' style='text-decoration: none'>  <div>"+str(img['id'])+":   <img src='https://latex.codecogs.com/svg.image?"+img['server_image_path']+"'></div> </a><br>" 
		# print(img['id'])

	return HttpResponse('<h2><p>Latex Image Testing</p><p><a href="latex_1/?A_2">Link 1 : latex_1</a><br /><a href="latex-image/?A_2">Link 2 : latex-image</a><br /><a href="latex-image_1/?A_2">Link 3 : latex-image_1</a></p><br><br>Latex Images Created</h2>'+str(data))


def health_check(request):
	return HttpResponse("OK")

# def media(request):
# 	test = "http://127.0.0.1:8000/media/img/latex/latex_48_file.png"
# 	# image_path = request.get_full_path().split('media')
# 	image_path = test.split('/')

# 	print(image_path[6])

# 	return HttpResponse("OK")



	
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

		latex_path_png = "https://latex.codecogs.com/png.image?%s" % (image_path)
		latex_path_gif = "https://latex.codecogs.com/gif.latex?%s" % (image_path)
		latex_path_svg = "https://latex.codecogs.com/svg.latex?%s" % (image_path)
	
		if LatexImage.objects.filter(server_image_path=image_path).exists():
			print("Not Created........exists")
			image = LatexImage.objects.filter(server_image_path=image_path).last()
			created = "Not Created"     

			print("image.local_image.url....." + image.local_image.url)
			print(image.local_image)
			print(image.local_image.path)

			return HttpResponse('<p><br><br> Image Path: '+str(image.local_image.url)+'<br><br><img src="'+image.local_image.url+'"'+'<br><br><br> Image ID: '+str(image.id)+'<br><br><br><img src="'+latex_path_gif+'"<br><br><br><img src="'+latex_path_png+'"<br><br><br><img src="'+latex_path_svg+'"><br><br>  '+ str(created)+'</p>' )
		else:
			print("Created........Not exists")
			image = LatexImage.objects.create(server_image_path=image_path)
			latex_path_s = "https://latex.codecogs.com/svg.latex?%s" % (str(image.server_image_path))

			try:

				img_temp = NamedTemporaryFile()
				image_content = urlopen(latex_path_s).read()
				img_temp.write(image_content)
				img_temp.flush()

				img_filename = 'latex_%s_file.svg' % (image.id)
				image.local_image.save(img_filename, File(img_temp))

				image.save()
				image_path_local = image.local_image.url

			except Exception as e:
				image_path_local = ""


			created = "Created"
			return HttpResponse('<p><br><br> Image Path: '+str(image_path_local)+'<br><br><img src="'+image_path_local+'"'+'<br><br><br> Image ID: '+str(image.id)+'<br><br><br><img src="'+latex_path_gif+'"<br><br><br><img src="'+latex_path_png+'"<br><br><br><img src="'+latex_path_svg+'"><br><br>  '+ str(created)+'</p>' )
	return HttpResponse("No Code")