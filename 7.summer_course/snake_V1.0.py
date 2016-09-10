# coding:utf-8
# lesson-12
import random

game_map = [
			['*', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
			]

# 打印game_map
def print_game_map(lst, step):
	print '================== '+"第"+str(step)+"步操作后结果"+' ================'
	for i in range(0, len(lst)):
		for j in range(0, len(lst[i])):
			print lst[i][j],
		print ''
	print "================== map end =================="
	print ''

# print_game_map(game_map)

def set_block(lst):
	for i in range(0,10):
		a = random.randint(0, len(lst)-1)
		b = random.randint(0, len(lst)-1)
		if a == 0 & b == 0:
			pass
		else:
			lst[a][b] = 'x'

set_block(game_map)
print_game_map(game_map, 0)
# 要求：定义四个方法，碰到x就吃掉，置成'o'
	
def find_star(lst):
	for i in range(0, len(lst)):
		for j in range(0, len(lst)):
			if lst[i][j] == '*':
				return i,j



# def find_x(lst):
# 	for i in range(0, len(lst)):
# 		for j in range(0, len(lst)):
# 			if lst[i][j] == '*':
# 				return i,j

position_star = [0, 0]

def up(lst_map):
	# lst_map:地图
	# lst_star:'*'位置
	# a = lst_star[0]
	# b = lst_star[1]
	a = find_star(lst_map)[0]
	b = find_star(lst_map)[1]
	if a == 0:
		print 'you die, game over!'
	else:
		if lst_map[a-1][b] == 'x':
			print "吃了一个x"
			lst_map[a-1][b] = '*'
			lst_map[a][b] = 'o'
			print '向上移动一步'

		else:
			lst_map[a-1][b] = '*'
			lst_map[a][b] = 'o'
			print '向上移动一步'




# position_star = up(game_map, position_star)

def down(lst_map):
	# lst_map:地图
	# lst_star:'*'位置
	# a = lst_star[0]
	# b = lst_star[1]
	a = find_star(lst_map)[0]
	b = find_star(lst_map)[1]
	if a == 8:
		print 'you die, game over!'
	else:
		if lst_map[a+1][b] == 'x':
			print "吃了一个x"

			lst_map[a+1][b] = '*'
			lst_map[a][b] = 'o'
			print '向下移动一步'

		else:
			lst_map[a+1][b] = '*'
			lst_map[a][b] = 'o'
			print '向下移动一步'




def left(lst_map):
	# lst_map:地图
	# lst_star:'*'位置
	# a = lst_star[0]
	# b = lst_star[1]
	a = find_star(lst_map)[0]
	b = find_star(lst_map)[1]
	if b == 0:
		print 'you die, game over!'
	else:
		if lst_map[a][b-1] == 'x':
			print "吃了一个x"

			lst_map[a][b-1] = '*'
			lst_map[a][b] = 'o'
			print '向左移动一步'

		else:
			lst_map[a][b-1] = '*'
			lst_map[a][b-1] = 'o'
			print '向左移动一步'



def right(lst_map):
	# lst_map:地图
	# # lst_star:'*'位置
	# a = lst_star[0]
	# b = lst_star[1]
	a = find_star(lst_map)[0]
	b = find_star(lst_map)[1]
	if b == 8:
		print 'you die, game over!'
	else:
		if lst_map[a][b+1] == 'x':
			print "吃了一个x"

			lst_map[a][b+1] = '*'
			lst_map[a][b] = 'o'
			print '向右移动一步'

		else:
			lst_map[a][b+1] = '*'
			lst_map[a][b] = 'o'
			print '向右移动一步'



# u d l r
# input: 'udlrrldu' -> up  down  down  left right right down

# def down(lst):
# def left(lst):
# def right(lst):

def to_do_list(action_str, lst_map):
	step_count = 1
	for action in action_str:
		if action == 'u':
			up(lst_map)
			print_game_map(lst_map, step_count)
		if action == 'd':
			down(lst_map)
			print_game_map(lst_map, step_count)
		if action == 'l':
			left(lst_map)
			print_game_map(lst_map, step_count)
		if action == 'r':
			right(lst_map)
			print_game_map(lst_map, step_count)
		step_count += 1

action_lst = 'ddddddddrrrrrrrr'
to_do_list(action_lst, game_map)




















