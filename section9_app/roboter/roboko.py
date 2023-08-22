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
            reader = csv.DictReader(rank_csv)
            
            rank_dist = {}
            for each in reader:
                each_restaurant = each['NAME']
                each_count = each['COUNT']
                rank_dist[each_restaurant] = int(each_count)
                
            # ファイルの読み取り位置を戻す
            rank_csv.seek(11)
            
            for each in reader:
                each_restaurant = each['NAME']
                each_count = each['COUNT']                
                
                cprint("==============================================", 'green')
                cprint(f'私のおすすめのレストランは、{each_restaurant}です。', 'green')
                cprint(f'I recommend {each_restaurant}.', 'green')
                print('')
                cprint('このレストランは好きですか？ [Yes/No]', 'green')
                cprint('Do you like it? [y/n]', 'green')
                cprint("==============================================", 'green')
            
                answer = input()
                
                yes_ans = ['Yes', 'yes', 'Y', 'y']
                no_ans = ['No', 'no', 'N', 'n']
                
                if answer in yes_ans:
                    print('yes', answer)
                    break
                    
                elif answer in no_ans:
                    print('no', answer)
                    continue
                
                else:
                    print('他の文字が入力されました。')
                    break
                
            cprint("==============================================", 'green')
            cprint(f"{name}さん。どこのレストランが好きですか？", 'green')
            cprint(f"{name}, which restaurant do you like?", 'green')
            cprint("==============================================", 'green')
    
            while(1):
                like_restaurant = input()
                Like_Restaurant = like_restaurant.title()
                if like_restaurant != '':
                    break
                
            print('変更前rank_dist:', rank_dist)
            
            if Like_Restaurant in rank_dist:
                add_count = rank_dist[Like_Restaurant]
                add_count += 1
                rank_dist[Like_Restaurant] = add_count
            
            else:
                writer.writerow({'NAME': Like_Restaurant, 'COUNT': 1})
                
                
    
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
                Like_Restaurant = like_restaurant.title()
                if like_restaurant != '':
                    break
                
            # print(Like_Restaurant)
            
            writer.writerow({'NAME': Like_Restaurant, 'COUNT': 1})
    
    
    cprint("==============================================", 'green')
    cprint(f'Roboko: {name}さん。ありがとうございました。', 'green')
    cprint(f'Roboko: Thank you so much, {name}!', 'green')
    print('')
    cprint('良い１日を！さようなら。', 'green')
    cprint('Have a good day!', 'green')
    cprint("==============================================", 'green')
    
    print('変更後rank_dist:', rank_dist)