from django.db import models


# Create your models here.
# Create your models here.
class protrainyModel(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_branch = models.CharField(max_length=5)
    user_password = models.CharField(max_length=10)
    user_type=models.CharField(max_length=50)
    verify=models.CharField(max_length=50)

    def __str__(self):
        return "name={0},user_name={1},user_branch={2},user_password={3},user_type={4},verify={5}".format(self.name, self.user_name,
                                                                                 self.user_branch, self.user_password,self.user_type,self.verify)
