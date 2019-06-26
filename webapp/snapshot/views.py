import base64
import uuid
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def main(request):
    return render(request, 'main.html')


@api_view(['POST'])
def upload(request):
    if request.method == 'POST':
        data = request.data.get('snapshot')
        encoded_data = data.split(',')[1]
        decoded_data = base64.b64decode(encoded_data)
        filename = str(uuid.uuid4()) + '.png'
        fd = open(filename, 'wb')
        fd.write(decoded_data)
        fd.close()
    return Response({'filename': filename},
                    status=status.HTTP_201_CREATED)
