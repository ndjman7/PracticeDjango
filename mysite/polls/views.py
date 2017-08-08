from django.shortcuts import get_object_or_404, render
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()[:5]
    return render(request, 'polls/index.html', {'latest_question_list' : latest_question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
