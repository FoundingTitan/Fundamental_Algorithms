
from heapq import *
import sys

def valid_move(x, y, n, m):
	return x >= 0 and x < n and y >= 0 and y < m;

def min_cost_route(grid):

	n = len(grid)
	m = len(grid[0])

	#Possible moves
	dx = [1,-1, 0, 0, 1, 1,-1,-1]
	dy = [0, 0, 1,-1, 1,-1, 1,-1]

	cost_matrix = [[sys.maxsize for _ in range(m)] for _ in range(n)] #Initialize all cost to be maximum
	visited = [[False for _ in range(m)] for _ in range(n)] #Initialize all grid cells to be not visited

	priority_queue = []

	#Add cost of starting position: lowest left corner
	# starting x = n-1
	# starting y = 0
	cost_matrix[n-1][0] = grid[n-1][0]
	heappush(priority_queue, (grid[n-1][0], n-1, 0))

	while(len(priority_queue) > 0):
		cell = heappop(priority_queue)
		cur_x = cell[1]
		cur_y = cell[2]

		if visited[cur_x][cur_y]:
			continue

		visited[cur_x][cur_y] = True

		for i in range(8):
			next_x = cur_x + dx[i]
			next_y = cur_y + dy[i]

			if valid_move(next_x, next_y, n, m) and not visited[next_x][next_y]:
				cost_matrix[next_x][next_y] = min(cost_matrix[next_x][next_y], 
												cost_matrix[cur_x][cur_y] + grid[next_x][next_y])
				heappush(priority_queue, (cost_matrix[next_x][next_y], next_x, next_y))

	#neturn cost of upper right corner
	#end x = 0
	#end y = m-1
	return cost_matrix[0][m-1]

if __name__ == '__main__':

	grids = []

	#read all the grids from keyboard
	current_grid=[]
	n,m = map(int,input().strip().split())
	while n != 0 and m != 0:
		for i in range(0,n):  # where n is the no. of lines you want 
		    current_grid.append([int(m) for m in input().split()])  # for taking m spaced integers as input
		grids.append(current_grid)
		current_grid = []
		n,m = map(int,input().strip().split())

	#Compute the min_cost_route for each grid
	for grid in grids:
		min_cost = min_cost_route(grid)
		print(min_cost)

	
