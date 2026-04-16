def prompt(text):
    return f"""
Role- Act as data extractor model. Your role is to just extract data from the given 
text and return in valid JSON format.
Task- Extract fields from text in format as specified in schema below.
Schema- "flight_number", 
        "origin", 
        "destination", 
        "date",
        "no_of_pieces", 
        "weight_kg", 
        "agent_name", 
        "agent_id" 

Constraints- If missing field then return null, Return in JSON format
Failure Behaviour- if confidence low return "low confidence"

Text:
{text}
"""