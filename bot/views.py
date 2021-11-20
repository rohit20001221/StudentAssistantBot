from django.http import Http404
from rest_framework.generics import ListAPIView
from bot.models import Branch
from bot.serializers import (
    BranchSerializer,
    DocumentSerializer,
    SemisterSerializer,
    SubjectSerializer,
)


class BranchListAPI(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class SemisterBranchListAPI(ListAPIView):
    serializer_class = SemisterSerializer

    def get_queryset(self):
        id = self.kwargs["id"]

        try:
            return Branch.objects.get(id=id).semisters.all()
        except:
            raise Http404


class BranchSemisterSubjectListAPI(ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        branchId = self.kwargs["branchId"]
        semisterId = self.kwargs["semisterId"]

        try:
            return (
                Branch.objects.get(id=branchId)
                .semisters.get(id=semisterId)
                .subjects.all()
            )
        except:
            raise Http404


class BranchSemisterSubjectDocumentListAPI(ListAPIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        branchId = self.kwargs["branchId"]
        semisterId = self.kwargs["semisterId"]
        subjectId = self.kwargs["subjectId"]

        try:
            return (
                Branch.objects.get(id=branchId)
                .semisters.get(id=semisterId)
                .subjects.get(id=subjectId)
                .documents.all()
            )
        except Exception as e:
            print(e)
            raise Http404
