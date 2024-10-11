import random

def get_computer_choice():
    # コンピュータの選択肢をランダムに決定
    choices = ['グー', 'チョキ', 'パー']
    return random.choice(choices)

def get_user_choice(player_name):
    # プレイヤーにじゃんけんの選択を入力してもらう
    choice = input(f"{player_name}さん、グー、チョキ、パーを選んでください: ")
    while choice not in ['グー', 'チョキ', 'パー']:
        choice = input(f"{player_name}さん、無効な入力です。グー、チョキ、パーを選んでください: ")
    return choice

def determine_winner(choices):
    # 各プレイヤーの選択を基に勝敗を決定する
    unique_choices = set(choices.values())
    
    # 全員同じ手なら引き分け
    if len(unique_choices) == 1:
        return "引き分け"
    
    # グー、チョキ、パーそれぞれの数をカウント
    counts = {'グー': 0, 'チョキ': 0, 'パー': 0}
    for choice in choices.values():
        counts[choice] += 1
    
    # グーが1つでチョキが複数、もしくはチョキが1つでパーが複数、またはパーが1つでグーが複数の場合、その単独の勝者を決定
    if counts['グー'] == 1 and counts['チョキ'] > 0:
        for player, choice in choices.items():
            if choice == 'グー':
                return f"{player}さんが勝ちました!"
    elif counts['チョキ'] == 1 and counts['パー'] > 0:
        for player, choice in choices.items():
            if choice == 'チョキ':
                return f"{player}さんが勝ちました!"
    elif counts['パー'] == 1 and counts['グー'] > 0:
        for player, choice in choices.items():
            if choice == 'パー':
                return f"{player}さんが勝ちました!"
    
    return "引き分け"

def play_round(players):
    # 1回のじゃんけんを行い、結果を返す
    choices = {}
    for player in players:
        choices[player] = get_user_choice(player)
    
    for player, choice in choices.items():
        print(f"{player}さんの選択: {choice}")
    
    result = determine_winner(choices)
    print(result)
    return result

def play_game():
    print("複数プレイヤーでのじゃんけんゲームを始めましょう!")
    
    # プレイヤーの数を取得
    num_players = int(input("プレイヤーの人数を入力してください: "))
    players = []
    
    # プレイヤー名を取得
    for i in range(num_players):
        player_name = input(f"プレイヤー{i+1}の名前を入力してください: ")
        players.append(player_name)
    
    # ゲームのラウンドを開始
    play_round(players)

# ゲームを開始
if __name__ == "__main__":
    play_game()
