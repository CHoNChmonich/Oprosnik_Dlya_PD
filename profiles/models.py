from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255)
    admin_name = models.CharField(max_length=255, unique=True)
    minimum_score = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class DirectionType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='direction_type_images/', blank=True, null=True)


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    direction_type = models.ForeignKey(DirectionType, on_delete=models.CASCADE, related_name='faculties')


class Profile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.ManyToManyField(Subject, related_name='profiles')
    similar_profiles = models.ManyToManyField('self', blank=True, null=True, symmetrical=True)
    passing_score = models.PositiveIntegerField(default=0)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='profiles')

    def __str__(self):
        return f'{self.name} (Проходной балл: {self.passing_score}'

    def get_related_profiles(self):
        # Находим все профили c того же факультета
        related_profiles = Profile.objects.filter(faculty=self.faculty).exclude(id=self.id).distinct()
        return related_profiles


class ProfileSubjectMinScore(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='min_scores')
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='min_scores')
    score = models.PositiveIntegerField(default=0)


class ProfileImage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
