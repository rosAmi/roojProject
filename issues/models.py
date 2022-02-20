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

    def resolve(self):
        self.response = self.make_resolve()
        self.save()

    def make_resolve(self):
        s_num = self.serial[0:1]

        def state_num(state):
            i_sum = 0
            if self.indicator1 == state:
                i_sum += 1
            if self.indicator2 == state:
                i_sum += 1
            if self.indicator3 == state:
                i_sum += 1
            return i_sum

        if "24" in s_num:
            return "Please upgrade your device"
        if "36" in s_num:
            if state_num("off") == 3:
                return "Turn on the device"
            if state_num("blinking") > 1:
                return "Please wait"
            if state_num("on") == 3:
                return "All is ok"
        if "51" in s_num:
            if state_num("off") == 3:
                return "Turn on the device"
            if self.indicator1 == "blinking":
                return "Please wait"
            if state_num("on") > 0 and state_num("off") == (3 - state_num("on")):
                return "All is ok"

        def is_all_num():
            return all(i.isdigit() for i in self.serial)

        if is_all_num():
            return "Bad serial number"

        return "Unknown device"

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['uid']


        """
        # OLD LOGIC #
        
                def all_on():
                    return self.indicator1 == "on" and self.indicator2 == "on" and self.indicator3 == "on"

                def all_off():
                    return self.indicator1 == "off" and self.indicator2 == "off" and self.indicator3 == "off"

                def on_num():
                    on_n = 0
                    if self.indicator1 == "on":
                        on_n = on_n + 1
                    if self.indicator2 == "on":
                        on_n = on_n + 1
                    if self.indicator3 == "on":
                        on_n = on_n + 1
                    return on_n

                def off_num():
                    off_n = 0
                    if self.indicator1 == "off":
                        off_n = off_n + 1
                    if self.indicator2 == "off":
                        off_n = off_n + 1
                    if self.indicator3 == "off":
                        off_n = off_n + 1
                    return off_n

                def bl_num():
                    bl = 0
                    if self.indicator1 == "blinking":
                        bl = bl + 1
                    if self.indicator2 == "blinking":
                        bl = bl + 1
                    if self.indicator3 == "blinking":
                        bl = bl + 1
                    return bl
                    
        if "24" in s_num:
            return "Please upgrade your device"
        if "36" in s_num:
            if off_num() == 3:
                return "Turn on the device"
            if bl_num() > 1:
                return "Please wait"
            if on_num() == 3:
                return "All is ok"
        if "51" in s_num:
            if off_num() == 3:
                return "Turn on the device"
            if self.indicator1 == "blinking":
                return "Please wait"
            if on_num() > 0 and off_num() == 3 - on_num():
                return "All is ok"
        """
