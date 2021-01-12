from django.db import models
from django.contrib.auth.models import AbstractUser

class Player(AbstractUser):
    email = models.EmailField(unique=True)
    participate = models.BooleanField(default=False)
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def exists(email):
        """
        Check exists other player in de data base
        :param email:
        :return:
        """
        #Get player's list
        players = Player.objects.filter(email=email).count()

        return True if players>0 else False