import re

def regex_extract(t):
    def g(p, grp=1, cast=str):
        m = re.search(p, t)
        return cast(m.group(grp)) if m else None

    return {
        "flight_number": g(r"[A-Z]{2}-\d+", 0),
        "origin": g(r"from (\w+)"),
        "destination": g(r"to (\w+)"),
        "date": g(r"on (\d+ \w+)"),
        "no_of_pieces": g(r"(\d+) pieces", cast=int),
        "weight_kg": g(r"(\d+) kg", cast=int),
        "agent_name": g(r"Agent: (\w+)"),
        "agent_id": g(r"ID: (\w+)"),
    }