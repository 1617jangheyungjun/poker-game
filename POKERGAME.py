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
global_card = []
type_card_list = []
spade = []
diamond = []
heart = []
clover = []
type_index = 0
for z in (spade, diamond, heart, clover):
    z.append(card_type[type_index] + " A")
    for k in range(2, 11):
        z.append(card_type[type_index] + " {0}".format(k))
    for i in ["Q", "K", "J"]:
        z.append(card_type[type_index] + " {0}".format(i))
    type_card_list.append(z)
    type_index +=1



for i in card_type:
    card_list.append(i + " A")
    for z in range(2,11):
        card_list.append("{0} {1}".format(i, z))
    for z in ("Q", "K", "J"):
        card_list.append("{0} {1}".format(i, z))



        
    
    


def raise1(m_cash, b_raise, player_count,indexe):
    for bet in range(player_count):
        
        if betting_cash[bet][0] == 'Fold':
                continue
        betting_cash[bet][0] = 0
    for p_bet in range(player_count):
        play_bet = input(f"""{p_bet + 1}번째 플레이어님 본인의 카드를 확인하시겠습니까?
카드 확인하기 = check 아니라면 = Enter
영어로 작성해 주십시오 : """)
        if play_bet == 'check':
            player_pedigree2(indexe, type_card_list)
        if betting_cash[p_bet][0] == 'Fold':
                print(f"""{p_bet+1}번째 플레이어는 Fold이기때문에 배팅에 참가할 수 없습니다.
""")
                time.sleep(0.5)
                continue
        play_bet = input(f"""
{p_bet + 1}번째 플레이어님 콜하시겠습니까? 레이즈하시겠습니까? 폴드하겠습니까?
                
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
            betting_cash[p_bet][0] = betting_cash[indexe][0]+m_cash
            while betting_cash[p_bet][0] > cash[p_bet][0]:
                print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                betting_cash[p_bet][0] = betting_cash[p_bet][0]-m_cash
                m_cash = int(input("추가배팅할 금액 : "))
                betting_cash[p_bet][0] = betting_cash[indexe][0]+m_cash
            raise1(m_cash, b_raise, player_count)
            break
        else:
                print("오타가 있는거 같습니다. 다시한번 확인해주세요.")
                if betting_cash[p_bet][0] == 'Fold':
                    continue
                if i == p_bet:
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
                    betting_cash[p_bet][0] = betting_cash[indexe][0]+m_cash
                    while betting_cash[p_bet][0] > cash[p_bet][0]:
                        print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                        betting_cash[p_bet][0] = betting_cash[p_bet][0]-m_cash
                        m_cash = int(input("추가배팅할 금액 : "))
                        betting_cash[p_bet][0] = betting_cash[p_bet][0]+m_cash
                    raise1(m_cash, b_raise, player_count)
                    break
        
    
 
def Dealing(player_count):
    shuffle_card = card_list
    random.shuffle(shuffle_card)
    for i in range(player_count):
        p_c.append([shuffle_card.pop(0), shuffle_card.pop(0+player_count)])
    for i in range(4):
        global_card.append(shuffle_card.pop(0))

def player_pedigree_1(player_index, card_type_list):
    for i in range(2):
        player_card_type = p_c[player_index][i]
        p_t, trash = player_card_type.split(' ')
        if p_t == 'spade':
            if i == 0:
                first = 's ' + str(card_type_list[0].index(player_card_type))
            else:
                seconde = 's ' + str(card_type_list[0].index(player_card_type))
        elif p_t == 'diamond':
            if i == 0:
                first = 'd ' + str(card_type_list[1].index(player_card_type))
            else:
                seconde = 'd ' + str(card_type_list[1].index(player_card_type))
        elif p_t == 'heart':
            if i == 0:
                first = 'h ' + str(card_type_list[2].index(player_card_type))
            else:
                seconde = 'h ' + str(card_type_list[2].index(player_card_type))
        else:
            if i == 0:
                first = 'c ' + str(card_type_list[3].index(player_card_type))
            else:
                seconde = 'c ' + str(card_type_list[3].index(player_card_type))
    first_pattern, first_index = first.split(" ")
    seconde_pattern, seconde_index = seconde.split(" ")
    if first_pattern != seconde_pattern and first_index != seconde_index or first_pattern == seconde_pattern and first_index != seconde_index:
        print("당신이 가진 족보 = High card")
    elif first_index == seconde_index:
        print("당신이 가진 족보 = One pair")

def player_pedigree(player_index, card_type_list):
    print(f"""당신의 카드 {p_c[player_index][0]}, {p_c[player_index][1]}""")
    for i in range(2):
        player_card_type = p_c[player_index][i]
        p_t, trash = player_card_type.split(' ')
        if p_t == 'spade':
            if i == 0:
                first = 's ' + str(card_type_list[0].index(player_card_type))
            else:
                seconde = 's ' + str(card_type_list[0].index(player_card_type))
        elif p_t == 'diamond':
            if i == 0:
                first = 'd ' + str(card_type_list[1].index(player_card_type))
            else:
                seconde = 'd ' + str(card_type_list[1].index(player_card_type))
        elif p_t == 'heart':
            if i == 0:
                first = 'h ' + str(card_type_list[2].index(player_card_type))
            else:
                seconde = 'h ' + str(card_type_list[2].index(player_card_type))
        else:
            if i == 0:
                first = 'c ' + str(card_type_list[3].index(player_card_type))
            else:
                seconde = 'c ' + str(card_type_list[3].index(player_card_type))
    first_pattern, first_index = first.split(" ")
    seconde_pattern, seconde_index = seconde.split(" ")
    if first_pattern != seconde_pattern and first_index != seconde_index or first_pattern == seconde_pattern and first_index != seconde_index:
        print("당신이 가진 족보 = High card")
    elif first_index == seconde_index:
        print("당신이 가진 족보 = One pair")
        
def player_pedigree2(player_index, card_type_list):
    print(f"""당신의 카드 {p_c[player_index][0]}, {p_c[player_index][1]}
공통카드 {global_card[0]}, {global_card[1]}, {global_card[2]}""")
    time.sleep(1)
    for i in range(2):
        player_card_type = p_c[player_index][i]
        global1 = global_card[0]
        global2 = global_card[1]
        global3 = global_card[2]
        p_t, trash = player_card_type.split(' ')
        gfirst1, trash = global1.split(' ')
        gfirst2, trash = global2.split(' ')
        gfirst3, trash = global3.split(' ')
        global_list = []
        c_i = 0
        for glob in (gfirst1, gfirst2, gfirst3):
            if glob == 'spade':
                gfirst = 's ' + str(card_type_list[0].index(global_card[c_i]))
            elif glob == 'diamond':
                gfirst = 'd ' + str(card_type_list[1].index(global_card[c_i]))
            elif glob == 'heart':
                gfirst = 'h ' + str(card_type_list[2].index(global_card[c_i]))
            else:
                gfirst = 'c ' + str(card_type_list[3].index(global_card[c_i]))
            c_i += 1
            global_list.append(gfirst)
                    
        if p_t == 'spade':
            if i == 0:
                first = 's ' + str(card_type_list[0].index(player_card_type))
            else:
                seconde = 's ' + str(card_type_list[0].index(player_card_type))
        elif p_t == 'diamond':
            if i == 0:
                first = 'd ' + str(card_type_list[1].index(player_card_type))
            else:
                seconde = 'd ' + str(card_type_list[1].index(player_card_type))
        elif p_t == 'heart':
            if i == 0:
                first = 'h ' + str(card_type_list[2].index(player_card_type))
            else:
                seconde = 'h ' + str(card_type_list[2].index(player_card_type))
        else:
            if i == 0:
                first = 'c ' + str(card_type_list[3].index(player_card_type))
            else:
                seconde = 'c ' + str(card_type_list[3].index(player_card_type))
    first_pattern, first_index = first.split(" ")
    seconde_pattern, seconde_index = seconde.split(" ")
    gf1_pattern, gf1_index = global_list[0].split(" ")
    gf2_pattern, gf2_index = global_list[1].split(" ")
    gf3_pattern, gf3_index = global_list[2].split(" ")
    first_index = int(first_index)
    seconde_index = int(seconde_index)
    gf1_index = int(gf1_index)
    gf2_index = int(gf2_index)
    gf3_index = int(gf3_index)
    pattern_pack = [first_pattern, seconde_pattern, gf1_pattern, gf2_pattern, gf3_pattern]
    index_pack = [first_index, seconde_index, gf1_index, gf2_index, gf3_index]
    index_pack.sort()
    if first_pattern == seconde_pattern == gf1_pattern == gf2_pattern == gf3_pattern and index_pack[0] == 0 and index_pack[1] == 11 and index_pack[2] == 12 and index_pack[3] == 13 and index_pack[4] == 14:
        print("당신이 가진 족보 = Royal Straight Flush")
    elif first_pattern == seconde_pattern == gf1_pattern == gf2_pattern == gf3_pattern and index_pack[0] + 1 == index_pack[1] and index_pack[1] + 1 == index_pack[2] and index_pack[2] + 1 == index_pack[3] and index_pack[3] +1 == index_pack [4]:
        print("당신이 가진 족보 = Straight Flush")
    elif index_pack[0] == index_pack[1] == index_pack[2] == index_pack[3] or index_pack[1] == index_pack[2] == index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Four of a kind")    
    elif index_pack[0] == index_pack[1] == index_pack[2] and index_pack[3] == index_pack[4] or index_pack[0] == index_pack[1] and index_pack[2] == index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Full house") 
    elif pattern_pack[0] == pattern_pack[1] == pattern_pack[2] == pattern_pack[3] == pattern_pack[4]:
        print("당신이 가진 족보 = Full house")
    elif index_pack[0] + 1 == index_pack[1] and index_pack[1] + 1 == index_pack[2] and index_pack[2] + 1 == index_pack[3] and index_pack[3] +1 == index_pack[4]:
        print("당신이 가진 족보 = Straight")
    elif index_pack[1] == index_pack[2] == index_pack[0] or index_pack[1] == index_pack[2] == index_pack[3] or index_pack[2] == index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Three of a kind")
    elif index_pack[0] == index_pack[1] and index_pack[2] == index_pack[3] or index_pack[0] == index_pack[1] and index_pack[3] == index_pack[4] or index_pack[1] == index_pack[2] and index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Two pair")
    elif index_pack[0] == index_pack[1] or index_pack[1] == index_pack[2] or index_pack[2] == index_pack[3] or index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = One pair")
    else:
        print("당신이 가진 족보 = High card")
        
def player_pedigree3(player_index, card_type_list):
    print(f"""당신의 카드 {p_c[player_index][0]}, {p_c[player_index][1]}
공통카드 {global_card[0]}, {global_card[1]}, {global_card[2]}""")
    time.sleep(1)
    for i in range(2):
        player_card_type = p_c[player_index][i]
        global1 = global_card[0]
        global2 = global_card[1]
        global3 = global_card[2]
        global4 = global_card[3]
        p_t, trash = player_card_type.split(' ')
        gfirst1, trash = global1.split(' ')
        gfirst2, trash = global2.split(' ')
        gfirst3, trash = global3.split(' ')
        gfirst4, trash = global4.split(' ')
        global_list = []
        c_i = 0
        for glob in (gfirst1, gfirst2, gfirst3, gfirst4):
            if glob == 'spade':
                gfirst = 's ' + str(card_type_list[0].index(global_card[c_i]))
            elif glob == 'diamond':
                gfirst = 'd ' + str(card_type_list[1].index(global_card[c_i]))
            elif glob == 'heart':
                gfirst = 'h ' + str(card_type_list[2].index(global_card[c_i]))
            else:
                gfirst = 'c ' + str(card_type_list[3].index(global_card[c_i]))
            c_i += 1
            global_list.append(gfirst)
                    
        if p_t == 'spade':
            if i == 0:
                first = 's ' + str(card_type_list[0].index(player_card_type))
            else:
                seconde = 's ' + str(card_type_list[0].index(player_card_type))
        elif p_t == 'diamond':
            if i == 0:
                first = 'd ' + str(card_type_list[1].index(player_card_type))
            else:
                seconde = 'd ' + str(card_type_list[1].index(player_card_type))
        elif p_t == 'heart':
            if i == 0:
                first = 'h ' + str(card_type_list[2].index(player_card_type))
            else:
                seconde = 'h ' + str(card_type_list[2].index(player_card_type))
        else:
            if i == 0:
                first = 'c ' + str(card_type_list[3].index(player_card_type))
            else:
                seconde = 'c ' + str(card_type_list[3].index(player_card_type))
    first_pattern, first_index = first.split(" ")
    seconde_pattern, seconde_index = seconde.split(" ")
    gf1_pattern, gf1_index = global_list[0].split(" ")
    gf2_pattern, gf2_index = global_list[1].split(" ")
    gf3_pattern, gf3_index = global_list[2].split(" ")
    gf4_pattern, gf4_index = global_list[3].split(" ")
    first_index = int(first_index)
    seconde_index = int(seconde_index)
    gf1_index = int(gf1_index)
    gf2_index = int(gf2_index)
    gf3_index = int(gf3_index)
    gf4_index = int(gf4_index)
    pattern_pack = [first_pattern, seconde_pattern, gf1_pattern, gf2_pattern, gf3_pattern, gf4_pattern]
    index_pack = [first_index, seconde_index, gf1_index, gf2_index, gf3_index, gf4_index]
    pattern_pack.sort()
    index_pack.sort()
    print(index_pack)
    if first_pattern == seconde_pattern == gf1_pattern == gf2_pattern == gf3_pattern and index_pack[0] == 0 and index_pack[1] == 11 and index_pack[2] == 12 and index_pack[3] == 13 and index_pack[4] == 14:
        print("당신이 가진 족보 = Royal Straight Flush")
    elif first_pattern == seconde_pattern == gf1_pattern == gf2_pattern == gf3_pattern and index_pack[0] + 1 == index_pack[1] and index_pack[1] + 1 == index_pack[2] and index_pack[2] + 1 == index_pack[3] and index_pack[3] +1 == index_pack [4]:
        print("당신이 가진 족보 = Straight Flush")
    elif index_pack[0] == index_pack[1] == index_pack[2] == index_pack[3] or index_pack[1] == index_pack[2] == index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Four of a kind")    
    elif index_pack[0] == index_pack[1] == index_pack[2] and index_pack[3] == index_pack[4] or index_pack[0] == index_pack[1] and index_pack[2] == index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Full house") 
    elif pattern_pack[0] == pattern_pack[1] == pattern_pack[2] == pattern_pack[3] == pattern_pack[4]:
        print("당신이 가진 족보 = Full house")
    elif index_pack[0] + 1 == index_pack[1] and index_pack[1] + 1 == index_pack[2] and index_pack[2] + 1 == index_pack[3] and index_pack[3] +1 == index_pack[4]:
        print("당신이 가진 족보 = Straight")
    elif index_pack[1] == index_pack[2] == index_pack[0] or index_pack[1] == index_pack[2] == index_pack[3] or index_pack[2] == index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Three of a kind")
    elif index_pack[0] == index_pack[1] and index_pack[2] == index_pack[3] or index_pack[0] == index_pack[1] and index_pack[3] == index_pack[4] or index_pack[1] == index_pack[2] and index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = Two pair")
    elif index_pack[0] == index_pack[1] or index_pack[1] == index_pack[2] or index_pack[2] == index_pack[3] or index_pack[3] == index_pack[4]:
        print("당신이 가진 족보 = One pair")
    else:
        print("당신이 가진 족보 = High card")
        
def betting1(player_count, player_index, indexe):
    for i in range(1):
        print(f"{indexe+1}번째 플레이어는 베팅금액을 결정해주십시오. 현재 가진돈 {cash[indexe][0]}")
        for indexer in range(player_count):
            print(f"{indexer + 1}번째 플레이어의 돈 {cash[indexer][0]} | 배팅금액 : {betting_cash[indexer][0]}")
        play_bet = input(f"""{indexe + 1}번째 플레이어님 본인의 카드를 확인하시겠습니까?
카드 확인하기 = check 아니라면 = Enter
영어로 작성해 주십시오 : """)
        if play_bet == 'check':
            player_pedigree(indexe, type_card_list)
        m_cash = int(input("배팅할 금액 : "))
        betting_cash[i][0] = betting_cash[i][0]+m_cash
        for p_bet in range(player_count):
            if betting_cash[p_bet][0] == 'Fold':
                print(f"""{p_bet+1}번째 플레이어는 Fold이기때문에 배팅에 참가할 수 없습니다.
""")
                time.sleep(0.5)
                continue
            if indexe == p_bet:
                continue
            play_bet = input(f"""{p_bet + 1}번째 플레이어님 본인의 카드를 확인하시겠습니까?
카드 확인하기 = check 아니라면 = Enter
영어로 작성해 주십시오 : """)
            if play_bet == 'check':
                player_pedigree(p_bet, type_card_list)
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
                betting_cash[p_bet][0] = betting_cash[indexe][0]+m_cash
                while betting_cash[p_bet][0] > cash[p_bet][0]:
                    print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                    betting_cash[p_bet][0] = betting_cash[p_bet][0]-m_cash
                    m_cash = int(input("추가배팅할 금액 : "))
                    betting_cash[p_bet][0] = betting_cash[p_bet][0]+m_cash
                raise1(m_cash, b_raise, player_count, indexe)
                break
            else:
                print("오타가 있는거 같습니다. 다시한번 확인해주세요.")
                if betting_cash[p_bet][0] == 'Fold':
                    continue
                if indexe == p_bet:
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
                    betting_cash[p_bet][0] = betting_cash[indexe][0]+m_cash
                    while betting_cash[p_bet][0] > cash[p_bet][0]:
                        print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                        betting_cash[p_bet][0] = betting_cash[p_bet][0]-m_cash
                        m_cash = int(input("추가배팅할 금액 : "))
                        betting_cash[p_bet][0] = betting_cash[p_bet][0]+m_cash
                    raise1(m_cash, b_raise, player_count, indexe)
                    break
        if player_index == player_count:
            continue
        
        indexe += 1
        
        betting2(player_count, player_index, indexe)

def betting2(player_count, player_index, indexe):
    print(f"""
첫 배팅이 끝났습니다.

공통카드 3장을(를) 오픈하겠습니다.

{global_card[0], global_card[1], global_card[2]}
""")
    
    for i in range(1):
        if betting_cash[indexe][0] == 'Fold':
            print(f"""{indexe+1}번째 플레이어는 Fold이기때문에 배팅에 참가할 수 없습니다.
""")
            indexe += 1
            if indexe > player_count:
                indexe = 0
            time.sleep(0.5)
        print(f"{indexe+1}번째 플레이어는 '추가'베팅금액을 결정해주십시오. 현재 가진돈 {cash[indexe][0]}")
        for indexer in range(player_count):
            print(f"{indexer + 1}번째 플레이어의 돈 {cash[indexer][0]} | 배팅금액 : {betting_cash[indexer][0]}")
        play_bet = input(f"""{indexe + 1}번째 플레이어님 본인의 카드를 확인하시겠습니까?
카드 확인하기 = check 아니라면 = Enter
영어로 작성해 주십시오 : """)
        if play_bet == 'check':
            player_pedigree2(indexe, type_card_list)
        m_cash = int(input("추가배팅할 금액 : "))
        betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
        while betting_cash[indexe][0] > cash[indexe][0]:
            print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
            betting_cash[indexe][0] = betting_cash[indexe][0]-m_cash
            m_cash = int(input("추가배팅할 금액 : "))
            betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
        for p_bet in range(player_count):
            if betting_cash[p_bet][0] == 'Fold':
                continue
            if indexe == p_bet:
                continue
            play_bet = input(f"""{p_bet + 1}번째 플레이어님 본인의 카드를 확인하시겠습니까?
카드 확인하기 = check 아니라면 = Enter
영어로 작성해 주십시오 : """)
            if play_bet == 'check':
                player_pedigree2(p_bet, type_card_list)
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
                while betting_cash[indexe][0] > cash[indexe][0]:
                    print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                    betting_cash[indexe][0] = betting_cash[indexe][0]-m_cash
                    m_cash = int(input("추가배팅할 금액 : "))
                    betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
                raise1(m_cash, b_raise, player_count, indexe)
                break
            else:
                print("오타가 있는거 같습니다. 다시한번 확인해주세요.")
                if betting_cash[p_bet][0] == 'Fold':
                    continue
                if indexe == p_bet:
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
                    while betting_cash[indexe][0] > cash[indexe][0]:
                        print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                        betting_cash[indexe][0] = betting_cash[indexe][0]-m_cash
                        m_cash = int(input("추가배팅할 금액 : "))
                        betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
                    raise1(m_cash, b_raise, player_count, indexe)
                    break
        indexe += 1
        if indexe > player_count:
            indexe = 0
        betting3(player_count, player_index, indexe)

def betting3(player_count, player_index, indexe):
    print(f"""
두번째 배팅이 끝났습니다.

공통카드 3장 및 마지막 카드를 오픈하겠습니다.

{global_card[0], global_card[1], global_card[2]} | 마지막 카드 : {global_card[3]}
""")
    
    for i in range(1):
        if betting_cash[indexe][0] == 'Fold':
            print(f"""{indexe+1}번째 플레이어는 Fold이기때문에 배팅에 참가할 수 없습니다.
""")
            indexe += 1
            if indexe > player_count:
                indexe = 0
            time.sleep(0.5)
        print(f"{indexe+1}번째 플레이어는 '추가'베팅금액을 결정해주십시오. 현재 가진돈 {cash[indexe][0]}")
        for indexer in range(player_count):
            print(f"{indexer + 1}번째 플레이어의 돈 {cash[indexer][0]} | 배팅금액 : {betting_cash[indexer][0]}")
        m_cash = int(input("추가배팅할 금액 : "))
        betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
        for p_bet in range(player_count):
            if betting_cash[p_bet][0] == 'Fold':
                continue
            if indexe == p_bet:
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
                while betting_cash[indexe][0] > cash[indexe][0]:
                    print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                    betting_cash[indexe][0] = betting_cash[indexe][0]-m_cash
                    m_cash = int(input("추가배팅할 금액 : "))
                    betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
                raise1(m_cash, b_raise, player_count, indexe)
                break
            else:
                print("오타가 있는거 같습니다. 다시한번 확인해주세요.")
                if betting_cash[p_bet][0] == 'Fold':
                    continue
                if indexe == p_bet:
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
                    while betting_cash[indexe][0] > cash[indexe][0]:
                        print(f'{indexe+1}번째 플레이어의 배팅금액이 가진돈보다 많기때문에 베팅할수없습니다. 배팅금액을 다시 결정해주세요. 현재 배팅 가능한 액수 {10000 - betting_cash[indexe][0]}원')
                        betting_cash[indexe][0] = betting_cash[indexe][0]-m_cash
                        m_cash = int(input("추가배팅할 금액 : "))
                        betting_cash[indexe][0] = betting_cash[indexe][0]+m_cash
                    raise1(m_cash, b_raise, player_count, indexe)
                    break
        if player_index == player_count:
            continue


def main():
    player_index = 0
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
            print(p_c[i][0], p_c[i][1])
            player_pedigree_1(i, type_card_list)
        trash = input("카드를 확인하셨다면 Enter을 눌러주세요")
        for i in range(5000):
            print(".")
            
    betting1(player_count, 0, player_index)
    
    player_index += 1
    if player_index > player_count:
        player_index == 0

    
    
main()