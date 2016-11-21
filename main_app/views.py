from django.shortcuts import render
from .models import Treasure
# Create your views here.

def index(request):
	treasure = Treasure.objects.all()
	return render(request, 'index.html', {'treasures':treasures})
	
	
	
class Treasure:
	def __init__(self, name, value, material, location, img_url):
		self.name = name
		self.value = value
		self.material = material
		self.location = location
		self.img_url = img_url

treasures = [
	Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM","C:/Users/Temi_Ogunsanya/Treasuregram/main_app/static/images/gold-nugget.png"),
	Treasure("Fool's Gold", 0.5, 'trash', "swag, LA", "images/fools-gold.png"),
	Treasure('coffee can', 700.00, 'Aluminum Oxide', "Curly's Creek, NM", "images/coffee-can.png")
]