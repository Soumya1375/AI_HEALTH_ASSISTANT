def is_emergency(text: str) -> bool:
    keywords = [
        "chest pain", "breathing problem", "faint", "stroke",
        "severe pain", "unconscious", "heart attack"
    ]

    text_lower = text.lower()
    return any(k in text_lower for k in keywords)