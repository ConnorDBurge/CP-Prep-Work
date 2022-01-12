from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def get_question(guestion_id):
    return Question.objects.get(id=guestion_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', data)


def detail(request, question_id):
    question = get_question(question_id)
    data = {'question': question}
    return render(request, 'polls/detail.html', data)


def results(request, question_id):
    question = get_question(question_id)
    data = {'question': question}
    return render(request, 'polls/results.html', data)


def vote(request, question_id):
    question = get_question(question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
