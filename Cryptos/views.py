from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Crypto
from .permissions import IsOwnerOrReadOnly
from .serializers import CryptoSerializer


class CryptoList(ListCreateAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer


class CryptoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer
