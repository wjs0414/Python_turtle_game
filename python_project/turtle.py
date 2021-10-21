import pygame
import random
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("turtle")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background1 = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/background.png")
background2 = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/background02.png")

#거북이 손(바위)
turtle_rock = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/rock01.png")
turtle_rock_size = turtle_rock.get_rect().size
turtle_rock_width = turtle_rock_size[0]
turtle_rock_height = turtle_rock_size[1]
turtle_rock_x_pos = (screen_width/3)-(turtle_rock_width/2)
turtle_rock_y_pos = screen_height-turtle_rock_height*1.2
#거북이 손(가위)
turtle_scissor = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/scissor01.png")
turtle_scissor_size = turtle_scissor.get_rect().size
turtle_scissor_width = turtle_scissor_size[0]
turtle_scissor_height = turtle_scissor_size[1]
turtle_scissor_x_pos = (screen_width/2)-(turtle_scissor_width/2)
turtle_scissor_y_pos = screen_height-turtle_scissor_height*1.2

#거북이 손(보자기)
turtle_paper = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/paper01.png")
turtle_paper_size = turtle_paper.get_rect().size
turtle_paper_width = turtle_paper_size[0]
turtle_paper_height = turtle_paper_size[1]
turtle_paper_x_pos = (screen_width/3*2)-(turtle_paper_width/2)
turtle_paper_y_pos = screen_height-turtle_paper_height*1.2

#결승선
finishline = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/finishline.png")
finishline_size = finishline.get_rect().size
finishline_width = finishline_size[0]
finishline_height = finishline_size[1]
finishline_x_pos =screen_width-finishline_width*2
finishline_y_pos=screen_height-finishline_height

#토끼 길
load1 = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/load001.png")
load1_size = load1.get_rect().size
load1_width = load1_size[0]
load1_height = load1_size[1]
load1_x_pos = 0
load1_y_pos = finishline_y_pos+ load1_height/2

#거북이 길
load2 = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/load002.png")
load2_size = load2.get_rect().size
load2_width = load2_size[0]
load2_height = load2_size[1]
load2_x_pos=0
load2_y_pos = turtle_rock_y_pos - load2_height*1.3

#거북이
turtle = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/turtle01.png")
turtle_size=turtle.get_rect().size #이미지 크기 저장
turtle1_width = turtle_size[0] #가로 크기
turtle_height= turtle_size[1] #세로 크기
turtle_x_pos = 0
turtle_y_pos = load2_y_pos+(load2_height/2)-(turtle_height/2)



#토끼
rabbit = pygame.image.load("C:/Users/우지수/Desktop/python workplace/python_project/image/rabbit01.png")
rabbit_size=rabbit.get_rect().size #이미지 크기 저장
rabbit_width = rabbit_size[0] #가로 크기
rabbit_height= rabbit_size[1] #세로 크기
rabbit_x_pos = 0 #화면의 맨 왼쪽
rabbit_y_pos = load1_y_pos+(load1_height/2)-(rabbit_height/2) #길 중앙


#거북이 가위바위보 버튼
class button():
    def __init__(self,  x,y,width,height, text=''):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text


    def isOver(self, pos):
        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    


turtle_rock_button = button(turtle_rock_x_pos,turtle_rock_y_pos,turtle_rock_width,turtle_rock_height,"바위")
turtle_scissor_button = button(turtle_scissor_x_pos,turtle_scissor_y_pos,turtle_scissor_width,turtle_scissor_height,"가위")
turtle_paper_button = button(turtle_paper_x_pos,turtle_paper_y_pos,turtle_paper_width,turtle_paper_height,"보")

#폰트
game_font = pygame.font.Font(None,40) #폰트 객체 생성(폰트,크기)

game_result = "game over"

