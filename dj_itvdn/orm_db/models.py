from django.db import models

# Create your models here.
class Human(models.Model):
    CHOICE_COMPANY = (
        ('google', 'Google'),
        ('yandex', 'Yandex'),
        ('itvdn', 'Itvdn'),
        ('epam', 'Epam'),
    )

    POSITION_COICES = (
        ('senior', 'Senior'),
        ('middle', 'Middle'),
        ('junior', 'Junior'),
    )

    PYTHON = 'py'
    JS = 'js'
    CS = 'c#'
    CPP = 'cpp'

    LANGUAGE_COICES = (
        (PYTHON, 'Python'),
        (JS, 'Javascript'),
        (CS, 'C#'),
        (CPP, 'C++'),
    )

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    birth = models.DateField(auto_now_add=False, auto_now=False)
    company = models.CharField(max_length=150, choices=CHOICE_COMPANY)
    position = models.CharField(max_length=15, choices=POSITION_COICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_COICES, default=PYTHON)
    salary = models.IntegerField()

    def __str__(self):
        return 'Имя: {0}, Фамилия: {1}, Компания: {2}'.format(self.name, self.surname, self.company)

    def dict(self):
        obj = {
            'name': self.name,
            'surname': self.surname,
            'birth': self.birth,
            'company': self.company,
            'position': self.position,
            'language': self.language,
            'salary': self.salary,
        }
        return obj
