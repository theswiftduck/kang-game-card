from classes import *
import time
from tqdm import tqdm

print('KANG CARD GAME v0.01e-10a')
time.sleep(2)
print("Welcome to Kang card game. Please read 'README.md' first if you're not familiar with this card game before")
time.sleep(2)
print('Loading...')
for i in tqdm(range(0,100)):
    time.sleep(0.1)


orders = ['1','2','3','4']
print('Please type your name:')
name = input()
print('Welcome to Kang card game ', name)
print('Please take a seat')
print('Choose your seat between [1-4]')
order = input()

player = Player(name, order)
orders.remove(player.order)

print(orders)
bot1 = Player('Alice', orders[0])
bot2 = Player('Bill', orders[1])
bot3 = Player('Joma', orders[2])


# GAME START
players = [player, bot1, bot2, bot3]


# INITAILIZE DECK
mydeck = Deck()
print(mydeck.cards)

table = Table()

# SHUFFLE THE DECK
mydeck.shuffle_cards()
print(mydeck.cards)

# DISTRIBUTE TO EACH PLAYER
for i in range(0,6):
    for p in players:
        if p.order == '1':
            _pop = mydeck.pop()
            p.get_card(_pop)
            continue
        if p.order == '2':
            _pop = mydeck.pop()
            p.get_card(_pop)
            continue
        if p.order == '3':
            _pop = mydeck.pop()
            p.get_card(_pop)
            continue
        if p.order == '4':
            _pop = mydeck.pop()
            p.get_card(_pop)
            continue

# print(f'{player.name}: ',player.cards)
# print(f'{bot1.name}: ', bot1.cards)
# print(f'{bot2.name}: ', bot2.cards)
# print(f'{bot3.name}: ', bot3.cards)
# print('Current Deck: ', mydeck.cards)
print('On table: ', table.on_table)
print('Deck remians: ', len(mydeck.cards))
is_Kang = False

def check_table(lst):
    drop_list = []
    try:
        for el in lst:
            if el[1] == table.on_table[1]:
                drop_list.append(el)
    except:
        drop_list = []
    return drop_list



def player_turn(obj):
    global is_Kang
    print('Your turn')
    time.sleep(0.1)
    print(f'{bot1.name} have {len(bot1.cards)} on hands')
    print(f'{bot2.name} have {len(bot2.cards)} on hands')
    print(f'{bot3.name} have {len(bot3.cards)} on hands')
    print('Your current score is: ', obj.check_score())
    time.sleep(0.1)
    print(obj.name + "'s Cards: ", sorted(obj.cards))
    time.sleep(0.1)
    drop_list = check_table(obj.cards)
    if len(drop_list) > 0:
        for card in drop_list:
            obj.drop_card(card)
            table.on_table = card
            print(f'You have just drop {table.on_table} into table')
            time.sleep(0.1)
        
        while True:
            choices_list = ['Kang', 'Pass']
            print('Your current score is: ', obj.check_score())
            time.sleep(0.1)
            print('What would you do next? ', choices_list)
            time.sleep(0.1)    
            choose = input()
            if choose == 'Pass':
                break
            elif choose == 'Kang':
                is_Kang = True
                break
            else:
                print("That's not possible, try again.")
                time.sleep(0.1)

    else:
        while True:
            print('You have to draw a card from deck. Press Y to confirm...')
            y = input()
            if y == 'Y' or y == 'y':
                break
            else:
                print('There is no other way bro.')
                time.sleep(0.1)
        pop_ = mydeck.pop()
        obj.get_card(pop_)
        print(f'You have just pick {pop_} up')
        time.sleep(0.1)
        print(obj.name + "'s Cards: ", sorted(obj.cards))
        time.sleep(0.1)
        print('Your current score is: ', obj.check_score())
        time.sleep(0.1)
        while True:
            print('Choose one card from hand to drop to table:')
            will_be_drop = input()
            if will_be_drop in sorted(obj.cards):
                for card in obj.cards:
                    if card[1] == will_be_drop[1]:
                        obj.drop_card(card)
                table.on_table = will_be_drop
                break
            else:
                print('That card is not in your hand. Please try again')
                time.sleep(0.1)
        print(obj.name + "'s Cards: ", sorted(obj.cards))
        time.sleep(0.1)
        print('Your current score is: ', obj.check_score())
        time.sleep(0.1)
        
        while True:
            choices_list = ['Kang', 'Pass']
            print('What would you do next? ', choices_list)
            time.sleep(0.1)        
            choose = input()          
            if choose == 'Pass':
                break
            elif choose == 'Kang':
                is_Kang = True
                break
            else:
                print('That is not possible bro.')
                time.sleep(0.1)


