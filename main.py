import pygame
import random
import math
import time
from pygame import mixer



pygame.init()

screen = pygame.display.set_mode((850,700))
pygame.display.set_caption('BrickBreak')

background = pygame.image.load('wallpaper.png')
mixer.music.load('farm.wav')
mixer.music.play(-1)




ballimage = pygame.image.load('futbol.png')
#baller = pygame.font.Font('freesansbold.ttf', 32)
ballx = 320
bally = 550
ballx_change = 0.5
bally_change = 0.5
def ball(x,y):
	#ballimage = baller.render('o',True,(255,0,0))
	screen.blit(ballimage, (x,y))



boardimage = pygame.image.load('board.png')
boardx = 320
boardy = 600
boardx_change = 0
boardy_change = 0
def board(x,y):
	screen.blit(boardimage,(x,y))



brickimage = []
brickx = [random.randrange(0,110),random.randrange(160,270),random.randrange(320,430),random.randrange(480,590),random.randrange(640,760),random.randrange(350,450),random.randrange(0,110),random.randrange(160,270),random.randrange(320,430),random.randrange(480,590),random.randrange(640,760),random.randrange(250,350)]
bricky = [random.randrange(10,100),random.randrange(10,100),random.randrange(10,100),random.randrange(10,100),random.randrange(10,100),random.randrange(240,300),random.randrange(110,250),random.randrange(110,250),random.randrange(110,250),random.randrange(110,250),random.randrange(110,250),random.randrange(240,300)]
brick_number  = 12

for i in range(brick_number):
	brickimage.append(pygame.image.load('brick.png'))

def brick(x,y,i):
	screen.blit(brickimage[i],(x,y))
	 

#ox,oy = cord of ball----- tx,ty = cord of object ----- lx,ux = upper lower limit of x ---- ly,uy = lower upper limit of y
def collision(ox,oy,tx,ty,lx,ux,ly,uy):
	if int(ox) in range(int(tx-lx),int(tx+ux)) and int(oy) in range(int(ty-ly),int(ty+uy)):
		return True
	return False


gameov = pygame.font.Font('freesansbold.ttf', 64)
def game_over(x,y):
	over = gameov.render('YOU LOSE XX',True, (0,255,255))
	screen.blit(over, (x, y))


winning = pygame.font.Font('freesansbold.ttf', 64)
def win(x,y):
	over = winning.render('  YOU WIN <3',True, (0,255,255))
	screen.blit(over, (x, y))




game = True
while game:
	screen.fill((200,200,200))
	screen.blit(background, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				boardx_change = -1

			if event.key == pygame.K_RIGHT:
				boardx_change = 1


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				boardx_change = 0



	for j in range(brick_number):
		collide = collision(ballx,bally,brickx[j],bricky[j],10,64,-10,44)
		if collide:
			bricky[j] = 2000
			bally_change *= -1
			hitsound = mixer.Sound('breakhit.wav')
			hitsound.play()

		brick(brickx[j],bricky[j],j)

		if bally >= 700:
			game_over(200,300)
			
			break

		if len(set(bricky)) == 1:
			win(200,300)
			ballx_change = 0
			bally_change = 0
			
			



	










	ballx += ballx_change
	bally += bally_change
	if ballx <= 10:
		ballx_change = 0.8
	elif ballx >= 800:
		ballx_change = -0.8
	if bally <= 10:
		bally_change = 0.8
	#if int(ballx) in range(int(boardx-30),int(boardx+134)) and int(bally) in range(int(boardy)+35,int(boardy+40)):
		#bally_change = -0.2
	if collision(ballx,bally,boardx,boardy,20,130,-35,40):

		bally_change = -0.8
		padsound = mixer.Sound('spraysound.wav')
		padsound.play()
	ball(ballx,bally)

	







	boardx += boardx_change
	if boardx <= 5:
		boardx = 5
	elif boardx >=720:
		boardx = 720
	board(boardx,boardy)







	pygame.display.update()

