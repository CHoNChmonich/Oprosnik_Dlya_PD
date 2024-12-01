from django.shortcuts import render
from questions.models import Question, DirectionType


def test_view(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answers.all()
    related_directions = None
    if answers.first().recommend_direction:
        for answer in answers:
            related_directions = (answer, answer.recommend_direction)
    context = {
        'title': f'Вопрос №{question.number}',
        'question': question,
        'answers': answers,
        'related_directions': related_directions,
    }
    return render(request, 'questions/question_page.html', context)


def result_view(request, direction_id):
    direction = DirectionType.objects.get(id=direction_id)
    faculties = direction.faculties.all()
    context = {
        'title': 'Результат тестирования',
        'faculties': faculties,
        'direction': direction,
    }
    return render(request, 'questions/test_result.html', context)
