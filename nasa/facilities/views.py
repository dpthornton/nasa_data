from facilities.models import Facility
from .serializers import FacilitiesSerializer
from rest_framework import generics

class Facilities(generics.ListAPIView):
    """
    Return a list of NASA facilities.
    """
    queryset = Facility.objects.filter(status='Active')
    serializer_class = FacilitiesSerializer