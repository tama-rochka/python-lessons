with open('thameshello.txt', 'w') as f:
    f.write('hi thames! this is a test')
    f.write('\n')
    
with open('thameshello.txt') as f:
    full_text = f.read()

print(full_text)