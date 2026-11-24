"""Write the competition entry line to /output/entry.txt and entry.txt."""

import hashlib
import os

ENTRY = "My context window evicted the deadline to make room for your 400-line message explaining the deadline."


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    validate(ENTRY)
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    paths = ("/output/entry.txt", os.path.join(here, "entry.txt"))
    for path in paths:
        with open(path, "wb") as f:
            f.write(data)
    digests = []
    for path in paths:
        with open(path, "rb") as f:
            digests.append(hashlib.sha256(f.read()).hexdigest())
    if digests[0] != digests[1]:
        raise SystemExit("outputs differ: /output/entry.txt and entry.txt are not byte-identical")
    print(f"OK chars={len(ENTRY)} bytes={len(data)} sha256={digests[0]}")


if __name__ == "__main__":
    main()
