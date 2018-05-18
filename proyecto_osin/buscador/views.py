from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def list_people(request):
    return render(request,'buscador.html')
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'buscador/index.html', context)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'buscador/detail.html', {'question': question})
