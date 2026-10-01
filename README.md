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

The application follows a simple layered architecture:

### Data Layer (`alarm_clock/models.py`)
- **Alarm**: Dataclass representing a single alarm with `id`, `time`, and `active` status
- Simple immutable data structure with no business logic

### Business Logic Layer (`alarm_clock/clock.py`)
- **AlarmClock**: Core class managing alarm lifecycle
  - `set_alarm()`: Creates and stores a new alarm
  - `list_alarms()`: Returns a copy of all alarms
  - `cancel_alarm()`: Deactivates an alarm by ID
  - `check_due_alarms()`: Checks which alarms should trigger at current time
- JSON persistence for alarm state (saved to `alarms.json`)
- Configurable storage (can disable persistence for testing)

### Presentation Layer (`alarm_clock/cli.py`)
- **CLI interface**: argparse-based command-line parser
- Commands: `set`, `list`, `cancel`, `run`
- Input validation with clear error messages
- User-friendly output formatting

### Entry Point (`alarm_clock/__main__.py`)
- Simple module entry point that delegates to CLI main function

### Design Decisions
- **No external dependencies**: Uses only Python standard library
- **JSON persistence**: Simple file-based storage (no database)
- **Single-threaded**: Blocking loop for simplicity
- **Testable**: Storage can be disabled for unit tests
- **Cross-platform**: Works on Windows, macOS, and Linux
