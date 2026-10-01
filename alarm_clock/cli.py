import argparse
from datetime import datetime
from alarm_clock.clock import AlarmClock
import time as time_module

def parse_time(value: str):
    try:
        return datetime.strptime(value, "%H:%M").time()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid time format: {value}. Use HH:MM")

def build_parser():
    parser = argparse.ArgumentParser(prog="alarm-clock", description="Alarm Clock CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    set_parser = subparsers.add_parser("set", help="Set an alarm")
    set_parser.add_argument("time", type=parse_time, help="Alarm time in HH:MM format")
    subparsers.add_parser("list", help="List all alarms")
    cancel_parser = subparsers.add_parser("cancel", help="Cancel an alarm")
    cancel_parser.add_argument("alarm_id", type=int, help="Alarm ID to cancel")
    subparsers.add_parser("run", help="Run the alarm clock")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    
    if args.command == "set":
        alarm_clock = AlarmClock()
        alarm = alarm_clock.set_alarm(args.time)
        print(f"Alarm set for {alarm.time.strftime('%H:%M')} (ID: {alarm.id})")
    elif args.command == "list":
        alarm_clock = AlarmClock()
        alarms = alarm_clock.list_alarms()
        if not alarms:
            print("No alarms set.")
        else:
            for alarm in alarms:
                status = "active" if alarm.active else "cancelled"
                print(f"ID: {alarm.id} | Time: {alarm.time.strftime('%H:%M')} | Status: {status}")
    elif args.command == "cancel":
        alarm_clock = AlarmClock()
        if alarm_clock.cancel_alarm(args.alarm_id):
            print(f"Alarm {args.alarm_id} cancelled.")
        else:
            print(f"Alarm {args.alarm_id} not found or already cancelled.")
    elif args.command == "run":
        alarm_clock = AlarmClock()
        run_clock(alarm_clock)

def run_clock(clock : AlarmClock):
    print("Alarm Clock running. Press Ctrl+C to stop.")
    try:
        while True:
            current_time = datetime.now().time().replace(second = 0, microsecond = 0)
            triggered = clock.check_due_alarms(current_time)
            for alarm in triggered:
                print(f"Alarm triggered: {alarm}")
            time_module.sleep(1) # Check every second
    except KeyboardInterrupt:
        print("Alarm Clock stopped.")
