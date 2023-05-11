def greetings_function(name):
    print('Welcome '+ name + '!')

def greetings_function2(*names):
    for i in names:
        print('Hello ', i + '!')

greetings_function2('Siddhu', 'Yash', 'Simi')