from datetime import time
from alarm_clock.models import Alarm

def test_alarm_defaults_to_active():
    alarm = Alarm(id=1, time=time(14, 30))
    assert alarm.id == 1
    assert alarm.time == time(14, 30)
    assert alarm.active is True