from rest_framework import generics

from common.models import Flag, Binding
from api_v1.serializers import FlagSerializer, BindingSerializer


class BindingList(generics.ListCreateAPIView):
    serializer_class = BindingSerializer
    queryset = Binding.objects.all()
    filterset_fields = [
        "subject",
    ]


binding_list_view = BindingList.as_view()


class BindingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BindingSerializer
    queryset = Binding.objects.all()


binding_detail_view = BindingDetail.as_view()
