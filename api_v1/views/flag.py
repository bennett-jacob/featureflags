from rest_framework import generics

from common.models import Flag, Binding
from api_v1.serializers import FlagSerializer, BindingSerializer


class FlagList(generics.CreateAPIView):
    serializer_class = FlagSerializer
    queryset = Flag.objects.all()


flag_list_view = FlagList.as_view()


class FlagDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FlagSerializer
    queryset = Flag.objects.all()
    lookup_field = "name"


flag_detail_view = FlagDetail.as_view()


class FlagBindingList(generics.ListAPIView):
    serializer_class = BindingSerializer

    def get_queryset(self):
        try:
            flag_name = self.kwargs.get("name", None)
            return Binding.objects.filter(flag__name=flag_name)
        except:
            return Binding.objects.none()


flag_binding_list_view = FlagBindingList.as_view()
