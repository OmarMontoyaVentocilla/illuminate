from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'buscador/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'buscador/detail.html', {'question': question})