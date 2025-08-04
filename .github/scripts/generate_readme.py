import json
import os
import re

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

def normalize_title(title):
    """Normalize the title to create a valid filename."""
    title = title.lower()
    title = title.replace(" ", "_")
    title = re.sub(r"[^a-z0-9_]", "", title)  # remove anything not alphanumeric or underscore
    return title + ".py"

with open("progress.json", "r", encoding="utf-8") as f:
    data = json.load(f)

completed = 0
category_blocks = {}

for category, problems in data.items():
    key = category.upper().replace(" ", "_")
    folder = category.lower().replace(" ", "_")
    block = []

    for title, done in problems.items():
        completed += int(done)
        emoji = "✅" if done else "🔲"

        filename = normalize_title(title)
        filepath = f"solutions/{folder}/{filename}"
        link = f"[{title}]({filepath})" if os.path.exists(filepath) else f"{title}"

        if done and not os.path.exists(filepath):
            print(f"⚠️ File not found: {filepath} (expected for: '{title}')")


        block.append(f"- {emoji} {link}")

    category_blocks[key] = "\n".join(block)

with open("README.template.md", "r", encoding="utf-8") as f:
    template = f.read()

template = template.replace("{{COMPLETED}}", str(completed))

for key, block in category_blocks.items():
    template = template.replace("{{" + key + "}}", block)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(template)

