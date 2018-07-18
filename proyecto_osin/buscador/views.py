from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from zeep import Client
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your views here.
def list_people(request):
    return render(request,'buscador.html')
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'buscador/index.html', context)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'buscador/detail.html', {'question': question})
def wseervice(request):
    client = Client('http://www.soapclient.com/xml/soapresponder.wsdl')
    result = client.service.Method1('Zeep', 'is cool')
    data={
        'result':result
    }
    return JsonResponse(data) 