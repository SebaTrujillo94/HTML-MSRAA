
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find project detail overlay HTML
for i, line in enumerate(lines):
    if 'pdOverlay' in line or 'pd-overlay' in line or 'pd-title' in line or 'pdOrientBtn' in line or 'pdCloseBtn' in line:
        print(f'{i+1}: {line.rstrip()}')
