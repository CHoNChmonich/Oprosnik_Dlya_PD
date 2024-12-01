from django.shortcuts import render
from questions.models import Question
from profiles.models import DirectionType
from profiles.models import Subject


def index_view(request):
    first_question = Question.objects.get(is_first_question=True)
    directions = DirectionType.objects.all()
    subjects_list = Subject.objects.all()
    return render(request, 'main/index.html',
                  context={'title': 'Главная страница', 'first_question': first_question, 'directions': directions,
                           'subject_list': subjects_list, })
