import pygame, caracter


class Player(caracter.Caracter):
    frame={}
    sound = {}
    def __init__(self, position=(0, 0)):

        # maybe u can make the rect_attack evry time o attack
        super(Player, self).__init__(position)
        self.rect = Player.frame[self.frame_on][self.frame_index].get_rect(topleft=position)
        self.attack_on = False
        self.attack_combo = 1
        self.attack_next = False
        self.hit_box = pygame.Rect(position[0], position[1], 21 * 3, 40 * 3)
        self.reload=0
        self.hp=850
        self.hp_max = 850

        self.num_jumps = 0
        self.death=False
        self.test_mode=False
        self.block=0
        self.roll_on=False
        self.grab_on = True


        # \ self.rect.width -= 13

        return

    # This funtion is to controle the player movement, changes the side (for the img) , the atribute movement is list where [x_movement , y_movement]

    def controle(self, up, down, left, right, jump, k1, k2,k3):
        print(self.num_jumps)
#-------------------------------------------------------
        if up:
            jump=True
#----------------------------------------------------------

        # animation
        if self.animation():

            if self.roll_on:
                self.hit_box.y -= 20 * 3
                self.hit_box.height = 40 * 3
            elif self.grab_on:
                self.frame_index=4
            self.attack_on = False
            self.roll_on= False





        if self.hp==0 and self.frame_on != "death":
            self.frame_on = "death"
            self.frame_index = 0
            #Player.sound[self.frame_on].play()
        elif ((self.attack_next == True and self.attack_on == False) or (self.attack_on != False and (
                self.frame_on != "attack1" and self.frame_on != "attack2" and self.frame_on != "attack3") ))and self.hp!=0 and self.roll_on==False and self.grab_on==False:
            if self.attack_next == True and self.attack_on == False:
                if right and not left:
                    self.side_left = False
                elif not right and left:
                    self.side_left = True
            if (self.attack_next == True) and self.attack_on == False:
                self.attack_next = False
                self.attack_on = True
                self.attack_combo += 1

                if self.attack_combo == 4:
                    self.attack_combo = 1
            else:
                self.attack_combo = 1
                print(1)

            self.frame_on = "attack" + str(self.attack_combo)
            self.frame_index = 0

            self.play_sound()
#---------------------------------------------------------------------------------------------

            self.reload = 12

