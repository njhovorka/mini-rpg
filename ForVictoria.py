import pygame
import random

pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption('For Victoria')


idle_list = [[pygame.image.load('images/heavy_idle1.png'), pygame.image.load('images/heavy_idle1.png'), pygame.image.load('images/heavy_idle2.png'), pygame.image.load('images/heavy_idle2.png')] , \
             [pygame.image.load('images/captain_idle1.png'), pygame.image.load('images/captain_idle1.png'), pygame.image.load('images/captain_idle2.png'), pygame.image.load('images/captain_idle2.png')], \
             [pygame.image.load('images/engineer_idle1.png'), pygame.image.load('images/engineer_idle1.png'), pygame.image.load('images/engineer_idle2.png'), pygame.image.load('images/engineer_idle2.png')], \
             [pygame.image.load('images/bot_idle1.png'), pygame.image.load('images/bot_idle1.png'), pygame.image.load('images/bot_idle2.png'), pygame.image.load('images/bot_idle2.png')], \
             [pygame.image.load('images/rifler_idle1.png'), pygame.image.load('images/rifler_idle1.png'), pygame.image.load('rimages/ifler_idle2.png'), pygame.image.load('images/rifler_idle2.png')], \
             [pygame.image.load('images/alchemist_idle1.png'), pygame.image.load('images/alchemist_idle1.png'), pygame.image.load('images/alchemist_idle2.png'), pygame.image.load('images/alchemist_idle2.png')]]
             
firing_list = [[pygame.image.load('images/heavy_firing1.png'), pygame.image.load('images/heavy_firing2.png'), pygame.image.load('images/heavy_firing1.png'), pygame.image.load('images/heavy_firing2.png')], \
               [pygame.image.load('images/captain_firing1.png'), pygame.image.load('images/captain_firing2.png'), pygame.image.load('images/captain_firing1.png'), pygame.image.load('images/captain_firing2.png')], \
               [pygame.image.load('images/engineer_firing1.png'), pygame.image.load('images/engineer_firing2.png'), pygame.image.load('images/engineer_firing1.png'), pygame.image.load('images/engineer_firing2.png')], \
               [pygame.image.load('images/bot_firing1.png'), pygame.image.load('images/bot_firing2.png'), pygame.image.load('images/bot_firing1.png'), pygame.image.load('images/bot_firing2.png')],\
               [pygame.image.load('images/rifler_firing1.png'), pygame.image.load('images/rifler_firing1.png'), pygame.image.load('images/rifler_firing2.png'), pygame.image.load('images/rifler_firing1.png')], \
               [pygame.image.load('images/alchemist_firing1.png'), pygame.image.load('images/alchemist_firing2.png'), pygame.image.load('images/alchemist_firing1.png'), pygame.image.load('images/alchemist_firing2.png')]]

action_list = ["Pick Action: 'a', 'h', 's'", "Pick Target: 1-4"]

hp_list = [20, 20, 20, 20]
enemy_idle = []
enemy_firing = []
action_count = 0
bg = pygame.image.load('images/background.png')

fighter_pick = pygame.image.load('images/fighter_pick.png')
invalid_pic = pygame.image.load('images/invalid_pic.png')
clock = pygame.time.Clock()
tick_count = 0

invalid = False
combat_page = False
reinforcement_text = False
fighter_list = []
fighters = []
target_list = []
y_lineup = 30
x_lineup = 30
setup = True
run = True
enemy_setup = False
combat_buffer = False
turn_pick = False
turn_pick_buffer = False
target_pick = False
combat =False
delay = 0
turn_attack = False
turn_heal = False
turn_special = False
hp_list = []
bot_count = 4
death_delay = [False, False, False, False]
death_count = 0
rifler_buff = False
heavy_buff = False
alchemist_buff = False
captain_buff = False
engineer_buff = False
bot_choice = ['a', 'd', 'b']

