from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
<<<<<<< HEAD
        return self.email
=======
        return self.email
>>>>>>> 14e5e8f (Final adjustment - Code cleanup, merged group work, adjusted details)
