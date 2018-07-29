import datetime
from django.utils import timezone
from django.template.defaultfilters import date as _date
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required


class Event(models.Model):
    title = models.CharField('Heiti', max_length=140)
    location = models.CharField('Staðsetning', max_length=150)
    info = models.TextField()

    starts = models.DateTimeField('Hefst')
    ends = models.DateTimeField('Lýkur')

    arrive_when = models.DateTimeField('Mæting hvenær', null = True, blank = True)
    arrive_where = models.CharField('Mæting hvert', null = True, max_length = 150, blank = True)

    registration_starts = models.DateTimeField('Skráning hefst')
    registration_limit = models.IntegerField('Takmarka skráningu',
                                            default=0,
                                            choices=[(0, u"Engin takmörk")] + list(zip(range(1,100), range(1,100))))

    is_transportation = models.BooleanField('Rútur', default=False)

    #objects = EventGetManager() #veit ekki hvað þetta er. Eitthvað úr gömlu síðunni
    class Meta:
        verbose_name = "Viðburður"
        verbose_name_plural = "Viðburðir"
        ordering = ['-starts']



    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})

    def __str__(self):
        if self.starts.date() != self.ends.date():
            return u"%s, %s - %s" % (self.title,
                            self.starts.strftime("%a %H:%M"),
                            self.ends.strftime("%a %H:%M"))
        else:
            return u"%s, %s - %s" % (self.title,
                            self.starts.strftime("%H:%M"),
                            self.ends.strftime("%H:%M"))


    def add_user_to_list_of_attendees(self, user):
        if not user.is_authenticated():
            return
        registration = EventRegistration.objects.create(user = user, event = self,
                                                        time_registered = timezone.now())

    def remove_user_from_list_of_attendees(self, user):
        if not user.is_authenticated():
            return
        registration = EventRegistration.objects.get(user = user, event = self)
        registration.delete()

    def add_user_to_list_of_transportation(self, user):
        if user.is_authenticated() and self.is_transportation:
            registration = EventRegistration.objects.get(user = user, event = self)
            registration.using_transportation = True
            registration.save()

    def remove_user_from_list_of_transportation(self, user):
        if user.is_authenticated() and self.is_transportation:
            registration = EventRegistration.objects.get(user = user, event = self)
            registration.using_transportation = False
            registration.save()


    def get_registrations(self):
        return EventRegistration.objects.filter(event = self)
    def get_registrated_users(self):
        return [r.user for r in self.get_registrations()]

    def get_attending_registrations(self): 
        attending_users = self.get_registrations()
        if self.has_registration_limit():
            return attending_users[:min(self.registration_limit, len(attending_users))]
        else:
            return attending_users

    def user_is_attending(self, user):
        return self.get_registrations().filter(user=user).count()==1

    def get_transportation_list(self): 
        reg = EventRegistration.objects.filter(event = self, using_transportation=True)
        bus = [r.user for r in reg]
        return bus
    
    def has_registration_limit(self):
        return self.registration_limit > 0

    def get_waiting_list(self):
        attending_users = self.get_registrations()
        return attending_users[self.registration_limit:]





class EventRegistration(models.Model):
    event = models.ForeignKey(Event,verbose_name='Viðburður')
    user = models.ForeignKey(User,verbose_name='Notandi')
    time_registered = models.DateTimeField()
    using_transportation = models.BooleanField('Rútur', default=False)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.event.title)

    class Meta:
        verbose_name = 'Skráning á viðburð'
        verbose_name_plural = 'Skráningar á viðburði'
        ordering = ['time_registered', ]
        unique_together = ('event', 'user')

    def save(self, *args, **kwargs):
        if self.id is None and self.time_registered is None:
            self.time_registered = datetime.datetime.now()
        super(EventRegistration, self).save(*args, **kwargs)

    def time_registered_format(self):
        return _date(self.time_registered,"d. F, H:i:s")
