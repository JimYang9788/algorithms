# Graphs 
# 1 Search through a Maze 
# DFS Version
import collections

Coordinate = collections.namedtuple('Coordinate', ('x','y'))
WHITE, BLACK = range(2)


def maze_search (maze, s, e):
    # Returns a path that leads you from start to end 
    # DFS seems the natural way to do it a
    def DFS (cur):
        # Checks if cur is within maze and is a white pixel 
        if not (0 <= cur.x < len (maze) and 0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE:
            return False
        path.append (cur)
        maze[cur.x][cur.y] == BLACK
        if cur == e :
            return True
        return 