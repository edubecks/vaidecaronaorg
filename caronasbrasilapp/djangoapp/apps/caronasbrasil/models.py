from django.db import models

# Create your models here.
class CaronaModel(models.Model):
    fb_post_id = models.CharField(max_length=40)
    fb_group_id = models.CharField(max_length=20)
    fb_content = models.CharField(max_length=1001)
    fb_user_id = models.CharField(max_length=20)
    fb_creation_date = models.DateTimeField(auto_now=False)
    ## Ex: "sao carlos/SP"
    origin = models.CharField(max_length=33)
    destiny = models.CharField(max_length=33)
    from_datetime = models.DateTimeField(auto_now=False)
    to_datetime = models.DateTimeField(auto_now=False)
    ofereco_procuro = models.CharField(max_length=1) ## o: ofereco, p: procuro
    num_vagas = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return 'https://www.facebook.com/groups/'+self.fb_group_id+'/permalink/'+\
               self.fb_post_id[self.fb_post_id.index('_')+1:]+'/'

    def get_contact_user(self):
        return 'https://www.facebook.com/messages/'+self.fb_user_id

    def get_more_info(self):
        return '/caronas/'+str(self.id)


class CaronaGroupModel(models.Model):
    fb_group_id = models.CharField(max_length=20)
    city1 = models.CharField(max_length=30)
    city1_state = models.CharField(max_length=2)
    city1_list = models.CharField(max_length=200)
    city2 = models.CharField(max_length=30)
    city2_state = models.CharField(max_length=2)
    city2_list = models.CharField(max_length=200)


class ParserErrorsModel(models.Model):
    fb_group_id = models.CharField(max_length=20)
    fb_post_id = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)