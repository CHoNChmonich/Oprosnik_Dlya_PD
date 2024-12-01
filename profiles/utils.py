from profiles.models import Profile, Subject

def filter_profiles_by_user_scores(total_score, selected_subjects):
    """
    Фильтрует профили на основе суммарного балла и выбранных предметов.

    total_score: int
        Суммарный балл, введенный пользователем.

    selected_subjects: list
        Список выбранных пользователем предметов.

    Returns:
        QuerySet с подходящими профилями.
    """
    # Находим профили, у которых есть ровно три требуемых предмета
    eligible_profiles = Profile.objects.filter(subjects__name__in=selected_subjects).distinct()

    matching_profiles = []
    for profile in eligible_profiles:
        # Получаем предметы профиля, совпадающие с выбранными пользователем
        profile_subjects = profile.subjects.filter(name__in=selected_subjects)

        # Проверяем, что у профиля ровно три совпадающих предмета
        if profile_subjects.count() == 3:
            # Сравниваем суммарный балл пользователя с проходным баллом профиля
            if total_score >= profile.passing_score:
                matching_profiles.append(profile)

    return matching_profiles
