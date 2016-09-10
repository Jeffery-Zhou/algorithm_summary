# coding:utf-8
# lesson-12
import random

game_map = [
			['#', 'o', 'x', 'o', 'o', 'x', 'x', 'o', 'o'],
			['o', 'x', 'o', 'x', 'o', 'o', 'o', 'o', 'x'],
			['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o', 'o'],
			['x', 'o', 'x', 'o', 'o', 'o', 'o', 'x', 'x'],
			['o', 'x', 'o', 'x', 'o', 'o', 'x', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'x', 'o', 'x', 'x'],
			['x', 'x', 'o', 'x', 'o', 'o', 'x', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'x', 'x', 'o', 'o'],
			['o', 'o', 'x', 'o', 'o', 'o', 'o', 'x', 'x'],
			]
"""
	"#": snake head
	"@": snake body
	"x": the food can be eaten by snake
"""


snake_body_lst = []	# snake body position

def find_snake_head(lst):	# find the head of the snake "#", and return the position of the head
	head = []
	for i in range(0, len(lst)):
		for j in range(0, len(lst)):
			if lst[i][j] == '#':
				head.append(i)
				head.append(j)
	if head:
		return head
	else:
		print "not found snake head!"
		return None


snake_body_lst.append(find_snake_head(game_map))	# append the snake head into the lst
# snake head -> the second -> the third ->...

def print_game_map(lst, step, snake_lst):
	if snake_lst:
		(x,y) = snake_lst[0]	# set the snake head
		print x,y
		lst[x][y] = '#'
	for (a,b) in snake_lst[1:]:  # set the snake body after the head
		lst[a][b] = '@'
	print "the "+str(step)+" step result:"
	for i in range(0, len(lst)):
		for j in range(0, len(lst[i])):
			print lst[i][j],
		print ''
	print "---- map end ----"
	print ''

def direction(snake_lst):
	# 'all':all direction
	# 'u': up direction: can up,left,right
	# 'd': down direction: can down, left, right
	# 'l': can left, up, down
	# 'r': can right, up, down
	if len(snake_lst) <= 1:
		return 'all'
	else:
		(a, b) = snake_lst[0]	# the first element of the snake (head)
		(c, d) = snake_lst[1]	# the second element of the snake
		# print a,b
		# print c,d
	if b == d & a - 1 == c:
		return 'u'

	if b == d & a + 1 == c:
		return 'd'

	if c == a & d + 1 == b:
		return 'r'

	if c == a & d - 1 == b:
		return 'l'


def UP(lst, snake_lst):
	if direction(snake_lst) == 'd':
		print "Died,game over! ERROR:DIRECTION"
	else :
		head = []
		head = find_snake_head(lst)
		if head:
			print 'head',head
			if head[0] == 0:
				print "Died, game over! ERROR: already TOP"
			elif lst[head[0]-1][head[1]] == 'x':
				snake_lst.insert(0,[head[0]-1,head[1]])
			elif lst[head[0]-1][head[1]] == '@':
				print "Died, game over! ERROR: bite yourself"
			else:
				snake_lst.insert(0,[head[0]-1,head[1]])
				(a,b) = snake_lst.pop()
				lst[a][b] = 'o'

def DOWN(lst, snake_lst):
	if direction(snake_lst) == 'u':
		print "Died, game over! ERROR:DIRECTION"
	else:
		head = []
		head = find_snake_head(lst)
		if head:
			print 'head',head
			if head[0] == 8:
				print "Died! game over! ERROR: already BOTTOM"
				exit(0)
			elif lst[head[0]+1][head[1]] == 'x':
				snake_lst.insert(0, [head[0]+1, head[1]])
			elif lst[head[0]+1][head[1]] == '@':
				print "Died, game over! ERROR: bite yourself"
			else:
				snake_lst.insert(0, [head[0]+1, head[1]])
				(a,b) = snake_lst.pop()
				lst[a][b] = 'o'


def LEFT(lst, snake_lst):
	if direction(snake_lst) == 'r':
		print "Died, game over! ERROR:DIRECTION"
	else:
		head = []
		head = find_snake_head(lst)
		if head:
			print 'head',head
			if head[1] == 0:
				print "Died! game over! ERROR: already BOTTOM"
			elif lst[head[0]][head[1]-1] == 'x':
				snake_lst.insert(0, [head[0], head[1]-1])
			elif lst[head[0]][head[1]-1] == '@':
				print "Died, game over! ERROR: bite yourself"
			else:
				snake_lst.insert(0, [head[0], head[1]-1])
				(a,b) = snake_lst.pop()
				lst[a][b] = 'o'


def RIGHT(lst, snake_lst):
	if direction(snake_lst) == 'l':
		print "Died, game over! ERROR:DIRECTION"
	else:
		head = []
		head = find_snake_head(lst)
		if head:
			print 'head',head
			if head[1] == 8:
				print "Died! game over! ERROR: already BOTTOM"
			elif lst[head[0]][head[1]+1] == 'x':
				snake_lst.insert(0, [head[0], head[1]+1])
			elif lst[head[0]][head[1]+1] == '@':
				print "Died, game over! ERROR: bite yourself"
			else:
				snake_lst.insert(0, [head[0], head[1]+1])
				(a,b) = snake_lst.pop()
				lst[a][b] = 'o'

print_game_map(game_map, 0, snake_body_lst)

def do(operationStr, lst, snake_lst):
	j = 1;
	for i in operationStr:
		if i == 'l' or 'L':
			LEFT(lst, snake_lst)
		if i == 'r' or 'R':
			RIGHT(lst, snake_lst)
		if i == 'u' or 'U':
			UP(lst, snake_lst)
		if i == 'd' or 'D':
			DOWN(lst, snake_lst)
		print 'Snake body', snake_lst
		print_game_map(lst, j, snake_lst)
		j += 1


do('DDDdddRrRrRRr', game_map, snake_body_lst)