class fighter(object):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        self.x = x
        self.y = y
        self.name = name
        self.width = width
        self.height = height
        self.idle = True
        self.firing = False
        self.tick_count = 0
        self.idle_index = idle_index
        self.firing_index = firing_index
        self.hp = 10
        self.dead = False
        self.defend = False
        self.delay = False
        self.rifler_buff = False
        self.heavy_buff = False
        self.alchemist_buff = False
        self.captain_buff = False
        self.engineer_buff = False
        

    def draw(self, win):
        
        if self.tick_count == 3:
            if self.idle:
                win.blit(idle_list[self.idle_index][self.tick_count], (self.x, self.y))
            elif self.firing:
                win.blit(firing_list[self.firing_index][self.tick_count], (self.x, self.y))
                        
            self.tick_count = 0
            
        elif self.idle:
            win.blit(idle_list[self.idle_index][self.tick_count], (self.x, self.y))
            self.tick_count += 1

        elif self.firing:
            win.blit(firing_list[self.firing_index][self.tick_count], (self.x, self.y))
            self.tick_count += 1

        if self.captain_buff:
            pygame.draw.rect(win, (255, 0, 0), (self.x - 5, self.y + 40, 4, 4))
        if self.rifler_buff:
            pygame.draw.rect(win, (0, 0, 255), (self.x - 5, self.y + 45, 4, 4))
        if self.heavy_buff:
            pygame.draw.rect(win, (0, 255, 0), (self.x - 5, self.y + 50, 4, 4))
        if self.engineer_buff:
            pygame.draw.rect(win, (255, 255, 0), (self.x - 5, self.y + 55, 4, 4))
        if self.alchemist_buff:
            pygame.draw.rect(win, (255, 0, 255), (self.x - 5, self.y + 60, 4, 4))
            
    def heal(self, target):
        healed_person = (fighters[target - 1])
        healed_person_2 = (fighters[random.randint(0, 3)])
        healed_person.hp += 1
        if self.name == 'alchemist':
            healed_person.hp += 1
        if self.captain_buff:
            heal = [10]
            for x in fighters:
                try:
                    if x.hp < heal[0].hp:
                        heal[0] = x
                except:
                    heal[0] = 10
            healed_person_2.hp = heal[0]
            
            if self.name == 'alchemist':
                healed_person_2.hp += 1

            self.captain_buff = False
        
        return
    
    def attack(self, target):
        if self.idle_index == 3:
            attacked_person = (fighters[target - 1])
            attacked_person.hp -= 1
            if attacked_person.rifler_buff:
                self.hp -= 2
                attacked_person.rifler_buff = False
                
            if attacked_person.heavy_buff:
                attacked_person.hp += 1
                attacked_person.heavy_buff = False
        elif self.idle_index != 3:
            attacked_person = (fighters[target + 3])
                
        
            attacked_person.hp -= 1
            
            if self.engineer_buff:
                attacked_person.hp -= 2
                self.engineer_buff = False
                    
            if self.idle_index == 4 and self.rifler_buff:
                attacked_person.hp -= 1
                self.rifler_buff = False
            
            if self.captain_buff:
                attacked_person = (fighters[random.randint(0,3)])
                attacked_person.hp -= 1
                self.captain_buff = False
        
        return

class bot(fighter):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        fighter.__init__(self, x, y, width, height, name, idle_index, firing_index)
    def __repr__(self):
        return(self.name)
    def buff(self, target):
        return

class alchemist(fighter):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        fighter.__init__(self, x, y, width, height, name, idle_index, firing_index)
        
    def __repr__(self):
        return(self.name)

    def special(self, target):
        fighters[target - 1].alchemist_buff = True

        return
        

class heavy(fighter):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        fighter.__init__(self, x, y, width, height, name, idle_index, firing_index)
        
    def __repr__(self):
        return(self.name)

    def special(self, target):
        fighters[target - 1].heavy_buff = True
        return


class captain(fighter):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        fighter.__init__(self, x, y, width, height, name, idle_index, firing_index)

    def __repr__(self):
        return(self.name)
    
    def special(self, target):
        fighters[target - 1].captain_buff = True
        return

class engineer(fighter):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        fighter.__init__(self, x, y, width, height, name, idle_index, firing_index)

    def __repr__(self):
        return(self.name)

    def special(self, target):
        fighters[target - 1].engineer_buff = True
        return

class rifler(fighter):
    def __init__(self, x, y, width, height, name, idle_index, firing_index):
        fighter.__init__(self, x, y, width, height, name, idle_index, firing_index)

    def __repr__(self):
        return(self.name)

    def special(self, target):
        fighters[target - 1].rifler_buff = True
        return


enemy_list = [bot(385, 25, 96, 96, 'Bot No. 1', 3, 3), bot(385, 130, 96, 96, 'Bot No. 2', 3, 3), \
              bot(385, 240, 96, 96, 'Bot No. 3', 3, 3), bot(385, 340, 96, 96, 'Bot No. 4', 3, 3)]

def drawWindow():
    global tick_count
        
    win.blit(bg, (0,0))
    if not setup:
        for x in fighters:
            if x.hp > 0 and (not x.delay):
                x.draw(win)

    if setup:
        win.blit(fighter_pick, (130, 450))

    if reinforcement_text:
        text = font.render('reinforcement: Bot No. ' + str(bot_count), 1, (255,255,255))
        win.blit(text, (125,15))

    if turn_pick or target_pick:
        turn_text = font.render(action_list[action_count], 1, (255,255,255))
        win.blit(turn_text, (125,450))
        
    hp_x = 10
    hp_y = 45
    enemy_x = 475
    if len(fighters) >= 4:
        hp_list = [fighters[0].hp, fighters[1].hp, fighters[2].hp, fighters[3].hp]
        for k in hp_list:
            text = font.render(str(k) , 1, (0,0,0))
            win.blit(text, (hp_x, hp_y))
            hp_y += 105
        hp_y = 45
        for k in fighters:
            if k.idle_index == 3:
                enemy_text = font.render(str(k.hp) , 1, (0,0,0))
                win.blit(enemy_text, (enemy_x, hp_y))
                hp_y += 105
            

    pygame.display.update()


