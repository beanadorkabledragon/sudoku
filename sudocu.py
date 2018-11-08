#!/usr/bin/env python
# -*- coding:utf-8 -*-

background_image_filename = "1.jpg"
mouse_image_filename = "2.png"

# 导入pygame库
import pygame
# 导入pygame中的函数和常量
from pygame.locals import *
# 使用sys中的exit函数
from sys import exit

import time

#初始化
pygame.init()

#设置屏幕
screen = pygame.display.set_mode((600,600))
#设置标题
pygame.display.set_caption("Hello World")
sx = (600-460)/2
x1 = sx
y1 = 5
width = 0
color = (0,0,0)
sw = 460
sh = 460
sy = 5
x2 = 82
y2 = sh+20
bgcolor = (173,173,173)
bgrect = (0,0,600,600)
sgcolor = (255,255,255)
bordercolor = (128,128,128)
intervalnumber1 = 51
intervalnumber2 = 52
color1 = (0,0,0)
color2 = (173,173,173)
rectwidth = 35
rectinterval = 45
font = pygame.font.Font("Cousine-Bold.ttf",32)
font2 = pygame.font.Font("Cousine-Regular.ttf",16)
fontwidth2,fontheight2 = font2.size("1")
fontwidth,fontheight = font.size("1")
fontwin = pygame.font.SysFont("华文彩云",64,bold=True)
pencilscreen = pygame.image.load("6.png").convert_alpha()
imagewidth,imageheight = pencilscreen.get_size()
fontcolor = (0,0,255)
fontcolor1 = (0,0,255)
fontcolor2 = (255,102,0)
control = -1
rectcolor = (255,255,255)
originrcolor = (255,255,255)
mousex = 0
mousey = 0
test = False
therectx = []
therecty = []
mod = 8
theerectx = 0
theerecty = 0
question = [[1,0,0,0,6,9,4,0,0],
			[6,0,0,0,2,1,0,5,0],
			[0,0,2,8,0,4,0,9,0],
			[0,0,0,0,8,0,5,0,0],
			[0,0,4,2,0,7,3,0,0],
			[2,0,6,4,0,5,7,0,0],
			[0,0,0,3,0,2,0,0,0],
			[4,0,0,0,7,0,0,0,0],
			[0,1,8,9,0,6,2,0,5]]
ti = -1
tti = -1
answer = [0 for i in range(81)]
draft = [[0 for i in range(9)]for j in range(81)]
res = -1
case = 0
check1 =[[0 for i in range(9)]for j in range(9)]
check2 =[[0 for i in range(9)]for j in range(9)] 
check3 =[[0 for i in range(9)]for j in range(9)]
wrong = [[0 for i in range(9)]for j in range(9)]
win = 0
delete = 0
ansormark = [[0 for i in range(9)]for j in range(9)]
# 函数内要引入全局变量，需要定义global
# 有要给全局变量赋值的地方，需要提前把全局变量定义为global，例如：79行，81行，84行，85行 
# 如果只是使用全局变量，并不需要给全局变量赋值的话，不需要定义global ，例如：80行（color1），85行（intervalnumber2）
def rel(i):
	global width,color,x1,y1
	if i==2 or i==5:
		width = 2
		color = color1
	else:
		width = 1
		color = color2
	if i == 3 or i == 6:
		x1 = x1 + intervalnumber2
		y1 = y1 + intervalnumber2
	else:
		x1 = x1 + intervalnumber1
		y1 = y1 + intervalnumber1
def drawlines():
	global x1,y1
	for i in range(8):
		rel(i)
		pygame.draw.line(screen,color,(x1,5),(x1,sy+sh),width)
		pygame.draw.line(screen,color,(sx,y1),(sx+sw,y1),width)
	x1 = sx
	y1 = sy
