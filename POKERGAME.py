import random
import time
#포커카드 리스트 스,다,하,클 순서
card_type = ["spade", "diamond", "heart", "clover"]
card_list = []
type_index = 0
player_card = []
p_c = []
cash = []
fold_player = []
fold_player_index = []
betting_cash = []
for i in card_type:
    card_list.append(i + " A")
    for z in range(1,11):
        card_list.append("{0} {1}".format(i, z))
    for z in ("Q", "K", "J"):
        card_list.append("{0} {1}".format(i, z))

def raise1(m_cash, b_raise, player_count):
    for bet in range(player_count):
        betting_cash[bet][0] = 0
    for p_bet in range(player_count):
        if betting_cash[p_bet][0] == 'Fold':
                continue
        play_bet = input(f"""{p_bet + 1}번째 플레이어님 콜하시겠습니까? 레이즈하시겠습니까? 폴드하겠습니까?
                
콜 = call 레이즈 = raise 폴드 = fold
영어로 작성해 주십시오 : """)
        if play_bet == "call":
            betting_cash[p_bet][0] = betting_cash[p_bet][0]+m_cash
        elif play_bet == 'fold':
            fold_player.append(betting_cash[p_bet][0])
            betting_cash[p_bet][0] = "Fold"
            fold_player_index.append(p_bet)
        elif play_bet == "raise":
            b_raise = int(input(f"얼마를 추가로 베팅하시겠습니까? | 현재 배팅금액 {betting_cash[0][0]} + "))
            m_cash = m_cash + b_raise
            raise1(m_cash, b_raise, player_count)
        
    
 
def Dealing(player_count):
    shuffle_card = card_list
    random.shuffle(card_list)
    for i in range(player_count):
        p_c.append([card_list[i], card_list[i+player_count]])
        
def betting1(player_count, player_index):
    for i in range(2):
        print(f"{player_index+1}번째 플레이어는 베팅금액을 결정해주십시오. 현재 가진돈 {cash[player_index][0]}")
        for indexer in range(player_count):
            print(f"{indexer + 1}번째 플레이어의 돈 {cash[indexer][0]} | 배팅금액 : {betting_cash[indexer][0]}")
        m_cash = int(input("배팅할 금액 : "))
        betting_cash[i][0] = betting_cash[i][0]+m_cash
        for p_bet in range(1, player_count):
            if betting_cash[p_bet][0] == 'Fold':
                continue
            play_bet = input(f"""{p_bet + 1}번째 플레이어님 콜하시겠습니까? 레이즈하시겠습니까? 폴드하겠습니까?
                
콜 = call 레이즈 = raise 폴드 = fold
영어로 작성해 주십시오 : """)
            if play_bet == "call":
                betting_cash[p_bet][0] = betting_cash[p_bet][0]+m_cash
            elif play_bet == 'fold':
                fold_player.append(betting_cash[p_bet][0])
                betting_cash[p_bet][0] = "Fold"
                fold_player_index.append(p_bet)
            elif play_bet == "raise":
                b_raise = int(input(f"얼마를 추가로 베팅하시겠습니까? | 현재 배팅금액 {betting_cash[0][0]} + "))
                m_cash = m_cash + b_raise
                raise1(m_cash, b_raise, player_count)
        if player_index == player_count:
            continue
        player_index += 1

def main():
    player_count = int(input("플레이어의 수를 정해주세요 : "))
    print("{0}명의 플레이어로 게임을 시작합니다.".format(player_count))
    print(f"{player_count}명의 플레이어에게 딜링을 하는중입니다.")
    for i in range(player_count):
        cash.append([10000])
        betting_cash.append([0])
    time.sleep(1)
    Dealing(player_count)
    print("게임은 텍사스 홀덤규칙으로 진행됩니다. 플레이어 분들은 자신의 카드를 확인해 주세요.")
    for i in range(player_count):
        trash = input(f"{i+1}번째 플레이어님 자신의 카드를 확인해 주세요.")
        if trash == "break":
            break
        else:
            print(p_c[i-1][0], p_c[i-1][1])
        trash = input("카드를 확인하셨다면 Enter을 눌러주세요")
        for i in range(5000):
            print(".")
            
    betting1(player_count, 0)
    
    
        
    
main()
    