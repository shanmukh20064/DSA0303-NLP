def check_agreement(subject, verb):
    subjects = {
        "he": {"Number": "singular", "Person": "third"},
        "she": {"Number": "singular", "Person": "third"},
        "it": {"Number": "singular", "Person": "third"},
        "they": {"Number": "plural", "Person": "third"}
    }
    verbs = {
        "runs": {"Number": "singular"},
        "writes": {"Number": "singular"},
        "run": {"Number": "plural"},
        "write": {"Number": "plural"}
    }
    if subject not in subjects or verb not in verbs:
        return False
    return subjects[subject]["Number"] == verbs[verb]["Number"]
subject = input("Enter subject: ").lower()
verb = input("Enter verb: ").lower()
print(check_agreement(subject, verb))