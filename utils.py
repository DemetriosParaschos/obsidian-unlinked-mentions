# utils.py
import re
import yaml

def prompt_exclude_callouts():
    user_input = input("Exclude callouts from search? (y/n): ").strip().lower()
    return user_input == 'y'

def extract_aliases(content):
    aliases = []
    if content.startswith("---"):
        try:
            frontmatter, _ = content.split("---", 2)[1:]
            metadata = yaml.safe_load(frontmatter)
            if isinstance(metadata, dict):
                for key in ("alias", "aliases"):
                    if key in metadata:
                        val = metadata[key]
                        aliases += [val] if isinstance(val, str) else val
        except Exception:
            pass
    return aliases

def clean_text(text, exclude_callouts=True):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]

    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", "", text)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    text = re.sub(r"\$[^$]*\$", "", text)
    text = re.sub(r"\[[^\]]+\]\([^)]*\)", "", text)
    text = re.sub(r"\[\[.*?\]\]", "", text)

    if not exclude_callouts:
        return text

    lines = text.splitlines()
    cleaned_lines = []
    in_callout = False

    for line in lines:
        if re.match(r'>\s*\[!\w+', line, flags=re.IGNORECASE):
            in_callout = True
            continue
        elif in_callout and line.strip().startswith(">"):
            continue
        else:
            in_callout = False
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)

def extract_all_contexts(text, term, length=60):
    matches = list(re.finditer(rf"(?<!\[\[)\b{re.escape(term)}\b(?!\]\])", text))
    contexts = []
    for match in matches:
        start = max(0, match.start() - length // 2)
        end = min(len(text), match.end() + length // 2)
        snippet = text[start:end].strip().replace('\n', ' ')
        snippet = re.sub(r"\s+", " ", snippet)
        snippet = re.sub(r"[#*_`>\-]+", "", snippet)

        if term.lower() not in snippet.lower():
            snippet = text[match.start():match.end() + 30]

        sentence_match = re.search(rf"[^.?!]*\b{re.escape(term)}\b[^.?!]*[.?!]", snippet)
        context = sentence_match.group(0).strip() if sentence_match else snippet
        contexts.append(context)
    return contexts
