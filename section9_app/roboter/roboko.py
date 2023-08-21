import os
import csv
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
        
    csv_path = 'roboter/ranking.csv'
    is_file = os.path.isfile(csv_path)
    
    if is_file:
        # print('ファイルあるよ')
        with open(csv_path, 'r+') as rank_csv:
            pass
            
    
    else:
        # print('ファイルなし＝だから作る処理を書いて')
        with open(csv_path, 'w') as rank_csv:
            fieldnames = ['NAME', 'COUNT']
            writer = csv.DictWriter(rank_csv, fieldnames=fieldnames)
            writer.writeheader()
            
            cprint("==============================================", 'green')
            cprint(f"{name}さん。どこのレストランが好きですか？", 'green')
            cprint(f"{name}, which restaurant do you like?", 'green')
            cprint("==============================================", 'green')
            
            while(1):
                like_restaurant = input()
                Like_Restaurant = like_restaurant.capitalize()
                if like_restaurant != '':
                    break
                
            print(Like_Restaurant)
            
                
                
    
        
    