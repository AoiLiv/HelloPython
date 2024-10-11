import random

def get_computer_choice():
    # コンピュータの選択肢をランダムに決定
    choices = ['グー', 'チョキ', 'パー']
    return random.choice(choices)

def get_user_choice():
    # プレイヤーにじゃんけんの選択を入力してもらう
    choice = input("グー、チョキ、パーを選んでください: ")
    while choice not in ['グー', 'チョキ', 'パー']:
        choice = input("無効な入力です。グー、チョキ、パーを選んでください: ")
    return choice

def determine_winner(user_choice, computer_choice):
    # 勝敗の判定を行う
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == 'グー' and computer_choice == 'チョキ') or \
         (user_choice == 'チョキ' and computer_choice == 'パー') or \
         (user_choice == 'パー' and computer_choice == 'グー'):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"

def play_round():
    # 1回のじゃんけんを行い結果を返す
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"コンピュータの選択: {computer_choice}")
    print(f"あなたの選択: {user_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

def play_game():
    print("じゃんけん3回勝負を始めましょう!")
    
    user_wins = 0
    computer_wins = 0
    rounds = 0
    
    while user_wins < 2 and computer_wins < 2:
        print(f"\n{rounds + 1}回戦目:")
        result = play_round()
        rounds += 1
        
        if result == "あなたの勝ち":
            user_wins += 1
        elif result == "コンピュータの勝ち":
            computer_wins += 1
        
        print(f"現在のスコア - あなた: {user_wins}, コンピュータ: {computer_wins}")
    
    # 最終結果を表示
    if user_wins == 2:
        print("\nあなたが3回勝負で勝ちました!")
    else:
        print("\nコンピュータが3回勝負で勝ちました!")

# ゲームを開始
if __name__ == "__main__":
    play_game()
