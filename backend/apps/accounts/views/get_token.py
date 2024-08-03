from rest_framework_simplejwt.views import TokenObtainPairView
from apps.accounts.serializers import AdditionalFieldsTokenSerializer


class AdditionalFieldsTokenView(TokenObtainPairView):
    serializer_class = AdditionalFieldsTokenSerializer
