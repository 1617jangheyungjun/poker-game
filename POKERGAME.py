import random
#포커카드 리스트 스,다,하,클 순서
card_type = ["spade", "diamond", "heart", "clover"]
card_list = []
spade = []
diamond = []
heart = []
clover = []
type_index = 0
for z in (spade, diamond, heart, clover):
    z.append(card_type[type_index] + "A")
    for k in range(2, 11):
        z.append(card_type[type_index] + " {0}".format(k))
    for i in ["Q", "K", "J"]:
        z.append(card_type[type_index] + " {0}".format(i))
    card_list.append(z)
    type_index +=1
print(card_list)
print(len(card_list), len(card_list[0]))
 
def Dealing():
    for i in range