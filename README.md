# Alarm Clock CLI

A simple Python CLI alarm clock application.

## Features

- Display current time continuously
- Set alarms for specific times (HH:MM format)
- List active alarms
- Cancel specific alarms
- Audio/visual alerts when alarm triggers
- Graceful shutdown with Ctrl+C

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
# Windows
.venv\Scripts\activate

# Unix/macOS
source .venv/bin/activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Run the alarm clock (interactive mode)
```bash
python -m alarm_clock
```

### Set an alarm
```bash
python -m alarm_clock set 07:30
```

### List active alarms
```bash
python -m alarm_clock list
```

### Cancel an alarm
```bash
python -m alarm_clock cancel 1
```

## Development

### Run tests
```bash
pytest
```

### Run with coverage
```bash
pytest --cov=alarm_clock
```

## Requirements

- Python 3.8+
- No external dependencies (uses standard library only)

## Architecture

- `alarm_clock/models.py`: Alarm and AlarmManager classes
- `alarm_clock/clock.py`: Time display and alarm checking logic
- `alarm_clock/cli.py`: Command-line interface using argparse
- `alarm_clock/__main__.py`: Entry point
