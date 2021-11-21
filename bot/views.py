from rest_framework.views import APIView
from rest_framework.response import Response
from bot.models import Subject

import json


class WebHook(APIView):
    def post(self, request):

        print(json.dumps(request.data, indent=2))

        if request.data["queryResult"]["intent"]["displayName"] == "getListSubjects":
            textResponse = []

            for subject in Subject.objects.all():
                textResponse.append({"text": {"text": [subject.name]}})

            return Response({"fulfillmentMessages": textResponse})

        subjectCodes = request.data["queryResult"]["parameters"]["subject"]

        responseText = []

        for code in subjectCodes:
            try:
                subject = Subject.objects.get(name=code)
                for document in subject.documents.all():
                    responseText.append({"text": {"text": [document.url]}})
            except Exception as e:
                responseText.append({"text": {"text": [str(e)]}})

        return Response({"fulfillmentMessages": responseText})
