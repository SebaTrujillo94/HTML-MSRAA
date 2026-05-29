
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
terms = ['sb-open', 'sb-expanded', 'openSidebarBtn', 'toggleSidebar', 'closeSide', 
         'sidebars-hidden', 'body.', 'classList.add(', 'classList.remove(', 'classList.toggle(']
for i, line in enumerate(lines):
    for t in terms:
        if t in line and ('sidebar' in line.lower() or 'sb-' in line or 'menu' in line.lower()):
            print(f'Line {i+1}: {line.rstrip()}')
            break
