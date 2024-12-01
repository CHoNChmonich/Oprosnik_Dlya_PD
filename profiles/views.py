from django.shortcuts import render, get_object_or_404
from .models import Profile, Faculty, DirectionType
from django.shortcuts import render
from profiles.models import Profile, Subject, ProfileSubjectMinScore
from profiles.utils import filter_profiles_by_user_scores  # Импорт функции фильтрации


def filter_profiles(request):
    # Получаем выбранные предметы
    selected_subjects = request.GET.getlist('subjects', [])
    total_score = request.GET.get('total_score', '')

    # Проверяем, что пользователь выбрал ровно 3 предмета и ввел валидный балл
    if len(selected_subjects) == 3 and total_score.isdigit():
        total_score = int(total_score)
        # Создаем словарь с предметами и суммарным баллом
        user_scores = {subject: total_score // 3 for subject in selected_subjects}
        # Фильтруем профили
        profiles = filter_profiles_by_user_scores(user_scores)
    else:
        profiles = []

    # Все предметы ЕГЭ для отображения в фильтре
    subject_list = Subject.objects.all()

    return render(request, 'profiles/filter_results.html', {
        'profiles': profiles,
        'subject_list': subject_list,
        'selected_subjects': selected_subjects,
        'total_score': total_score,
    })


def direction_detail(request, direction_id):
    direction = DirectionType.objects.get(id=direction_id)
    faculties = direction.faculties.all()
    context = {
        'title': direction.name,
        'direction': direction,
        'faculties': faculties,
    }
    return render(request, 'profiles/direction.html', context)


def faculty_detail(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    profiles = faculty.profiles.all()
    context = {
        'title': faculty.name,
        'faculty': faculty,
        'profiles': profiles,
    }
    return render(request, 'profiles/faculty.html', context)


def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    subjects_dict={}
    subjects_min_score = ProfileSubjectMinScore.objects.filter(profile_id=profile).values('subject_id', 'score')
    min_scores_dict = {item['subject_id']: item['score'] for item in subjects_min_score}
    context = {
        'title': profile.name,
        'profile': profile,
        'min_scores_dict': min_scores_dict,
    }
    return render(request, 'profiles/profile.html', context)


def filter_profiles(request):
    # Получаем выбранные предметы
    selected_subjects = request.GET.getlist('subjects', [])
    total_score = request.GET.get('total_score', '')

    profiles = []
    # Проверяем, что выбрано ровно 3 предмета и введен валидный суммарный балл
    if len(selected_subjects) == 3 and total_score.isdigit():
        total_score = int(total_score)
        # Фильтруем профили на основе выбранных предметов и суммарного балла
        profiles = filter_profiles_by_user_scores(total_score, selected_subjects)

    # Загружаем все предметы для отображения в форме
    subject_list = Subject.objects.all()

    return render(request, 'profiles/filtered_profiles.html', {
        'profiles': profiles,
        'subject_list': subject_list,
        'selected_subjects': selected_subjects,
        'total_score': total_score,
    })

