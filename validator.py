def validate(data):
    required=[
        "flight_number","origin","destination","date",
        "no_of_pieces","weight_kg","agent_name","agent_id"
    ]
    errors=[]
    for k in required:
        if k not in data:
            errors.append(f"{k} missing")
    return errors