from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from bot.models import Branch, Semister, Subject, Document


class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class SemisterSerializer(ModelSerializer):
    class Meta:
        model = Semister
        fields = "__all__"


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
