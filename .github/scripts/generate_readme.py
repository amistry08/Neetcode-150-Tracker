import json
import os

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

        filename = title.lower().replace(" ", "_").replace("-", "").replace("(", "").replace(")", "") + ".py"
        filepath = f"solutions/{folder}/{filename}"
        link = f"[{title}]({filepath})" if os.path.exists(filepath) else f"{title}"

        block.append(f"- {emoji} {link}")

    category_blocks[key] = "\n".join(block)

with open("README.template.md", "r", encoding="utf-8") as f:
    template = f.read()

template = template.replace("{{COMPLETED}}", str(completed))

for key, block in category_blocks.items():
    template = template.replace("{{" + key + "}}", block)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(template)

