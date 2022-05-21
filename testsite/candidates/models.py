from django.db import models


class Skill(models.Model):
    """Модель навыка"""
    name = models.CharField(max_length=20, verbose_name='навык', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Навыки'
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Language(models.Model):
    """Модель языка"""
    name = models.CharField(max_length=30, verbose_name='язык', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Языки'
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Hobby(models.Model):
    """Модель хобби"""
    name = models.CharField(max_length=30, verbose_name='Хобби', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Хобби'
        verbose_name = 'Хобби'
        verbose_name_plural = 'Хобби'


class Candidate(models.Model):
    """Модель кандидата"""
    name = models.CharField(max_length=20, verbose_name='Имя', null=True, blank=True)
    surname = models.CharField(max_length=20, verbose_name='Фамилия', null=True, blank=True)
    lastname = models.CharField(max_length=20, verbose_name='Отчество', null=True, blank=True)
    language = models.ManyToManyField(Language, verbose_name='Язык', null=True, blank=True)
    skill = models.ManyToManyField(Skill, verbose_name='Навык', null=True, blank=True)
    hobby = models.ManyToManyField(Hobby, verbose_name='Навык', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Кандидат'
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
