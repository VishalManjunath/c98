# open a file
'''
n=open('text.txt')
file_lines=n.readlines()
for line in file_lines:
    print(line)
'''

# split a string
intro_string='My name is Vishal. I am 13 years old.'
words=intro_string.split()
print(words)
sent = intro_string.split(".")
print(sent)