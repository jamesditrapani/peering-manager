from rest_framework import serializers

from extras.models import JobResult, ServiceReference
from users.api.nested_serializers import UserNestedSerializer
from utils.api.fields import ContentTypeField

from .nested_serializers import *


class JobResultSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="extras-api:jobresult-detail")
    user = UserNestedSerializer(read_only=True)
    obj_type = ContentTypeField(read_only=True)

    class Meta:
        model = JobResult
        fields = [
            "id",
            "url",
            "created",
            "completed",
            "name",
            "obj_type",
            "status",
            "user",
            "data",
            "job_id",
            "output",
        ]


class ServiceReferenceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="extras-api:servicereference-detail")
    owner_type = ContentTypeField(read_only=True)

    class Meta:
        model = ServiceReference
        fields = [
            "id",
            "url",
            "identifier",
            "owner_id",
            "owner_type"
        ]