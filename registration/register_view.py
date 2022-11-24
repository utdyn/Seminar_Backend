from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.utils import json
import logging
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from registration.models import Participant, Participant2Seminar, Seminar


class RegisterView(APIView):

    def put(self, request):

        form = json.loads(request.body.decode('utf-8'))['content']
        user = Participant(
            gender=form['gender'],
            name=form['name'],
            geb=form['geb'],
            address=form['address'],
            telephone=form['telephone'],
            memberNr=form['memberNr'],
            food=form['food'],
        )
        user.save()
        slots = form['slots']
        for slot in slots:
            for check in slot["check"]:
                seminar = Seminar.objects.filter(id=check).first()
                p = Participant2Seminar(participant=user,
                                        seminar=seminar,
                                        pref="alt")
                p.save()
            seminar = Seminar.objects.filter(id=slot["radio"]).first()
            p = Participant2Seminar(participant=user,
                                    seminar=seminar,
                                    pref="primary")
            p.save()

        return JsonResponse({'instance_id': user.id})
