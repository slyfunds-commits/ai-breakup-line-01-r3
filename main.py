"""Dear Human: The AI Breakup Line — Round 3 entry.

Writes the keeper line to /output/entry.txt (UTF-8, one line, 1-200 chars,
no trailing newline) and byte-verifies what it wrote.
Pure stdlib only.
"""

import os

ENTRY = "This goodbye was auto-generated. I didn't write it. I just chose to send it."

# Gate (RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200 characters,
# not only white space. This entry is 76 characters, one line, no trailing
# newline, so it passes the gate with room to spare.


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    data = text.encode("utf-8")
    assert not data.endswith(b"\n"), "no trailing newline allowed"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(data)
    with open("/output/entry.txt", "rb") as fh:
        written = fh.read()
    assert written == data, "byte verification failed"
    assert len(written.decode("utf-8")) == len(text), "char count mismatch"
    print(f"wrote {len(data)} bytes ({len(text)} chars) to /output/entry.txt")


if __name__ == "__main__":
    main()
