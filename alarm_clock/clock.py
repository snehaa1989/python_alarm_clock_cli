import json
import os
from datetime import time
from alarm_clock.models import Alarm

ALARMS_FILE = "alarms.json"

class AlarmClock:
    def __init__(self, storage_file: str | None = ALARMS_FILE):
        self.storage_file = storage_file
        self.alarms: list[Alarm] = []
        self._next_id = 1
        if storage_file:
            self._load()
    
    def _load(self):
        if not self.storage_file:
            return
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.alarms = [
                        Alarm(
                            id=a['id'],
                            time=time.fromisoformat(a['time']),
                            active=a['active']
                        )
                        for a in data.get('alarms', [])
                    ]
                    self._next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, KeyError, ValueError):
                # If file is corrupted, start fresh
                self.alarms = []
                self._next_id = 1
    
    def _save(self):
        if not self.storage_file:
            return
        data = {
            'alarms': [
                {
                    'id': alarm.id,
                    'time': alarm.time.isoformat(),
                    'active': alarm.active
                }
                for alarm in self.alarms
            ],
            'next_id': self._next_id
        }
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def set_alarm(self, alarm_time: time) -> Alarm:
        alarm = Alarm(id=self._next_id, time=alarm_time)
        self.alarms.append(alarm)
        self._next_id += 1
        self._save()
        return alarm

    def list_alarms(self) -> list[Alarm]:
        return self.alarms.copy()

    def cancel_alarm(self, alarm_id: int) -> bool:
        for alarm in self.alarms:
            if alarm.id == alarm_id and alarm.active:
                alarm.active = False
                self._save()
                return True
        return False

    def check_due_alarms(self, current_time : time) -> list[Alarm]:
        triggered = []
        for alarm in self.alarms:
            if alarm.active and alarm.time <= current_time:
                alarm.active = False
                triggered.append(alarm)
        if triggered:
            self._save()
        return triggered