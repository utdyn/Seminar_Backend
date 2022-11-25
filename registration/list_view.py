from django.http import JsonResponse
from rest_framework.views import APIView

from registration.models import Seminar, Slot


class ListView(APIView):
    # return Json file with Seminar list
    def get(self, request):

        seminar_list = list(Seminar.objects.values())
        slots = list(Slot.objects.values())
        for slot in slots:
            slot_list = list()
            for seminar in seminar_list:

                if seminar['slot_id'] == slot['id']:
                    slot_list.append(seminar)
            slot["seminar_list"] = slot_list
            slot["radio"] = ""

        return JsonResponse({'seminar_list': slots})

