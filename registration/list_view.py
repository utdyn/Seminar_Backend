from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.utils import json
import logging
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from registration.models import Participant, Seminar, Slot


class ListView(APIView):

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

