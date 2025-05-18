import json

with open('progress.json', 'r') as f:
    progress = json.load(f)

total = 0
completed = 0
lines = ["# NeetCode 150 Progress\n"]

for category, problems in progress.items():
    solved = sum(problems.values())
    total += len(problems)
    completed += solved
    percent = int((solved / len(problems)) * 100)
    lines.append(f"### {category} ({solved}/{len(problems)}) [{percent}%]")
    lines.append(f"[{'█' * (percent // 10)}{'░' * (10 - percent // 10)}]  \n")

lines.append(f"\n**Total Solved:** {completed}/{total} ({int((completed/total)*100)}%)\n")

with open('README.md', 'w') as f:
    f.write('\n'.join(lines))
