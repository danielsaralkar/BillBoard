from django.shortcuts import render
from django.utils import timezone
from mainbillboard.models import Messages
import json

# Create your views here.
def get_data(request):
    myresult = Messages.object.all()
    return render(request, 'index.html', {'comments': myresult})

def add_post(request):
    new_row = Messages()
    return json.dumps({"STATUS":"SUCCESS"})