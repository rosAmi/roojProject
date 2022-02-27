from django.db import models

# import datetime
# now = datetime.datetime.now()


class Issue(models.Model):
    Indicator_Status = (
        ('off', 'Off'),
        ('on', 'On'),
        ('blinking', 'Blinking')
    )

    uid = models.PositiveIntegerField()
    description = models.CharField(max_length=140)
    serial = models.CharField(max_length=64)
    indicator1 = models.CharField(max_length=8, choices=Indicator_Status, default='off')
    indicator2 = models.CharField(max_length=8, choices=Indicator_Status, default='off')
    indicator3 = models.CharField(max_length=8, choices=Indicator_Status, default='off')
    date_time = models.DateTimeField(auto_now_add=True)
    response = models.CharField(max_length=140, blank=True)

    def save(self, *args, **kwargs):
        self.response = self.make_resolve()
        super().save(*args, **kwargs)

    def make_resolve(self):
        serial_num = self.serial[0:2]

        def state_num(state):
            i_sum = 0
            if self.indicator1 == state:
                i_sum += 1
            if self.indicator2 == state:
                i_sum += 1
            if self.indicator3 == state:
                i_sum += 1
            return i_sum

            #  check  if all serial digits are numbers
        if all(i.isdigit() for i in self.serial):
            return "Bad serial number"

        if "24" == serial_num:
            return "Please upgrade your device"
        if "36" == serial_num:
            if state_num("off") == 3:
                return "Turn on the device"
            if state_num("blinking") > 1:
                return "Please wait"
            if state_num("on") == 3:
                return "All is ok"
            return "Serial 36, unknown resolve"
        if '51' == serial_num:
            if state_num("off") == 3:
                return "Turn on the device"
            if self.indicator1 == "blinking":
                return "Please wait"
            if state_num("on") > 0 and state_num("off") == (3 - state_num("on")):
                return "All is ok"
            return "Serial 51, unknown resolve"

        else:
            return "Unknown device"

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['uid']