def drawrects():
	global therectx,therecty,theerectx,theerecty,x1,y1
	for l in range(9):
		for ll in range(9):
			therectx.append(x1)
			therecty.append(y1)

			if ll==3 or ll ==6:
				pygame.draw.rect(screen,(255,255,255),(x1,y1,50,50))	
			else:
				pygame.draw.rect(screen,(255,255,255),(x1,y1,50,50))
			if ll == 0 or ll == 2 or ll == 5:
				x1 += 52
			else:
				x1 +=  51
		x1 = sx
		if l == 0 or l==2 or l==5:
			y1 +=  52
		else:
			y1 +=  51
	x1 = sx
	y1 = sy
def mousepress():
	global mousex,mousey,mod,tti,theerectx,theerecty,case,ansormark
	if pygame.mouse.get_pressed()[0] :
		mousex,mousey = pygame.mouse.get_pos()
		for q in range(81):
			if pygame.Rect(therectx[q],therecty[q],50,50).collidepoint(mousex,mousey)==True :
				mod = 1
				theerectx = therectx[q]
				theerecty = therecty[q]
				tti = q
	if mod == 1 :
		pygame.draw.rect(screen,(238,232,170),(theerectx,theerecty,50,50))
def definedcheck():
	global check1,check2,check3,question
	for i in range(9):
		for j in range(9):
			if question[i][j] > 0:
				check1[i][j] = question[i][j]
			if question[j][i] > 0:
				check2[i][j] = question[j][i]
			if question[(i//3)*3+j//3][(i%3)*3+j%3] > 0:	
				check3[i][j] = question[(i//3)*3+j//3][(i%3)*3+j%3]
def drawquestion():
	global ti,tti,therectx,therecty
	for i in range(9):
		for j in range(9) :
			ti = ti + 1
			if wrong[i][j] == True:	
				fontrender = font.render(str(question[i][j]),True,(255,0,0))
			else:
				fontrender = font.render(str(question[i][j]),True,(0,0,0))
			if question[i][j] > 0:
				if ti != tti : 
					pygame.draw.rect(screen,(226,226,226),(therectx[ti],therecty[ti],50,50))
				screen.blit(fontrender,(therectx[ti]+(50 - fontwidth)/2,therecty[ti]+(50 - fontheight)/2))
	ti = -1
def drawanswerandmark():
	global res,control,ti,tti,answer,theerectx,theerecty,delete,draft
	# print(ansormark[0][2])
	# print(control)
	if control > -1 and question[tti//9][tti%9] == 0:
		if ansormark[tti//9][tti%9] == 0:
			answer[tti] = control+1
			check1[tti//9][tti%9] = control+1
			check2[tti%9][tti//9] = control+1
			check3[(tti//9//3)*3+tti%9//3][(tti//9%3)*3+tti%9%3] = control+1
			control=-1
		if ansormark[tti//9][tti%9] == 1:
			draft[tti][control] = control+1
			control = -1
	
	for i in range(81):
		if ansormark[i//9][i%9] == 0:	
			if answer[i] > 0:
				if delete == 1:
					answer[i] = 0
					check1[i//9][i%9] = 0
					check2[i%9][i//9] = 0
					check3[((i//9)//3)*3+(i%9)//3][((i//9)%3)*3+(i%9)%3] = 0
					delete = 0
				if wrong[i//9][i%9] == True:
					fontrender = font.render(str(answer[i]),True,(255,0,0))
				else:
					fontrender = font.render(str(answer[i]),True,(0,0,255))
				screen.blit(fontrender,(therectx[i]+(50 - fontwidth)/2,therecty[i]+(50 - fontheight)/2))
		if ansormark[i//9][i%9] == 1:	
			for j in range(9):
				if draft[i][j] > 0:
					fontrender = font2.render(str(draft[i][j]),True,(0,0,255))	
					screen.blit(fontrender,(therectx[i]+(50//3*((draft[i][j]-1)%3)+(50//3-fontwidth2)//2),therecty[i]+(50//3*((draft[i][j]-1)//3)+(50//3-fontheight2)//2)))
# def drawmark():
# 	global control,draft
# 	print(ansormark[tti//9][tti%9])
# 	print(control)
# 	if control > -1 and question[tti//9][tti%9] == 0:
# 		draft[tti][control] = control+1
# 		control=-1
# 		for i in range(81):
# 			for j in range(9):
# 				if ansormark[i//9][j] == 1:
# 					if draft[i][j] > 0:
# 						fontrender = font2.render(str(draft[i][j]),True,(0,0,255))
# 						screen.blit(fontrender,(therectx[i]+(50//3*((draft[i][j]-1)%3)+(50//3-fontwidth2)//2),therecty[i]+(50//3*((draft[i][j]-1)//3)+(50//3-fontheight2)//2)))
def drawequip():
	global rectcolor,fontcolor,x2,y2
	for j in range(10):
		if case == 1 and j == 9:
			rectcolor = fontcolor2
		else:
			rectcolor = originrcolor
		pygame.draw.rect(screen,rectcolor,(x2,y2,rectwidth,rectwidth))
		if control == j:
			fontcolor = fontcolor2
		else:
			fontcolor = fontcolor1
		fontrender = font.render(str(j+1),True,fontcolor)
		if j!=9:	
			screen.blit(fontrender,(x2+(rectwidth - fontwidth)/2,y2+(rectwidth - fontheight)/2))
		else:
			screen.blit(pencilscreen,(x2+(rectwidth - imagewidth)/2,y2+(rectwidth - imageheight)/2))
		x2 = x2 + rectinterval
	x2 = 82
	y2 = sh+20
	pygame.draw.rect(screen,bordercolor,(sx-1,sy-1,sw+2,sh+2),1)
def checkanswer():
	global check1,check2,check3,question,tti,control,wrong
	wrong = [[0 for i in range(9)]for j in range(9)]
	for i in range(9):
		for j in range(9):
			if check1[i].count(j+1) > 1:
				for x in range(9):
					if check1[i][x] == j+1:
						wrong[i][x] = True
			if check2[i].count(j+1) > 1:
				for x in range(9):
					if check2[i][x] == j+1:
						wrong[x][i] = True
			if check3[i].count(j+1) > 1:
				for x in range(9):
					if check3[i][x] == j+1:
						wrong[(i//3)*3+x//3][(i%3)*3+x%3] = True
def checkwin():
	fontrender = fontwin.render("恭喜你答对了 ",True,(0,255,0))
	global win
	win = True
	for i in range(9):
		if check1[i].count(0) > 0 or check2[i].count(0) > 0 or check3[i].count(0) > 0 or wrong[i].count(True) > 0:
			win = False
			break
	if win == True:
		screen.blit(fontrender,(100,240))
	

definedcheck()
while True:
	for event in pygame.event.get():
		if event.type == QUIT :
			exit()
		if event.type == KEYDOWN:
			if event.key == K_1:
				control = 0
			if event.key == K_2:
				control = 1
			if event.key == K_3:
				control = 2
			if event.key == K_4:
				control = 3
			if event.key == K_5:
				control = 4
			if event.key == K_6:
				control = 5
			if event.key == K_7:
				control = 6
			if event.key == K_8:
				control = 7
			if event.key == K_9:
				control = 8
			if event.key == K_w:
				if case == 1:
					case = 0
				elif case == 0:
					case = 1
				ansormark[tti//9][tti%9] = case		
			if event.key == K_0:
				delete = 1

	pygame.draw.rect(screen,bgcolor,bgrect)
	pygame.draw.rect(screen,sgcolor,(sx,sy,sw,sh))

	drawlines()
	
	drawrects()

	mousepress()

	drawquestion()

	drawequip()
	
	drawanswerandmark()

	checkanswer()

	checkwin()

	pygame.display.update()