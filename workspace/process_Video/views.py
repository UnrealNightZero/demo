from django.shortcuts import render
from django.http import HttpResponse

import base64
import io
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from PIL import Image
import cv2
import json

# Create your views here.

@require_POST
@csrf_exempt
def processImage(request):
    image_data = json.loads(request.body)
    test = image_data.get('imageData')
    print(test)
    image_bytes = base64.b64decode(test.split(',')[1])

    image = Image.open(io.BytesIO(image_bytes))
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    buffered = io.BytesIO()
    Image.fromarray(gray_image).save(buffered, format="JPEG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return JsonResponse({'imageData': 'data:image/jpeg;base64,' + encoded_image})