turtle_to_x=0
rabbit_to_x=0
running = True
while running:
    dt = clock.tick(30)
    #화면에 그리기
    screen.blit(background1,(0,finishline_y_pos))
    screen.blit(background2,(0,0))
    screen.blit(load1,(load1_x_pos,load1_y_pos))
    screen.blit(load2,(load2_x_pos,load2_y_pos))
    screen.blit(finishline,(finishline_x_pos,finishline_y_pos))
    screen.blit(turtle,(turtle_x_pos,turtle_y_pos))
    screen.blit(rabbit,(rabbit_x_pos,rabbit_y_pos))
    screen.blit(turtle_scissor,(turtle_scissor_x_pos,turtle_scissor_y_pos))
    screen.blit(turtle_rock,(turtle_rock_x_pos,turtle_rock_y_pos))
    screen.blit(turtle_paper,(turtle_paper_x_pos,turtle_paper_y_pos))

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            rabbit_hand = random.choice(["scissor","rock","paper"])    
            rabbit_choice = game_font.render("rabbit: "+rabbit_hand ,True,(255,255,255))
            screen.blit(rabbit_choice,(15,15))
            pygame.display.update()
            pygame.time.delay(1000)

            #거북이가 바위를 고른 경우
            if turtle_rock_button.isOver(pos):                
                
                if rabbit_hand == "rock":
                    turtle_x_pos+=10
                    rabbit_x_pos+=10
                    pygame.time.delay(1000)
                                      
                elif rabbit_hand == "paper":
                    
                    rabbit_x_pos+=60
                    if turtle_x_pos >0 :
                        turtle_x_pos -= 30
                        if turtle_x_pos<30 :
                            turtle_x_pos =0
                    pygame.time.delay(1000)
                                      
                elif rabbit_hand == "scissor":
                    
                    turtle_x_pos +=60
                    if rabbit_x_pos >0:
                        rabbit_x_pos -=30
                        if rabbit_x_pos<30 :
                            rabbit_x_pos =0
                    pygame.time.delay(1000)
                    
           
            #거북이가 가위를 고른 경우
            elif turtle_scissor_button.isOver(pos):
                
                if rabbit_hand == "scissor":
                   turtle_x_pos+=10
                   rabbit_x_pos+=10
                   pygame.time.delay(1000)
                elif rabbit_hand == "rock":
                    
                    rabbit_x_pos+=60
                    if turtle_x_pos >30 :
                        turtle_x_pos -= 30
                        if turtle_x_pos<30 :
                            turtle_x_pos =0

                    pygame.time.delay(1000)
 
                elif rabbit_hand == "paper":
                    
                    turtle_x_pos +=60
                    if rabbit_x_pos >0:
                        rabbit_x_pos -=30
                        if rabbit_x_pos<30 :
                            rabbit_x_pos =0
                    pygame.time.delay(1000)
            
            #거북이가 보를 고른 경우
            elif turtle_paper_button.isOver(pos):
                

                if rabbit_hand == "paper":
                   turtle_x_pos+=10
                   rabbit_x_pos+=10
                   pygame.time.delay(1000)
                   
   
                elif rabbit_hand == "scissor":
                    
                    rabbit_x_pos+=60
                    if turtle_x_pos >0 :
                        turtle_x_pos -= 30
                        if turtle_x_pos<30 :
                            turtle_x_pos =0
                    pygame.time.delay(1000)
                    
      
                elif rabbit_hand == "rock":
                    
                    turtle_x_pos +=60
                    if rabbit_x_pos >0:
                        rabbit_x_pos -=30
                        if rabbit_x_pos<30 :
                            rabbit_x_pos =0
                    pygame.time.delay(1000)
    
    # 충돌 처리
    turtle_rect = turtle.get_rect()
    turtle_rect.left = turtle_x_pos #실제로 캐릭터가 화면상에서 위치하고 있는 곳으로 업데이트
    turtle_rect.top = turtle_y_pos

    rabbit_rect = rabbit.get_rect()
    rabbit_rect.left = rabbit_x_pos
    rabbit_rect.top = rabbit_y_pos

    finishline_rect = finishline.get_rect()
    finishline_rect.left = finishline_x_pos
    finishline_rect.top = finishline_y_pos

    if turtle_rect.colliderect(finishline_rect) or rabbit_rect.colliderect(finishline_rect):
        if turtle_rect.colliderect(finishline_rect):
            game_result = "turtle win"
        else:
            game_result = "rabbit win"
        running = False


    pygame.display.update()

#게임 결과 중앙에 텍스트
msg = game_font.render(game_result,True,(255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2),int(screen_height/2))) #화면 중앙
screen.blit(msg,msg_rect)
pygame.display.update()
pygame.time.delay(2000) 

pygame.quit()