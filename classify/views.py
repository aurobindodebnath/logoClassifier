# import required django modules and functions
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ImageModelForm
from .models import ImageModel

# import required keras and tf functions and modules
import tensorflow as tf
from keras.models import model_from_json
from keras.preprocessing import image

# load model from json file
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into the loaded model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# compile the loaded model before use
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

graph = tf.get_default_graph()


# dictionory mapping prediction to food-outlets
dic = {0: "burgerking",
       1: "dominos",
       2: "kfc",
       3: "pizzahut",
       4: "starbucks"
      }

#### Views ####

def home(request):
	form = ImageModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('predict', args= [instance.id]))
	return render(request, "index.html", {"form": form})

def predict(request, id):
	obj= get_object_or_404(ImageModel, pk=id)
	img = image.load_img(obj.img.url, target_size=(128,128))
	img_array = image.img_to_array(img)
	img_array= img_array.reshape((1,)+ img_array.shape)
	global graph
	with graph.as_default():
		prediction_array = loaded_model.predict(img_array)
		prediction_list=[]
		for x in prediction_array[0]:
			prediction_list.append(int(x))
		for index, value in enumerate(prediction_list):
			if(value==1):
				print("The logo is of "+dic[index].upper())
				return HttpResponseRedirect("http://www.grabon.in/"+dic[index]+"-coupons/")
