# README.md
# Obsidian Unlinked Mentions Report

This Python script scans your Obsidian vault for unlinked mentions of note titles and aliases. It produces a contextual report that helps improve internal linking in your notes.

---

## 🚀 Features
- Parses aliases from YAML frontmatter
- Cleans notes from LaTeX, code, links, and optionally callouts
- Detects multiple context-rich unlinked mentions
- Generates a `.md` report with suggested links and context

---

## 📦 Installation

### 1. Clone or download the repository:
```bash
git clone https://github.com/yourusername/project_root.git
cd project_root
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

If not set, the script uses the default path hardcoded in `config.py`.

---

## ▶️ Usage

After setting up everything, simply run:

```bash
python -m project_root
```

You will be prompted whether to exclude Obsidian callout blocks. After scanning, a new file called:

```
00 - Unlinked Mentions Report.md
```

...will be generated in your vault directory.

---

## 🛠️ What is `pyproject.toml`?

The `pyproject.toml` file is a modern way to define your Python project's metadata and build system. It:
- Replaces `setup.py` for most uses
- Declares dependencies and Python version
- Allows easy installation via `pip`
- Supports packaging your project as a module (if you wish to distribute it later)

If you're just running the script, you don't *need* to touch this file. But it's good practice to have it included.

---

## 📂 Files
- `__main__.py`: Starts the program
- `config.py`: Holds vault path and file settings
- `processor.py`: Main logic and report generation
- `utils.py`: Helper functions for cleaning, parsing, and context extraction
- `requirements.txt`: List of needed Python packages
- `pyproject.toml`: Packaging and metadata definition
- `.gitignore`: Tells Git which files/folders to ignore
- `LICENSE`: MIT License (free to use and share)

---

## 📜 License
MIT License. See full license below:

```
MIT License

Copyright (c) 2025 Demetrios Paraschos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🧠 Tip
If you want to share this project or reuse it across multiple devices, just remember to:
- Set your `VAULT_PATH` properly
- Regenerate the virtual environment (`python3 -m venv venv`)
- Run the script with `python -m project_root`

---

Happy linking! 🧠🔗

