from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50, verbose_name="Client Address")
    # verbose_name="Client Address" -> es Con el nombre quye los veremos desde el panel de admin
    email = models.EmailField(blank=True, null=True)
    tlf = models.CharField(max_length=10, verbose_name="Phone number")
    def __str__(self):
        return 'Cliente name: %s. Email: %s. Phone number: %s ' %(self.name, self.email, self.tlf)


class Article(models.Model):
    article_name = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return 'Article name: %s. Section: %s. Price: %s' %(self.article_name, self.section, self.price)
    

class Order(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()

    def __str__(self):
        return 'Order number: %s.' %(self.number)
    
