"""Create a teacher account for the local activities application."""

import getpass
import hashlib
import json
import secrets
from pathlib import Path


teachers_file = Path(__file__).parent / "teachers.json"
iterations = 600_000


def main():
    username = input("Teacher username: ").strip()
    if not username or ":" in username:
        raise SystemExit("Username cannot be empty or contain a colon")

    password = getpass.getpass("Teacher password: ")
    confirmation = getpass.getpass("Confirm password: ")
    if not password:
        raise SystemExit("Password cannot be empty")
    if password != confirmation:
        raise SystemExit("Passwords do not match")

    if teachers_file.exists():
        with teachers_file.open(encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = {"teachers": {}}

    teachers = data.setdefault("teachers", {})
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iterations
    ).hex()
    teachers[username] = {
        "salt": salt.hex(),
        "password_hash": password_hash,
    }

    with teachers_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")
    print(f"Teacher account '{username}' saved to {teachers_file.name}")


if __name__ == "__main__":
    main()