from datetime import time
from alarm_clock.models import Alarm
from alarm_clock.clock import AlarmClock
def test_alarm_defaults_to_active():
    alarm = Alarm(id=1, time=time(14, 30))
    assert alarm.id == 1
    assert alarm.time == time(14, 30)
    assert alarm.active is True

def test_alarm_clock_initial_state():
    clock = AlarmClock(storage_file=None)
    assert clock.alarms == []
    assert clock._next_id == 1

def test_set_alarm_returns_alarm_with_id():
    clock = AlarmClock(storage_file=None)
    alarm = clock.set_alarm(time(8, 0))
    assert alarm.id == 1
    assert alarm.time == time(8, 0)
    assert alarm.active is True

def test_list_alarms_returns_copy():
    clock = AlarmClock(storage_file=None)
    alarm = clock.set_alarm(time(8, 0))
    alarms = clock.list_alarms()
    assert alarms == [alarm]
    # Modifying the list shouldn't affect internal state
    alarms.append(Alarm(id=2, time=time(9, 0)))
    assert clock.list_alarms() == [alarm]

def test_cancel_alarm_deactivates_alarm():
    clock = AlarmClock(storage_file=None)
    alarm = clock.set_alarm(time(8, 0))
    assert clock.cancel_alarm(1) is True
    assert alarm.active is False

def test_cancel_nonexistent_alarm_returns_false():
    clock = AlarmClock(storage_file=None)
    assert clock.cancel_alarm(999) is False

def test_check_due_alarms_returns_empty_list_when_no_alarms():
    clock = AlarmClock(storage_file=None)
    assert clock.check_due_alarms(time(8, 0)) == []

def test_check_due_alarms_returns_triggered_alarms():
    clock = AlarmClock(storage_file=None)
    alarm1 = clock.set_alarm(time(8, 0))
    alarm2 = clock.set_alarm(time(9, 0))
    triggered = clock.check_due_alarms(time(8, 30))
    assert triggered == [alarm1]
    assert alarm1.active is False
    assert alarm2.active is True

def test_check_due_alarms_does_not_trigger_inactive_alarms():
    clock = AlarmClock(storage_file=None)
    alarm = clock.set_alarm(time(8, 0))
    alarm.active = False
    assert clock.check_due_alarms(time(8, 30)) == []
    assert alarm.active is False

def test_check_due_alarms_only_triggers_alarms_at_or_before_time():
    clock = AlarmClock(storage_file=None)
    alarm1 = clock.set_alarm(time(8, 0))
    alarm2 = clock.set_alarm(time(9, 0))
    triggered = clock.check_due_alarms(time(8, 0))
    assert triggered == [alarm1]
    assert alarm1.active is False
    assert alarm2.active is True

