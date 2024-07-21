from django.contrib.auth.models import User
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering=('name',) #this is like order by , by alpabhet arrange kiya
        verbose_name_plural='Categories'

    #below function is because in admin page it shows categories created as object1,object2 and not the names so to show names we are doing it 

    def __str__(self):
        return self.name
    
class Samasya(models.Model):
    category=models.ForeignKey(Category, related_name='samasyas',on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    time=models.FloatField()
    image=models.ImageField(upload_to='samaya_images',blank=True,null=True) # for images i installed pillows 
    is_solved=models.BooleanField(default=False)
    submitted_by=models.ForeignKey(User, related_name='samasyas', on_delete=models.CASCADE)
    submitted_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',) #this is like order by , by alpabhet arrange kiya
        verbose_name_plural='Samasya'
    def __str__(self):
        return self.name