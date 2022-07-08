from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=180)
    born_at = models.DateTimeField('born at', null=True, blank=True)
    phone_number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Grade(models.Model):
    foreign_key: int = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject: str = models.CharField(max_length=80)
    grade_one: float = models.FloatField(default=0.0)
    grade_two: float = models.FloatField(default=0.0)
    grade_three: float = models.FloatField(default=0.0)
    average: float = models.FloatField(default=0.0)

    def calculate_average(self) -> float:
        self.average = (self.grade_one + self.grade_two + self.grade_three) / 3
        return self.average

    def __str__(self) -> str:
        traits: str = ""
        traits_list = [
            self.subject,
            self.grade_one,
            self.grade_two,
            self.grade_three,
            self.average
        ]
        for i in range(len(traits_list)):
            if i == 0:
                traits += (str(traits_list[i]))
            else:
                traits += ", " + (str(traits_list[i]))
        return traits
