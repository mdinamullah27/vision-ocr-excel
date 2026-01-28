def deduplicate(voters):
    seen = set()
    unique = []

    for v in voters:
        key = (v.get("voter_no"), v.get("name"), v.get("father"))
        if key not in seen:
            seen.add(key)
            unique.append(v)

    return unique
