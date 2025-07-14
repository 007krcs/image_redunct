import re

def detect_ids_with_gemini(full_text: str):
    pii_entities = []

    # 1. 🎯 Strict known formats for IDs (specific country patterns)
    patterns = {
        "PASSPORT": r"\b[A-Z][0-9]{7,9}\b",
        "AADHAAR": r"\b[0-9]{4}[\s-]?[0-9]{4}[\s-]?[0-9]{4}\b",
        "PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        "SSN": r"\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b",
        "PHONE": r"\b\+?[0-9]{10,13}\b",
        "PERSONAL_NO": r"\b[0-9]{6,7}\b",
    }

    for label, pattern in patterns.items():
        matches = re.findall(pattern, full_text.upper())
        for match in matches:
            if isinstance(match, tuple):
                match = " ".join(match)
            pii_entities.append({"type": label, "value": match})

    # 2. 🌍 Fallback: generic alphanumeric IDs (e.g. Korean, French IDs)
    for match in re.findall(r"\b[A-Z0-9]{6,12}\b", full_text):
        if not match.isdigit() and not any(char.islower() for char in match):  # avoid common words
            pii_entities.append({"type": "GENERIC_ID", "value": match})

    # 3. 📅 Match European date format - NOT masked, only detected
    # (Optional: remove this if you don't want any date detection at all)
    # for match in re.findall(r"\b\d{2}[\/\-\s]\d{2}[\/\-\s]\d{4}\b", full_text):
    #     pii_entities.append({"type": "EURO_DATE", "value": match})

    # ❌ 4. Avoid masking based on label keywords like NOM/SEX/etc. – COMMENTED OUT
    # This caused names/nationality to be masked unnecessarily
    # known_keywords = ["NOM", "SEX", "PRÉNOMS", "NATIONALITÉ", "NAISSANCE", "DOCUMENT"]
    # for line in full_text.splitlines():
    #     for keyword in known_keywords:
    #         if keyword in line.upper():
    #             values = re.findall(r"[A-Z]{3,}", line)
    #             for val in values:
    #                 pii_entities.append({"type": "KEYWORD", "value": val})

    return pii_entities

