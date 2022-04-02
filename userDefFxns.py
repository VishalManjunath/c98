# function to greet
'''
def greet(name):
    print("Hello, "+ name +". How are you?")

greet("Vishal")
'''

# count words from a file

def word_count():
    file_name=input('Enter the file: ')

    no_words=0

    file=open(file_name, 'r')

    for line in file:
        words=line.split()
        no_words+=len(words)
        
    print(no_words)

word_count()

