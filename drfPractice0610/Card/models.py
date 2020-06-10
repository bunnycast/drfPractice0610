from django.db import models


class Cards(models.Model):
    cardname = models.CharField(max_length=64, verbose_name="카드이름")
    cardnos = models.IntegerField(verbose_name="카드번호")
    validity = models.DateField(auto_now_add=False, verbose_name="유효기한")

    class Meta:
        ordering = ['cardname']
        verbose_name = 'Card'
        verbose_name_plural = 'Card'
