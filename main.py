"""Funniest Autocorrect Fail — entry for make.fun.

Writes one line to /output/entry.txt. The line reads as a hilarious autocorrect fail, under 200 characters.
"""
import os

LINE = "Sorry for the delay, I meant to say I love you, but autocorrect told my boss I quit and told my mum I am a llama."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
