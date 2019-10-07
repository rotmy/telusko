from django.shortcuts import render
from .models import Destination


# Create your views here.


def home(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})
    # return HttpResponse("Hello World!")


# Below is to get static content
# des1 = Destination()
# des1.name = "Mumbai"
# des1.description = "The City That Never Sleeps"
# des1.price = 890
# des1.img = 'destination_1.jpg'
# des1.offer = True


# des2 = Destination()
# des2.name = "Indonisia"
# des2.description = "The Textile City"
# des2.price = 770
# des2.img = 'destination_2.jpg'
# des2.offer = False


# des3 = Destination()
# des3.name = "San Franscisco"
# des3.description = "The Tourist Attraction"
# des3.price = 650
# des3.img = 'destination_3.jpg'
# des3.offer = False


# des4 = Destination()
# des4.name = "Paris"
# des4.description = "The Home of Fashion"
# des4.price = 880
# des4.img = 'destination_4.jpg'
# des4.offer = False


# des5 = Destination()
# des5.name = "Iceland"
# des5.description = "The Blue Sea Land"
# des5.price = 1200
# des5.img = 'destination_5.jpg'
# des5.offer = False


# des6 = Destination()
# des6.name = "Australia"
# des6.description = "The Land of Peace"
# des6.price = 1250
# des6.img = 'destination_6.jpg'
# des6.offer = True

# dests = [des1, des2, des3, des4, des5, des6]
