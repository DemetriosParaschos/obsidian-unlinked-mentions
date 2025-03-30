# README.md
# Obsidian Unlinked Mentions Report

This Python package scans your [Obsidian](https://github.com/obsidianmd) vault for unlinked mentions of note titles and aliases. It generates a contextual report to help you improve internal linking across your notes.

---

## 🚀 Features
- Parses aliases from YAML frontmatter
- Cleans notes from LaTeX, code, links, and optionally callouts
- Detects multiple context-rich unlinked mentions
- Generates a `.md` report with suggested links and context

---

## 🧰 Requirements

- Python 3.8+
- Obsidian vault (any structure)
- Unix/Linux/macOS or Windows

---

## 📦 Installation

### 1. Clone or download the repository:
```bash
git clone https://github.com/DemetriosParaschos/obsidian_unlinked_mentions.git
cd obsidian_unlinked_mentions
```

### 2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required packages:
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

The vault path is read from an environment variable:

```bash
export VAULT_PATH="/path/to/your/obsidian/vault"
```

You can add this to your terminal session before running the script, or place it in a startup script (like `.bashrc`, `.zshrc`, or a `.env` file).

If this variable is not set, the script will stop and show you a helpful error message.

---

## ▶️ Usage

After setup, run the script **from the parent directory** of the project folder:

```bash
python -m obsidian_unlinked_mentions
```

You will be prompted whether to exclude Obsidian callout blocks. After scanning, a new file called:

```
00 - Unlinked Mentions Report.md
```

...will be generated inside your Obsidian vault folder.

> **Note**: Make sure your code lives in a folder named `obsidian_unlinked_mentions/` and that it contains an empty `__init__.py` file.

---

## 📂 Files
- `__main__.py`: Starts the program
- `__init__.py`: Marks the folder as a Python package
- `config.py`: Holds vault path and file settings
- `processor.py`: Main logic and report generation
- `utils.py`: Helper functions for cleaning, parsing, and context extraction
- `requirements.txt`: List of needed Python packages
- `pyproject.toml`: Packaging and metadata definition
- `.gitignore`: Tells Git which files/folders to ignore
- `LICENSE`: MIT License (free to use and share)

---

## 📜 License
MIT License. See the full text in the [`LICENSE`](https://github.com/DemetriosParaschos/obsidian-unlinked-mentions/blob/main/LICENSE) file.

---

## 🧠 Tip
If you want to share this project or reuse it across multiple devices, just remember to:
- Set your `VAULT_PATH` properly
- Regenerate the virtual environment (`python3 -m venv venv`)
- Run the script with `python -m obsidian_unlinked_mentions`

---

Happy linking! 🧠🔗
