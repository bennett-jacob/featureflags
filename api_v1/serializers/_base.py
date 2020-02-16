from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        read_only_fields = (
            "created_at",
            "updated_at",
        )