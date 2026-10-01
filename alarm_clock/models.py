from dataclasses import dataclass
from datetime import time

@dataclass
class Alarm:
    id: int
    time: time
    active: bool = True