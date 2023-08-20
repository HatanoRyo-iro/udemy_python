from termcolor import cprint

def start():
    cprint("==============================================", 'green')
    cprint("こんにちは！私はRobokoです。あなたの名前は？", 'green')
    cprint("Hello, I am Roboko. What is your name?", 'green')
    cprint("==============================================", 'green')
    
    while(1):
        name = input()
        if name != '':
            break
        
    cprint("==============================================", 'green')
    cprint(f"{name}さん。どこのレストランが好きですか？", 'green')
    cprint(f"{name}, which restaurant do you like?", 'green')
    cprint("==============================================", 'green')
    
        
    