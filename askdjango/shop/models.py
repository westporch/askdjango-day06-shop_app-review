from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

def min_length_5_validator(value):
    if len(value) < 5:
        raise ValidationError('제품명을 다섯글자 이상 입력해주세요.')

class Item(models.Model):
    name = models.CharField(max_length=100,
        validators=[min_length_5_validator],
        help_text='제조사 및 모델명을 작성해주세요.')
    price = models.PositiveIntegerField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.id])