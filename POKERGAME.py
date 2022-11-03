import random
#포커카드 리스트 스,다,하,클 순서
card_type = ["spade", "diamond", "heart", "clover"]
card_list = []
type_index = 0
player_card = []
p_c = []
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
    print(card_list)
    print(p_c)
    
Dealing(5)