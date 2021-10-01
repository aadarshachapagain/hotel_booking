import os
import shutil
from io import BytesIO
from os.path import join

from PIL import Image
from django.core.files.base import File
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

from travel.devsettings import BASE_DIR, MEDIA_ROOT, MEDIA_URL


def all_percentage_complete(self):
	all_fields = self._meta.fields
	percent = {}
	total = 0.00
	each_percentage = 100 / len(all_fields)
	each_percentage = round(each_percentage, 2)
	for field in all_fields:
		percent.update({field.name: each_percentage})
		method = getattr(self, str(field.name))
		if method:
			total += percent.get(field.name)
			total = round(total, 2)
	
	total = round(total)
	return "%s" % (total)


def hotel_gallery_percentage_complete(temp, required_count):
	total = 0.00
	percent = (temp / required_count) * 100
	total = round(percent)
	return "%s" % (total)


# this function is created in order to show preview of cropped image to user.
# this function is called via api from html template.
# we save cropped image for temporary and after form is submitted we delete the image from temp folder.
def croppedImagePreview(request):
	# for creating specific directory
	# eg: for profile pic -> model = user , inventory pic -> model = inventory
	model = request.POST.get('model')
	print(model)
	# concat model with loggedIn userId
	userModel = model + '_' + str(request.user.id)
	# x,y,height and width are required to crop image
	left = float(request.POST.get('x'))
	top = float(request.POST.get('y'))
	bottom = float(request.POST.get('width')) + left
	right = float(request.POST.get('height')) + top
	original_image = request.FILES.get('image')
	# code to know extension of image
	extName = original_image.name.split(".")[-1]
	# code for seperating name from extension
	imageName = original_image.name.replace(extName + '.', '')
	# there is no jpg format in pillow so replace jpg with JPEg, PNG is available in pillow
	format = 'JPEG' if extName.lower() == 'jpg' else extName.upper()
	img_io = BytesIO()
	# open file
	original_image = Image.open(original_image)
	# crop use given coordinates
	cropped_img = original_image.crop((left, top, bottom, right))
	# save image with format
	cropped_img.save(img_io, format)
	# create django friendly files , it returns file which can be saved in django model directly
	img_content = File(img_io, name=imageName)
	# create new temporary directory in media directory
	uploadDirectory = join(MEDIA_ROOT, 'temporary/')
	# inside temporary directory create directory using above created userModel. Eg: user_4
	uploadDirectory = join(uploadDirectory, userModel)
	# we need media url to return url of saved image. media/temporary
	uploadURL = join(MEDIA_URL, 'temporary/')
	# concat temporary url to userModel. media/temporary/user_4
	uploadURL = join(uploadURL, userModel)
	# create object of FileSystemStorage and pass directory and url created above
	fs = FileSystemStorage(
		location=uploadDirectory,
		base_url=uploadURL
	)
	# save image to give url
	filename = fs.save(imageName, img_content)
	# extract url of recently saved image
	uploaded_file_url = fs.url(filename)
	# return url so user can preview
	return JsonResponse({
		'success': True,
		'img_content': uploaded_file_url,
	})


# this function is created to delete the temporary image which was saved only for preview purpose only.
def deleteCroppedImagePreview(request, model):
	userModel = model + '_' + str(request.user.id)
	uploadDirectory = join(MEDIA_ROOT, 'temporary/')
	# inside temporary directory create directory using above created userModel. Eg: user_4
	uploadDirectory = join(uploadDirectory, userModel)
	flag = shutil.rmtree(uploadDirectory, ignore_errors=True)
	return True
