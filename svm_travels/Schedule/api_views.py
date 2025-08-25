from django.http import JsonResponse
from .models import Schedule

def schedule_search_api(request):
    start = request.GET.get('start', '').strip()
    end = request.GET.get('end', '').strip()

    schedules = Schedule.objects.all()
    if start:
        schedules = schedules.filter(busroute__start__name__icontains=start)
    if end:
        schedules = schedules.filter(busroute__end__name__icontains=end)

    data = []
    for s in schedules:
        data.append({
            'id': s.id,
            'start': s.busroute.start.name,
            'end': s.busroute.end.name,
            'bus_name': s.bus.reg_no,
            'price': s.busroute.price,
            'departure': s.start_time.strftime('%H:%M'),
        })

    return JsonResponse(data, safe=False)
