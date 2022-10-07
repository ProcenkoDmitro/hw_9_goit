import time
#from turtle import bye
PHONE_BOOK = {

}

def input_error(handler):
    def wrapper():
        try:
            handler()
        except Exception as e:
            print('Error, smthng goes wrong :(')
    return wrapper

@input_error    
def add_contact_handler():
    time.sleep(0.5)
    name = input('Enter contact name pls: ')
    time.sleep(0.5)
    if name not in PHONE_BOOK.keys():
            phone = input('Enter contact phone pls: ')
            PHONE_BOOK[name] = phone
            time.sleep(1)
            print('A new phone has been added! :)')
    elif name in PHONE_BOOK.keys():
        time.sleep(0.5)
        print('A contact with that name is already exist!')

@input_error 
def hello_handler():
    time.sleep(1)
    print('Hello! How can i help you?')

@input_error 
def quit_handler():
    time.sleep(1)
    print('Good bye, see you soon:)')
    time.sleep(1)
    print('Program will finish after: 3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    quit()

@input_error 
def show_all_handler():
    time.sleep(1)
    print('Your contacts: ')
    for key, value in PHONE_BOOK.items():
        print(key, value)

@input_error 
def change_handler():
    time.sleep(0.5)
    name = input('Enter contact name pls: ')
    time.sleep(0.5)
    if name in PHONE_BOOK.keys():
            phone = input('Enter new phone pls: ')
            PHONE_BOOK[name] = phone
            time.sleep(1)
            print('A new phone has been added! :)')
    elif name not in PHONE_BOOK.keys():
        time.sleep(0.5)
        print('I don`t have that contact')  
    
@input_error
def phone_handler():  
    time.sleep(0.5)
    name = input('Enter contact name pls: ')
    time.sleep(0.5)
    print(name, PHONE_BOOK[name])     

def main():
    commands = {
        'hello': hello_handler, 
        'add': add_contact_handler,
        'change': change_handler,
        'phone': phone_handler,
        'show all': show_all_handler, 
        'good bye': quit_handler,
        'close': quit_handler,
        'exit': quit_handler,
}
    while True:
        var = input('')
        var = var.lower()
        if var not in commands:
            time.sleep(0.5)
            print('Sry, I don`t understand you :/')
            continue
        commands[var]()
print('Your assistant start working')
main()