#포커카드 리스트 스,다,하,클 순서
card_type = ["spade", "diamond", "heart", "clover"]
card_list = []
spade = []
diamond = []
heart = []
clover = []

for i in card_type:
    c_type = i
    for z in (spade, diamond, heart, clover):
        z.append(c_type + "A")
        for k in range(2, 11):
            z.append(c_type + " {0}".format(k))
        for i in ["Q", "K"]:
            z.append(c_type + " {0}".format(i))
        card_list.append(z)
print(card_list)
print(len(card_list), len(card_list[0]) + len(card_list[1]) + len(card_list[2]) + len(card_list[3]))