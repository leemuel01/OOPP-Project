import Monster as mm
import MonsterTypes as m
from random import randint

class MonsterGame:
    __cpu_monster = ''
    __player_monster = ''

    def choose_monster(self):
        print('1) Fire\n2) Water\n3) Grass')
        choice = str(input("Please choose a monster (F, W or G):"))
        if choice == 'F':
            MonsterGame.__player_monster = m.FireMonster()
        elif choice == 'W':
            MonsterGame.__player_monster = m.WaterMonster()
        elif choice == 'G':
            MonsterGame.__player_monster = m.GrassMonster()

    def generate_monster(self):
        cpu_choice = randint(1,3)
        if cpu_choice == 1:
            MonsterGame.__cpu_monster = m.FireMonster()
        elif cpu_choice == 2:
            MonsterGame.__cpu_monster = m.WaterMonster()
        elif cpu_choice == 3:
            MonsterGame.__cpu_monster = m.GrassMonster()
        else:
            print('Error! Please enter a valid monster choice')

    def fight(self):
        player_health = MonsterGame.__player_monster.get_health()
        player_def = MonsterGame.__player_monster.get_defence()
        player_atk = MonsterGame.__player_monster.get_attack()
        cpu_health = MonsterGame.__cpu_monster.get_health()
        cpu_atk = MonsterGame.__cpu_monster.get_attack()
        cpu_def = MonsterGame.__cpu_monster.get_defence()
        while True:
            cpu_health -= (player_atk-cpu_def)
            if cpu_health <= 0:
                if cpu_health > player_health:
                    print('You Lose...')
                    break
                elif cpu_health < player_health:
                    print('YOU WIN!!!')
                    break
            player_health -= (cpu_atk-player_def)
            if player_health <= 0:
                if cpu_health > player_health:
                    print('You Lose...')
                    break
                elif cpu_health < player_health:
                    print('YOU WIN!!!')
                    break
            print('CPU: ',MonsterGame.__cpu_monster.get_name(), ' suffers ',player_atk-cpu_def,' damage, the health is ',cpu_health, 'now'
            '\nPlayer: ',MonsterGame.__player_monster.get_name(), ' suffers ',cpu_atk-player_def,' damage, the health is ',player_health, 'now')


    def __init__(self):
        self.choose_monster()
        self.generate_monster()
        if MonsterGame.__player_monster != '':
            #print('fight liao')
            self.fight()



game = MonsterGame()
print(game)
