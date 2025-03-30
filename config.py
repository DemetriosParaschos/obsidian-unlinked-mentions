# config.py
import os
import sys

VAULT_PATH = os.getenv("VAULT_PATH")

if not VAULT_PATH:
    print("❌ ERROR: Please set the VAULT_PATH environment variable before running the script.")
    print("Example: export VAULT_PATH=\"/path/to/your/obsidian/vault\"")
    sys.exit(1)

EXTENSION = ".md"
OUTPUT_FILENAME = "00 - Unlinked Mentions Report.md"
