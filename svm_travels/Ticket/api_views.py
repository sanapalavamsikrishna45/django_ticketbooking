from django.http import JsonResponse
from django.views import View
from .models import Passenger
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# API to list all passengers
class PassengerListAPI(View):
    def get(self, request):
        passengers = Passenger.objects.all().values('id', 'name', 'age', 'gender')
        return JsonResponse(list(passengers), safe=False)

# API to add a new passenger
@method_decorator(csrf_exempt, name='dispatch')
class PassengerAddAPI(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')

        if not name or not age or not gender:
            return JsonResponse({'error': 'Missing fields'}, status=400)

        passenger = Passenger.objects.create(name=name, age=age, gender=gender)
        return JsonResponse({'id': passenger.id, 'name': passenger.name, 'age': passenger.age, 'gender': passenger.gender})
