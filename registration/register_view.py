from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView

from registration.models import Participant, Participant2Seminar, Seminar


class RegisterView(APIView):
    # return the new Participant id after saving it is data
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

        return JsonResponse({'id': user.id})
