from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=180)
    born_at = models.DateField('born at', null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self) -> str:
        return self.name


class Grade(models.Model):
    foreign_key: int = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject: str = models.CharField(max_length=80)
    grade_one: float = models.FloatField(default=0.0)
    grade_two: float = models.FloatField(default=0.0)
    grade_three: float = models.FloatField(default=0.0)
    grade_four: float = models.FloatField(default=0.0)
    sum: float = models.FloatField(default=0.0)
    average: float = models.FloatField(default=0.0)

    def calculate_average(self) -> float:
        self.average = round((self.grade_one + self.grade_two + self.grade_three + self.grade_four) / 4, 2)
        return self.average
    
    
    def total_sum(self) -> float:
        self.sum = (self.grade_one + self.grade_two + self.grade_three + self.grade_four)
        return self.sum
    
    
    def traits(self):
        traits_list = [
            self.subject,
            self.grade_one,
            self.grade_two,
            self.grade_three,
            self.grade_four,
            self.average
        ]
        return traits_list
    

    def __str__(self) -> str:
        traits: str = ""
        traits_list = [
            self.subject,
            self.grade_one,
            self.grade_two,
            self.grade_three,
            self.grade_four,
            self.average
        ]
        for i in range(len(traits_list)):
            if i == 0:
                traits += (str(traits_list[i]))
            else:
                traits += ", " + (str(traits_list[i]))
        return traits
