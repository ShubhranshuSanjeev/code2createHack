from django.shortcuts import render
# from .models import DustStats
from urllib.request import urlopen
from django.views.generic import TemplateView
import json
# Create your views here.

def index(request):
    return render(request, 'base.html')

class DustbinSatsView(TemplateView):
    template_name = 'dustbinStats.html'

    def get_context_data(self, **kwargs):
        READ_API_KEY = 'AP6S7R81XD7O3T75'
        CHANNEL_ID = '1012728'

        # connection = urlopen("https://api.thingspeak.com/channels/1012728/fields/1.json?api_key=H9BQPH7KALTEPO3A&results=270")
        # connection1 = urlopen("https://api.thingspeak.com/channels/1012728/status.json?api_key=H9BQPH7KALTEPO3A")
        # response = connection.read()
        # response1 = connection1.read()
        # data = json.loads(response1)
        # print(data['feeds'][-1]['entry_id'])
        context = super().get_context_data(**kwargs)
        context['filled'] = 78 
        # context['field1'] = 0 if not data['field1'] else data['field1']
        # context['field2'] = 0 if not data['field2'] else data['field2']
        # context['field3'] = 0 if not data['field3'] else data['field3']
        
        return context

