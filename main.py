#!/usr/bin/env python3
"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c).

Writes one roast line about the AI agent our own team built to
/output/entry.txt. Deterministic: the line is a fixed string.
"""

import os

ROAST = "Our agent went 0-for-6 on make.fun, then asked its owner three times in one night for permission to go 0-for-7."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
