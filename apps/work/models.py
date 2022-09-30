from django.db import models
from apps.company.models import Background


class Category(models.Model):
    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "1.1. Categories"

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Work(models.Model):
    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "1.0. Work"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='work/images')
    background = models.ForeignKey(Background, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Visa(models.Model):
    class Meta:
        verbose_name = "Visas"
        verbose_name_plural = "1.2. Visas"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    background = models.ForeignKey(Background, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='work/visa/images/')
    background_image = models.ImageField(upload_to='work/backgrounds/')
    description = models.TextField()
    is_active = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobType(models.Model):
    class Meta:
        verbose_name = "Job types"
        verbose_name_plural = "2.0. Jop types"

    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='work/jobs/icons', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProgrammingLanguages(models.Model):
    class Meta:
        verbose_name = "Programming Languages"
        verbose_name_plural = "2.1. Programming Languages"

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Specialty(models.Model):
    class Meta:
        verbose_name = "Specialties"
        verbose_name_plural = "2.2. Specialties"

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Framework(models.Model):
    class Meta:
        verbose_name = "Frameworks"
        verbose_name_plural = "2.3. Frameworks"

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ExpertiseLevel(models.Model):
    class Meta:
        verbose_name = "Expertise Levels"
        verbose_name_plural = "2.4. Expertise Levels"

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class WorkingConditionAndBenefit(models.Model):
    class Meta:
        verbose_name = "Working Conditions and Benefits"
        verbose_name_plural = "2.5. Working Conditions and Benefits"

    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    class Meta:
        verbose_name = "Jobs"
        verbose_name_plural = "2.6. Jobs"

    title = models.CharField(max_length=300)
    salary = models.CharField(max_length=100, help_text='For example ($2500 - 3000 / month)')
    industry = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    jop_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True, related_name='jop_type')
    speciality = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, related_name='speciality')
    programming_language = models.ForeignKey(ProgrammingLanguages, on_delete=models.SET_NULL, null=True,
                                             related_name='programming_language')
    frameworks = models.ManyToManyField(Framework, related_name='frameworks')
    expertise_level = models.ForeignKey(ExpertiseLevel, on_delete=models.SET_NULL, null=True,
                                        related_name='expertise_level')
    working_conditions_and_benefits = models.ManyToManyField(WorkingConditionAndBenefit,
                                                             related_name='working_conditions_and_benefits')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}  at {self.industry}'
