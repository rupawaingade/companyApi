
from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'Rama',
        'Raghav',
        'Madhav'

    ]
    return JsonResponse(friends,safe=False)