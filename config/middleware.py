from datetime import timedelta
from random import randint, shuffle

from django.utils.timezone import now

from positive_affirmation.users.models import User, Affirmation, Encouragement


class SimulateSocial(object):
    def process_request(self, request):
        if not request.user.is_authenticated() or request.user.control:
            return
        for a in Affirmation.objects.filter(user=request.user).all():
            if a.simulated:
                continue
            encouragements = Encouragement.objects.filter(affirmation=a).all()
            if len(encouragements):
                continue
            if a.created > now() - timedelta(minutes=20):
                continue
            for i in range(0, randint(0, 3)):
                users = [u for u in User.objects.filter(control=False).all()
                         if u != request.user]
                shuffle(users)
                Encouragement.objects.create(affirmation=a, encourager=users[i])
            a.simulated = True
            a.save()
