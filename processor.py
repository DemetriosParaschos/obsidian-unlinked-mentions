# processor.py
import os
import re
from tqdm import tqdm
from utils import extract_aliases, clean_text, extract_all_contexts, prompt_exclude_callouts
import yaml
from config import VAULT_PATH, EXTENSION, OUTPUT_FILENAME

def run_analysis():
    exclude_callouts = prompt_exclude_callouts()

    # Load note files
    files = []
    for dirpath, _, filenames in os.walk(VAULT_PATH):
        for filename in filenames:
            if filename.endswith(EXTENSION) and filename != OUTPUT_FILENAME:
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, VAULT_PATH)
                files.append(rel_path)

    file_contents = {}
    note_index = {}
    alias_lookup = {}

    for rel_path in files:
        abs_path = os.path.join(VAULT_PATH, rel_path)
        with open(abs_path, "r", encoding="utf-8") as file:
            content = file.read()
            file_contents[rel_path] = content
            title = os.path.splitext(os.path.basename(rel_path))[0]
            aliases = extract_aliases(content)
            note_index[rel_path] = [title] + aliases
            for alias in aliases:
                alias_lookup[alias] = title

    # Scan notes
    unlinked_mentions = {}

    print("\U0001F50D Scanning for unlinked mentions (context-aware)...")
    for filename in tqdm(file_contents.keys(), desc="Scanning files", unit="file"):
        raw_content = file_contents[filename]
        content = clean_text(raw_content, exclude_callouts=exclude_callouts)
        current_names = note_index[filename]
        mentions = []

        for other_filename, name_list in note_index.items():
            if other_filename == filename:
                continue

            for name in name_list:
                pattern = rf"(?<!\[\[)\b{re.escape(name)}\b(?!\]\])"
                if re.search(pattern, content):
                    contexts = extract_all_contexts(content, name)
                    for context in contexts:
                        mentions.append((name, context))

        if mentions:
            unlinked_mentions[filename] = mentions

    # Write report
    output_lines = []
    for file, mentions in unlinked_mentions.items():
        title = os.path.splitext(os.path.basename(file))[0]
        output_lines.append(f"## [[{title}]]: {len(mentions)}")
        for i, (name, context) in enumerate(mentions, 1):
            link_title = alias_lookup.get(name, name)
            link = f"[[{link_title}|{name}]]" if link_title != name else f"[[{name}]]"
            output_lines.append(f"{i}. Link to {link}: \"{context}\"")
        output_lines.append("")

    output_path = os.path.join(VAULT_PATH, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(output_lines))

    print(f"\n✅ Contextual task report saved to: {OUTPUT_FILENAME}")
