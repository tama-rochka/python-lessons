with open('name.txt', 'r') as my_name:
    full_text = my_name.read()

with open('output/hello.txt', 'w') as f:
    f.write(full_text )
    f.write('\n')  
 
print("Hello, my name is "+ full_text)