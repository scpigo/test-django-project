from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    ACTIVE = 'active'
    COMPLETED = 'completed'

    STATUSES = {
        ACTIVE: "Активен",
        COMPLETED: "Завершён",
    }

    title = models.CharField('Название', max_length=255)
    body = models.TextField('Текст')
    status = models.CharField('Статус',
        max_length=10,
        choices=STATUSES,
        default=ACTIVE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    parent_note = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='child_notes' )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'