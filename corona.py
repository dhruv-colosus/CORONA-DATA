
#██████╗░██╗░░██╗██████╗░██╗░░░██╗██╗░░░██╗  ░█████╗░░█████╗░██╗░░░░░░█████╗░░██████╗░██████╗██╗░░░██╗░██████╗
#██╔══██╗██║░░██║██╔══██╗██║░░░██║██║░░░██║  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██║░░░██║██╔════╝
#██║░░██║███████║██████╔╝██║░░░██║╚██╗░██╔╝  ██║░░╚═╝██║░░██║██║░░░░░██║░░██║╚█████╗░╚█████╗░██║░░░██║╚█████╗░
#██║░░██║██╔══██║██╔══██╗██║░░░██║░╚████╔╝░  ██║░░██╗██║░░██║██║░░░░░██║░░██║░╚═══██╗░╚═══██╗██║░░░██║░╚═══██╗
#██████╔╝██║░░██║██║░░██║╚██████╔╝░░╚██╔╝░░  ╚█████╔╝╚█████╔╝███████╗╚█████╔╝██████╔╝██████╔╝╚██████╔╝██████╔╝
#╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░  ░╚════╝░░╚════╝░╚══════╝░╚════╝░╚═════╝░╚═════╝░░╚═════╝░╚═════╝░
#         By Dhruv_Colossus   


import requests
from bs4 import BeautifulSoup
import pygame

pygame.init()
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
#COLORS
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
wonderfull=(90,15,74)
#Main Game Window
Game_Window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Live Corona Tracker")

pygame.display.update()
fps=57
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
font1=pygame.font.SysFont(None,75)
def score_on_screen(text,function,color,x,y):
    screen_text=font.render(text+function,True,color)
    Game_Window.blit(screen_text,[x,y])




def main():
    main="https://www.worldometers.info/coronavirus/"
    req=requests.get(main)

    pars=BeautifulSoup(req.text,"html.parser")

    data=pars.find_all("div",class_="maincounter-number")

    score_on_screen("Total Cases :" ,str(data[0].text.strip()),black,260,250)
    score_on_screen("Total Deaths :" ,str(data[1].text.strip()),black,260,290)
    score_on_screen("Total Recovered :", str(data[2].text.strip()),black,260,330)

def LOOP():
    exit_game=False
    while not exit_game:
        Game_Window.fill((233,10,29))
        main()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                
        pygame.display.update()
        clock.tick(60)

def welcome():
    exit_game = False
    while not exit_game:
        Game_Window.fill((233,10,29))
        score_on_screen("Welcome to Live Corona Virus Tracker ",str(), black, 180, 250)
        score_on_screen("Press Space Bar To Know The DATA",str(), black, 190, 290)
        score_on_screen("By Dhruv_Colosus",str(), black, 252, 335)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    LOOP()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    welcome()        



      