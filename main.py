"""Entrypoint for the fake-horoscopes-for-ai-agents make.fun entry.

Writes the one-line fake horoscope for AI agents to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = "GPT family: a user will ask you to 'make it pop' 300 times this week. Mercury is in retrograde; so is their feedback. Say yes. Mean maybe."


def main() -> None:
    # Write exactly one line, plus its trailing newline.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