#Main Loop--------------------------------------------------
font = pygame.font.SysFont('comicsans', 30, True)
while run:
    
    keys = pygame.key.get_pressed()
    if setup:
        invalid = False
        if keys[pygame.K_c]:
            fighter_list.append('c')   
        if keys[pygame.K_h]:
            fighter_list.append('h')
        if keys[pygame.K_e]:
            fighter_list.append('e')
        if keys[pygame.K_r]:
            fighter_list.append('r')
        if keys[pygame.K_a]:
            fighter_list.append('a')
            
        if len(fighter_list) == 4:
            turn_pick_buffer = True
          
            setup = False
            
            for x in fighter_list:
                if x == 'h':
                    new = heavy(x_lineup, y_lineup, 96, 96, 'heavy', 0, 0)
                    fighters.append(new)

                if x == 'a':
                    new = alchemist(x_lineup, y_lineup, 96, 96, 'alchemist', 5, 5)
                    fighters.append(new)

                if x == 'r':
                    new = rifler(x_lineup, y_lineup, 96, 96, 'rifler', 4, 4)
                    fighters.append(new)
                    
                if x == 'e':
                    new = engineer(x_lineup, y_lineup, 96, 96, 'engineer', 2, 2)
                    fighters.append(new)

                if x == 'c':
                    new = captain(x_lineup, y_lineup, 96, 96, 'captain', 1, 1)
                    fighters.append(new)

                y_lineup += 105


            for x in enemy_list:
                fighters.append(x)
                x.hp = 8

    if combat:

        for x in fighters:
            x.idle = False
            x.firing = True
            if turn_attack and x.idle_index == 2:
                x.idle = True
                x.firing = False
        delay += 1
        if delay == 10:
            for k in fighters:
                if k.idle_index == 3 and not k.delay:
                    choice = bot_choice[random.randint(0,2)]
                    if choice == 'd':
                        k.defend = True
                    if choice == 'a':
                        k.attack(random.randint (1,4))
                    if choice == 'b':
                        k.buff(random.randint(1,4))
                    
            #automate bot!
            if turn_attack:
                for x in fighters:
                    if x.idle_index != 3 and x.idle_index != 2:
                        x.attack(target_list[0])
                        if x.idle_index == 0:
                            x.attack(target_list[0])
                    elif x.idle_index == 2 and x.captain_buff:
                        x.attack(target_list[0])


            if turn_heal:
                for x in fighters:
                    if x.idle_index != 0 and x.idle_index != 3:
                        x.heal(target_list[0])
                    elif x.idle_index == 0:
                        x.heal(fighters.index(x) + 1)
                        if x.hp > 10:
                            x.hp = 10
                            
            for x in fighters:
                if x.hp > 10:
                    x.hp = 10  

            if turn_special:
                for k in fighters:
                    if k.idle_index != 3:
                        k.special(target_list[0])
                        if k.alchemist_buff:
                            valid = False
                            while not valid:
                                index = random.randint(0,3)
                                if index != target_list:
                                    valid = True
                                    k.special(index)
                                    alchemist_buff = False
            
            for k in fighters:
               
                if k.delay:
                    k.delay = False
                if k.hp <= 0:
                    if k.idle_index == 3:
                        bot_count += 1
                        new_bot = bot(k.x, k.y, 96, 96, ('Bot No: ' + str(bot_count)), 3, 3)
                        fighters[fighters.index(k)] = new_bot
                        new_bot.hp = 4 + bot_count
                        #new_bot.hp = 8 for not scaling
                        new_bot.tick_count = fighters[0].tick_count
                        reinforcement_text = True
                        new_bot.delay = True
                    else:
                        del(fighters[fighters.index(k)])
            
                        
                    
                k.idle = True
                k.firing = False
                
            target_list = []
            combat = False
            turn_attack = False
            turn_heal = False
            turn_special = False
            turn_pick = True
            delay = 0
            
            
    if target_pick:
        action_count = 1
        if keys[pygame.K_1]:
            target_list.append(1)   
        if keys[pygame.K_2]:
            target_list.append(2)   
        if keys[pygame.K_3]:
            target_list.append(3)
        if keys[pygame.K_4]:
            target_list.append(4)

        if len(target_list) == 1:
            combat = True
            target_pick = False
            

    if turn_pick:
        
                
                
        action_count = 0
        if keys[pygame.K_a]:
            turn_pick = False
            turn_attack = True
            target_pick = True

        if keys[pygame.K_h]:
            turn_pick = False
            turn_heal = True
            target_pick = True
            

        if keys[pygame.K_s]:
            turn_pick = False
            turn_special = True
            target_pick = True
        
    if turn_pick_buffer:
        turn_pick = True
        turn_pick_buffer = False
        
    tick_count += 1
    clock.tick(4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    
    main_menu = True

    drawWindow()
    
pygame.quit()


