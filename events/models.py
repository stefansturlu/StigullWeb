import datetime
from django.utils import timezone
from django.template.defaultfilters import date as _date
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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

    #is_transportation = models.BooleanField('Rútur', default=False)

    #objects = EventGetManager() #veit ekki hvað þetta er.
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
        registration = EventRegistration.objects.create(user = user,
                                                        event = self,
                                                        time_registered = timezone.now())

    def remove_user_from_list_of_attendees(self, user):
        registration = EventRegistration.objects.get(user = user, event = self)
        registration.delete()

    def get_registrations(self):
        return EventRegistration.objects.filter(event = self)

    def get_attending_users(self):
        attending_users = [r.user for r in self.get_registrations()]
        return attending_users






class EventRegistration(models.Model):
    event = models.ForeignKey(Event,verbose_name='Viðburður')
    user = models.ForeignKey(User,verbose_name='Notandi')
    time_registered = models.DateTimeField()
    #using_transportation = models.BooleanField('Rútur', default=False)

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
