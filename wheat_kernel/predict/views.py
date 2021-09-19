from .apps import PredictConfig
from django.shortcuts import render,redirect
import numpy as np
from django.contrib import messages
import logging

# Create the loggers object
logger = logging.getLogger('django')

# Create your views here.
def predict_kernel(request):
    if request.method == 'GET':
        logger.info('Web Page Accessed')
        return render(request, 'index.html')

    if request.method == 'POST':
        wheat_data = {x: request.POST.get(x) for x in request.POST.keys()}
        wheat_data.pop('csrfmiddlewaretoken')
        # Get values from dictionary and insert into list
        x = []
        for item in wheat_data.values():
            x.append(float(item))
        # Compute compactness and insert at index 2
        c = (4 * 3.14 * x[0]) / (x[1] ** 2)
        x.insert(2, c)
        # convert into numpy array and make predictions
        x = np.array(x).reshape(1, -1)
        model = PredictConfig.model
        prediction = model.predict(x)[0]
        # On basis of output save response
        if prediction == 0:
            response = "The Wheat Kernel is Kama"
        elif prediction == 1:
            response = "The Wheat Kernel is Rosa"
        elif prediction == 2:
            response = "The Wheat Kernel is Canadian"
        # return the response using message library and save actions into log file
        messages.success(request, response)
        logger.info('Data posted to make predictions')

        return redirect('index.html')