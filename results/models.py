from django.db import models

class Result(models.Model):
    RollNo = models.IntegerField(primary_key=True) 
    student_name = models.CharField(max_length=100)
    marksofsub1 = models.IntegerField()
    marksofsub2 = models.IntegerField()
    marksofsub3 = models.IntegerField()
    marksofsub4 = models.IntegerField()

    @property
    def TotalMarks(self):
        return self.marksofsub1 + self.marksofsub2 + self.marksofsub3 + self.marksofsub4

    @property
    def Percentage(self):
        total_possible = 400  # or 100 per subject
        return round((self.TotalMarks / total_possible) * 100, 2)

    def __str__(self):
        return f"{self.RollNo} - {self.student_name} - {self.TotalMarks}"
