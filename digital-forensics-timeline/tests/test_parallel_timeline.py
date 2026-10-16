from src.timeline import build_parallel_timeline, get_all_events


def test_build_parallel_timeline():
    log_files = [
        "data/system.log",
        "data/application.log",
        "data/browser.log",
        "data/auth.log",
    ]

    events = get_all_events(log_files)
    timeline = build_parallel_timeline(events)

    assert len(timeline) == 32

    for i in range(len(timeline) - 1):
        assert timeline[i].timestamp <= timeline[i + 1].timestamp