from django.db import models

import logging

logger = logging.getLogger('root.' + __name__)

class SiteTrafficTracker(models.Model):
    total_visited = models.IntegerField(default=0)
    num_splash_click = models.IntegerField(default=0)

    def increment_visited(self):
        self.total_visited+=1

    def increment_splash(self):
        self.num_splash_click+=1

'''
class UserList(models.Model):
    user = models.ForeignKey(Profile, null=False)
    list_name = models.CharField(max_length=30)
    can_delete = models.BooleanField(null=False, default=True)

    @staticmethod
    def create_default_lists(user):
        logger.info("Creating default user lists for user %s", user)
        watched = UserList(user=user, list_name='Watched', can_delete=False)
        watched.save()
        planning = UserList(user=user, list_name='Planning to Watch', can_delete=False)
        planning.save()

    def __str__(self):
        return "".join([str(self.user), ":", str(self.list_name)])


class UserListItem(models.Model):
    user_list = models.ForeignKey(UserList, null=False)
    movie = models.ForeignKey(Movie, null=False)
    rating = models.ForeignKey(Rating, null=False)

    def __str__(self):
        return "".join([str(self.movie), " {", str(self.user_list), "}"])

'''

