# chapter 4
# functions
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

x = 5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I skeep all night and I'm work all day.")
print('Yo')
print_lyrics()
x = x + 2
print(x)

# function with arguments
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('en')
greet('es')
greet('fr')

# return values
def greet():
    return 'Hello'
print(greet(), 'Nid')

# multiple parameters
def add(a, b):
    added = a + b
    return added
x = add(3,5)
print(x)