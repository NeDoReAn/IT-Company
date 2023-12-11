from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


class Developer(Customer, models.Model):
    pass


class Tester(Developer, models.Model):
    pass


class Database(models.Model):
    name = models.CharField(max_length=20)
    size = models.IntegerField()

    admin = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='databases')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_projects')

    developers = models.ManyToManyField(Developer, related_name='developer_projects')
    testers = models.ManyToManyField(Tester, related_name='tester_projects')

    database = models.OneToOneField(Database, on_delete=models.SET_NULL, related_name='project', null=True)

    def __str__(self):
        return self.name
