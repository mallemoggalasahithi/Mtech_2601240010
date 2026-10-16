import csv
import json

from src.exporters import export_to_csv, export_to_json
from src.timeline import get_all_events


def get_test_events():
    log_files = [
        "data/system.log",
        "data/application.log",
        "data/browser.log",
        "data/auth.log",
    ]

    return get_all_events(log_files)


def test_export_to_csv(tmp_path):
    events = get_test_events()
    output_file = tmp_path / "timeline.csv"

    export_to_csv(events, output_file)

    assert output_file.exists()

    with open(output_file, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    assert len(rows) == 33
    assert rows[0][0] == "Timestamp"
    assert rows[0][1] == "Source"


def test_export_to_json(tmp_path):
    events = get_test_events()
    output_file = tmp_path / "timeline.json"

    export_to_json(events, output_file)

    assert output_file.exists()

    with open(output_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 32
    assert "timestamp" in data[0]
    assert "source" in data[0]
    assert "severity" in data[0]