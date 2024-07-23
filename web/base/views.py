from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseView(APIView):
    serializer_class = None
    action_class = None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            res = self.action_class(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'results': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'results': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
