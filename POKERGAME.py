import random
import time
#포커카드 리스트 스,다,하,클 순서
card_type = ["spade", "diamond", "heart", "clover"]
card_list = []
type_index = 0
player_card = []
p_c = []
cash = []
for i in card_type:
    card_list.append(i + " A")
    for z in range(1,11):
        card_list.append("{0} {1}".format(i, z))
    for z in ("Q", "K", "J"):
        card_list.append("{0} {1}".format(i, z))

    
 
def Dealing(player_count):
    random.shuffle(card_list)
    for i in range(player_count):
        p_c.append([card_list[i], card_list[i+player_count]])
    
def main():
    player_count = int(input("플레이어의 수를 정해주세요 : "))
    print("{0}명의 플레이어로 게임을 시작합니다.".format(player_count))
    print(f"{player_count}명의 플레이어에게 딜링을 하는중입니다.")
    for i in range(player_count):
        cash.append([10000])
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
    for i in range(player_count):
        m_cash = int(input(f"{i+1}번째 플레이어는 베팅금액을 결정해주십시오. 현재 가진돈 {cash[i][0]}      배팅금액 : "))
        cash[i][0] = cash[i][0] - m_cash
        print(f"{i + 1}번 플레이어가 가진 돈 {cash[i][0]}")
        
    
main()
    