def bot_turn(obj):
    global is_Kang
    print(f"{obj.name}'s turn!!!")
    time.sleep(0.1)
    # print(f'{obj.name} current score is: ', obj.check_score())
    time.sleep(0.1)
    # print(obj.name + "'s Cards: ", sorted(obj.cards))
    time.sleep(0.1)
    drop_list = check_table(obj.cards)
    if len(drop_list) > 0:
        for card in drop_list:
            obj.drop_card(card)
            table.on_table = card
            print(f'{obj.name} have just drop {table.on_table} into table')
            time.sleep(0.1)
        if obj.check_score() < 10:
            print(f'{obj.name} choose to KANG!!!!!')
            time.sleep(0.1)
            is_Kang = True
        else:
            pass

    else:
        print(f'{obj.name} choose to draw from deck.')
        time.sleep(0.1)
        pop_ = mydeck.pop()
        obj.get_card(pop_)
        # print(f'{obj.name} have just pick {pop_} up')
        time.sleep(0.1)
        # print(obj.name + "'s Cards: ", sorted(obj.cards))
        time.sleep(0.1)
        # print(f'{obj.name} current score is: ', obj.check_score())
        time.sleep(0.1)
        will_be_drop = max(obj.cards)
        if will_be_drop in sorted(obj.cards):
            for card in obj.cards:
                if card[1] == will_be_drop[1]:
                    obj.drop_card(card)
                    print(f'{obj.name} have just drop {card} into table')
                    time.sleep(0.1)
            table.on_table = will_be_drop
        
        # print(obj.name + "'s Cards: ", sorted(obj.cards))
        time.sleep(0.1)
        # print(f'{obj.name} current score is: ', obj.check_score())
        time.sleep(0.1)
              
        if obj.check_score() < 10:
            print(f'{obj.name} chose to KANG!!!!!')
            time.sleep(0.1)
            is_Kang = True
        else:
            pass

while len(mydeck.cards) != 0 and len(player.cards) != 0 and len(bot1.cards) != 0 and len(bot2.cards) != 0 and len(bot3.cards) != 0 and is_Kang == False:
     
    player_turn(player)
    if is_Kang == True: break
    print('On table: ', table.on_table)
    time.sleep(2)
    bot_turn(bot1)
    if is_Kang == True: break
    print('On table: ', table.on_table)
    time.sleep(2)
    bot_turn(bot2)
    if is_Kang == True: break
    print('On table: ', table.on_table)
    time.sleep(2)
    bot_turn(bot3)
    if is_Kang == True: break
    print('On table: ', table.on_table)
    time.sleep(2)
    print('Deck remians: ', len(mydeck.cards))
    time.sleep(2)


whowin = {player.name:player.check_score(), bot1.name:bot1.check_score(), bot2.name:bot2.check_score(), bot3.name:bot3.check_score()}

print('The winner is: ', min(whowin, key=whowin.get))
print('The Winner Score is: ', whowin[min(whowin, key=whowin.get)])

print(f'{player.name} score: {player.check_score()}')
print(f'{bot1.name} score: {bot1.check_score()}')
print(f'{bot2.name} score: {bot2.check_score()}')
print(f'{bot3.name} score: {bot3.check_score()}')

if min(whowin, key=whowin.get) == player.name:
    print('Congratulation. You just beaten those useless bots. Good job man!!')
else:
    print("Nice try bro. You have been defeated by those useless bots.\n But that is not mean you are useless (even it seems to be). C'Mon man, keep it up!")
