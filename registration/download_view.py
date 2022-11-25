import os
from django.conf import settings
from django.http import HttpResponse
import xlsxwriter
from registration.models import Seminar, Participant, Participant2Seminar


# create and download an Excel master sheet from the database data
def DownloadView(request):

    workbook = xlsxwriter.Workbook('mastersheet.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    seminar_list = list(Seminar.objects.values())
    participants = list(Participant.objects.values())
    p2ss = list(Participant2Seminar.objects.values())

    worksheet.write(0, 1, "gender", bold)
    worksheet.write(0, 2, "name", bold)
    worksheet.write(0, 3, "birthday", bold)
    worksheet.write(0, 4, "address", bold)
    worksheet.write(0, 5, "telephone", bold)
    worksheet.write(0, 6, "memberNr", bold)
    worksheet.write(0, 7, "food", bold)

    for seminar in seminar_list:
        worksheet.write(0, seminar['id']+7, seminar["tag"], bold)

    for p in participants:
        worksheet.write(p['id'], 1, p['gender'])
        worksheet.write(p['id'], 2, p['name'])
        worksheet.write(p['id'], 3, p['geb'])
        worksheet.write(p['id'], 4, p['address'])
        worksheet.write(p['id'], 5, p['telephone'])
        worksheet.write(p['id'], 6, p['memberNr'])
        worksheet.write(p['id'], 7, p['food'])

    for p2s in p2ss:
        worksheet.write(p2s['participant_id'], p2s['seminar_id']+7, p2s['pref'])

    workbook.close()

    file_path = os. getcwd()+os.path.join(settings.MEDIA_ROOT, "/mastersheet.xlsx")
    print(os. getcwd())

    if os.path.exists(file_path):
        print(file_path)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

    return HttpResponse("<h1>Downloading the excel master sheet</h1>")


