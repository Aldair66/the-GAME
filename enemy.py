import pygame, caracter,tile



class Enemy(caracter.Caracter):


    def __init__(self, position=(0, 0),index=0):
        super(Enemy, self).__init__(position)
        self.rect = pygame.Rect(7, 8, 20 * 3, 27 * 3)
        self.run_speed= 12
        self.attack_on = False
        self.attack_combo = 1
        self.attack_next = False
        self.hit_box=self.rect
        self.num_jumps = 0
        print(self.hit_box)
        self.limits=(100,400)

        self.set_hit_box(self.rect)
    def ai(self,player,list_tile):
        up, down, left, right, jump, k1, k2=False,False,False,False,False,False,False
        if self.rect.centerx-player.rect.centerx <= 210 and self.rect.centerx-player.rect.centerx >= -210 :
            if self.rect.centerx-player.rect.centerx <= 90 and self.rect.centerx-player.rect.centerx >= -90 :
                left = False
                right = False
                k1=True
            elif self.rect.centerx-player.rect.centerx>0:

                left =True
                right=False

            elif self.rect.centerx-player.rect.centerx <0:

                left =False
                right=True
        else :
            if self.hit_box.right>=self.limits[1]:
                self.side_left = True
            elif self.hit_box.left<=self.limits[0]:
                self.side_left = False


            if self.side_left:
                left=True
                right =False


            else:
                left = False
                right = True





        self.controle(up, down, left, right, jump, k1, k2)

    def controle(self, up, down, left, right, jump, k1, k2):
        # animation
        if self.animation():
            self.attack_on = False
        if (self.attack_next == True and self.attack_on == False) or (self.attack_on != False and (self.frame_on != "attack"  )):
            if self.attack_next == True and self.attack_on == False:
                if right and not left:
                    self.side_left = False
                elif not right and left:
                    self.side_left = True
            if (self.attack_next == True) and self.attack_on == False:
                self.attack_next = False
                self.attack_on = True
                self.attack_combo += 1

                if self.attack_combo == 3:
                    self.attack_combo = 1
            else:
                self.attack_combo = 1
                print(1)

            self.frame_on = "attack"
            print("attack" + str(self.attack_combo))
            self.frame_index = 0



        elif self.movement[1] < 0 and self.frame_on != "jump" and self.attack_on == False:
            self.frame_on = "jump"
            self.frame_index = 0

        elif self.movement[1] > 0 and self.frame_on != "fall" and self.attack_on == False:
            #Hack- probabli gonna delete this
            self.frame_on = "idle"
            self.frame_index = 0

        elif (left or right) and self.frame_on != "run" and self.num_jumps == 0 and self.attack_on == False and self.movement [1]==0 :
            self.frame_on = "run"
            self.frame_index = 0

        elif self.movement[0] == 0 and self.movement[1] == 0 and self.frame_on != "idle" and self.num_jumps == 0 and self.attack_on == False:
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
        if jump and self.num_jumps < 2 and down == False:
            self.movement[1] = -15
            self.num_jumps += 1
        #if down and self.movement[1] == 0 and self.num_jumps == 0 and self.hit_box.height ==27 * 3:
        #    self.hit_box.height = self.hit_box.height / 2
        #    self.hit_box.y += self.rect.height / 2
        #elif not down and self.hit_box.height !=27 * 3:
        #    self.hit_box.y-=self.hit_box.height
        #    self.hit_box.height =27 * 3

        # Side movement
        if right and left:
            if self.movement[0] != 0:
                self.movement[0] = int(self.movement[0] * 0.7)
        elif right and left == False and self.attack_on == False :
            self.side_left = False
            self.movement[0] += 3
            if self.movement[0] >= self.run_speed:
                self.movement[0] = self.run_speed
        elif right == False and left and self.attack_on == False:
            self.side_left = True
            self.movement[0] -= 3
            if self.movement[0] <= -self.run_speed:
                self.movement[0] = -self.run_speed

        else:
            if self.movement!=0:
                self.movement[0] = int (self.movement[0]*0.7)
        # attack

        if k1:
            self.attack_next = True

        if self.attack_next == True and self.attack_on == False:
            self.attack_next = False
            self.attack_on = True
        return



        return False

    def move(self, barreiras):
        # Mudar depois, pq se colidir em duas barreiras do mesmo lado, por exemplo a direita e detectar primeiro a menos aa direita a posisao sera atualizada para a barreiramais a direita, assim atravesando a menos a direita!!!

        # gravidade talvez fique no controle

        self.gravity()


        # mover no y
        self.hit_box.y += self.movement[1]
        # lista das barreiras que colidio

        collisinons = self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[1] < 0:
                self.hit_box.top = barreira.bottom
                self.movement[1] = 0
            if self.movement[1] > 0:
                if True:
                    left = barreira
                    right = barreira
                    done = False

                    while (done == False):
                        for i in barreiras:


                            if i.midright == left.midleft:
                                left = i
                                continue
                        done = True

                    done = False
                    while (done == False):
                        for i in barreiras:
                            if i.midleft == right.midright:
                                right = i
                                continue
                        done = True
                print(self.limits)
                self.hit_box.bottom = barreira.top
                self.movement[1] = 0
                self.num_jumps = 0

        # mover no x
        self.hit_box.x += self.movement[0]
        # lista das barreiras que colidio
        collisinons = self.move_collision(barreiras)
        for barreira in collisinons:
            if self.movement[0] < 0:
                self.hit_box.left = barreira.right
            if self.movement[0] > 0:
                self.hit_box.right = barreira.left
        self.rect.center = self.hit_box.center

        return
    def set_limits(self,tiles,tile):
        left= tile
        right=tile
        done=False
        while (done==False):
            for i in tiles:
                if i.rect.midright==left.midleft:
                    left=i.rect
                    continue
            done =True

        done = False
        while (done == False):
            for i in tiles:
                if i.midleft == right.rect.midright:
                    right = i
                    continue
            done = True




        self.limits=(left.rect.left,right.rect.right)