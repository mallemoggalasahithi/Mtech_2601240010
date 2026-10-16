from dataclasses import dataclass
from datetime import datetime


@dataclass
class ForensicEvent:
    timestamp: datetime
    source: str
    event_type: str
    user: str
    description: str
    severity: str