#---------------------------------------------------------------------------------------------
        elif self.frame_on!="grab" and self.grab_on :

            self.frame_on = "grab"
            self.frame_index = 0


        elif self.roll_on== True and self.frame_on!="roll" and self.attack_on ==False and self.frame_on!="death"and not self.grab_on :
            print( self.frame_on)

            self.frame_on = "roll"
            self.frame_index = 0

        elif self.movement[1] < 0 and self.frame_on != "jump" and self.attack_on == False and self.frame_on != "death" and self.roll_on==False:
            self.frame_on = "jump"
            self.frame_index = 0
            self.play_sound()

        elif self.movement[1] > 0 and self.frame_on != "fall" and self.attack_on == False and self.frame_on != "death" and self.roll_on==False:
            self.frame_on = "fall"
            self.frame_index = 0
        elif k2  and self.frame_on!="block idli" and  self.attack_on == False and self.frame_on != "death" and self.roll_on==False:
            self.frame_on = "block idli"
            self.frame_index = 0
        #elif k3  and self.frame_on!="roll" and  self.attack_on == False and self.frame_on != "death":
        #    self.frame_on = "roll"
        #    self.frame_index = 0


        elif ((left and not right) or (not left and right)) and self.frame_on != "run" and self.num_jumps == 0 and self.attack_on == False and self.movement [1]==0  and self.frame_on != "death" and self.block==0 and self.roll_on==False and not self.grab_on:#and self.hit_box.height ==27 * 3:
            self.frame_on = "run"
            self.frame_index = 0
            self.play_sound()

        elif  self.movement[0] == 0 and self.movement[1] == 0 and self.frame_on != "idle" and self.num_jumps == 0 and self.attack_on == False and self.frame_on != "death" and self.block==0 and self.roll_on==False and not self.grab_on:#and self.hit_box.height ==27 * 3
            self.frame_on = "idle"
            self.frame_index = 0


        #       if self.attack_next == 1 :
        #          if self.attack_on==1 :
        #             self.attack_end = 0
        #            self.attack_on=0
        #           self.img_on = "attack"+str(self.attack_combo)
        #          self.attack_combo=+1
        #         if self.attack_combo>3:
        #            self.attack_combo=1

        # if u take the "and down ==False something happends"
        if jump and self.num_jumps < 2 and down == False and self.roll_on==False:
            self.grab_on=False
            self.movement[1] = -17
            self.num_jumps += 1
       # if down and self.movement[1] == 0 and self.num_jumps == 0 and self.hit_box.height ==27 * 3:
       #     self.hit_box.height = self.hit_box.height / 2
       #     self.hit_box.y += self.rect.height / 2
       # elif not down and self.hit_box.height !=27 * 3:
       #     self.hit_box.y-=self.hit_box.height
       #     self.hit_box.height =27 * 3

        # Side movement
        if right and left:
            if self.movement[0] != 0:
                self.movement[0] = int(self.movement[0] * 0.7)
        elif right and left == False and self.attack_on == False and self.frame_on!="die" and self.block==0 and self.roll_on==False:# and self.hit_box.height ==27 * 3:
            if self.side_left and self.grab_on:
                self.grab_on=False
            self.side_left = False
            if k2==False:
                self.movement[0] += 3
                if self.movement[0] >= self.run_speed:
                    self.movement[0] = self.run_speed
        elif right == False and left and self.attack_on == False and self.block==0 and self.roll_on==False:# and self.hit_box.height ==27 * 3:
            if not self.side_left and self.grab_on:
                self.grab_on=False
            self.side_left = True
            if k2==False:
                self.movement[0] -= 3
                if self.movement[0] <= -self.run_speed:
                    self.movement[0] = -self.run_speed



        else:
            if self.movement!=0 and self.roll_on==False:
                self.movement[0] = int (self.movement[0]*0.7)

        if self.roll_on and self.attack_on==False:
            if self.side_left:
                self.movement[0] -= 3
                if self.movement[0] <= -self.run_speed *1.5:
                    self.movement[0] = -self.run_speed*1.5
            else:
                self.movement[0] += 3
                if self.movement[0] >= self.run_speed*1.5:
                    self.movement[0] = self.run_speed*1.5

        if k3 and not self.attack_on and not self.roll_on and self.block==0:
            self.hit_box.y+=32*3
            self.hit_box.height = 8 * 3
            self.roll_on = True
        # attack


        if k1 :

            self.attack_next = True


        if self.attack_next == True and self.attack_on == False:

            self.attack_next = False
            self.attack_on = True

        if k2:
            self.block+=1
            print(self.block)
        else:
            self.block=0

        return

    def attack(self, hit_box,screen=None,camera=[0,0]):
        if self.attack_on :

            self.reload-=1
            if self.reload==0:

                attack_range = pygame.Rect(10, 10, 100, 100)
                if self.side_left:
                    attack_range.midright = self.hit_box.midleft
                else:
                    attack_range.midleft = self.hit_box.midright
  # I need to know in what side they got hit on

                return hit_box.colliderect(attack_range)

    def draw(self, screen, camera=(0, 0)):
        if self.roll_on:
            self.rect.center=(self.hit_box.centerx,self.hit_box.centery-66)
        else:
            self.rect.center = (self.hit_box.centerx, self.hit_box.centery-15)

        screen.blit(pygame.transform.flip(Player.frame[self.frame_on][int(self.frame_index)], self.side_left, False),(self.rect.x - camera[0], self.rect.y - camera[1]))

        if self.test_mode:
            rect=pygame.Surface(self.hit_box.size).convert_alpha()
            rect.fill((200,0,0,100))
            screen.blit(rect, (self.hit_box.x - camera[0], self.hit_box.y - camera[1]))
            if self.attack_on and self.reload==0:
                attack_range = pygame.Rect(10, 10, 100, 100)
                attack_range_surface = pygame.Surface(attack_range.size).convert_alpha()
                attack_range_surface.fill((250, 150, 71, 100))
                if self.side_left:
                    attack_range.midright = self.hit_box.midleft
                else:
                    attack_range.midleft = self.hit_box.midright

                screen.blit(attack_range_surface,(attack_range.x - camera[0], attack_range.y - camera[1]))
    def animation(self):


        self.frame_index += 13*(1/40)
        if len(Player.frame[self.frame_on])<= int(self.frame_index):
            self.frame_index = 0
            if self.frame_on=="death" and self.hp==0:
                self.frame_index=9
            return True
        return False
    def play_sound(self):
        Player.sound[self.frame_on].play()

    def damage(self,damage_points):
        if self.block>0 and self.block<15:
            self.play_sound()
        elif self.block>15:
            super(Player, self).damage(int(damage_points/2))
        else:
            super(Player, self).damage(damage_points)

            self.movement[1] = -4

    def move(self, barreiras):
        # Mudar depois, pq se colidir em duas barreiras do mesmo lado, por exemplo a direita e detectar primeiro a menos aa direita a posisao sera atualizada para a barreiramais a direita, assim atravesando a menos a direita!!!

        # gravidade talvez fique no controle



        self.gravity()

        # mover no y

        if self.grab_on:
            self.movement[1]=0

        self.hit_box.y += self.movement[1]
        # lista das barreiras que colidio

        collisinons = self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[1] < 0:
                self.hit_box.top = barreira.rect.bottom
                self.movement[1] = 0
            if self.movement[1] > 0:
                self.hit_box.bottom = barreira.rect.top
                self.movement[1] = 0
                self.num_jumps = 0

        # mover no x
        self.hit_box.x += self.movement[0]
        # lista das barreiras que colidio
        collisinons = self.move_collision(barreiras)

        for barreira in collisinons:
            if self.movement[0] < 0:
#--------------------------------------------------------------------------------------------------

                if self.grab_on==False and(self.frame_on=="fall" or self.frame_on=="jump") and self.hit_box.top-barreira.rect.top<6 and self.hit_box.top-barreira.rect.top>-2 and (barreira.index==10 or barreira.index==4 or barreira.index==15):
                    self.grab_on=True
                    self.num_jumps=0
                    self.hit_box.topleft = barreira.rect.topright

                else:
                    self.hit_box.left = barreira.rect.right
            elif self.movement[0] > 0:
                if self.grab_on==False and(self.frame_on=="fall" or self.frame_on=="jump") and self.hit_box.top-barreira.rect.top<6 and self.hit_box.top-barreira.rect.top>-2 and (barreira.index==10 or barreira.index==4 or barreira.index==15):
                    self.grab_on=True
                    self.num_jumps = 0
                    self.hit_box.topright = barreira.rect.topleft
                else:
                    self.hit_box.right = barreira.rect.left
        self.rect.center = self.hit_box.center

        return
    def move_collision(self, barreiras):
        collision = []

        for barreira in barreiras:

            if self.hit_box.colliderect(barreira.rect):
                collision.append(barreira)
        return collision

