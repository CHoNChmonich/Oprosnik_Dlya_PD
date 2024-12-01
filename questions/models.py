from django.db import models
from profiles.models import DirectionType


class Question(models.Model):
    is_first_question = models.BooleanField(default=False)
    number = models.PositiveIntegerField(default=0)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Вопрос под номером {self.number}: {self.body}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.TextField(max_length=255)
    next_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name="previous_answers")
    recommend_direction = models.ForeignKey(DirectionType, on_delete=models.SET_NULL, null=True, blank=True,
                                            related_name='related_answers')

    def __str__(self):
        return f'Ответ на вопрос {self.question} - {self.text}'
