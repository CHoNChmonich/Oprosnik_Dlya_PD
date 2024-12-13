from django.shortcuts import render

from profiles.models import Profile
from questions.models import Question


def test_view(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answers.all()
    # related_directions = None
    # if answers.first().recommend_profile:
    #     for answer in answers:
    #         related_profile = (answer, answer.recommend_profile)
    context = {
        'title': f'Вопрос №{question.number}',
        'question': question,
        'answers': answers,
        # 'related_profile': related_profile,
    }
    return render(request, 'questions/question_page.html', context)


def result_view(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {
        'title': 'Результат тестирования',
        'profile': profile,

    }
    return render(request, 'questions/test_result.html', context)
