from queue import PriorityQueue

class AStar:

    def __init__(self, m):
        self.m = m


    def preprocess(self, maze):
        
        maze_map = {}
        grid = []
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                valList = []
                if i < len(maze)-1 and j < len(maze[0])-1 and i > 0 and j > 0:                    
                    for k in "EWNS":
                        if k == 'E':
                            if maze[i][j+1] == 1:
                                valList.append(1)
                            else:
                                valList.append(0)
                        elif k == 'W':
                            if maze[i][j-1] == 1:
                                valList.append(1)
                            else:
                                valList.append(0)

                        elif k == 'S':
                            if maze[i+1][j] == 1:
                                valList.append(1)
                            else:
                                valList.append(0)
                        else:
                            if maze[i-1][j] == 1:
                                valList.append(1)
                            else:
                                valList.append(0)
                    maze_map[(i, j)] = valList

                    

                
                
                
                grid.append((i,j))

        return grid, maze_map



    def h(self, cell1,cell2):
        x1,y1=cell1
        x2,y2=cell2

        return abs(x1-x2) + abs(y1-y2)

    def aStar(self, start, end):
        tempmaze = self.m.copy()
        tempmaze[0] = 0
        tempmaze[len(self.m)-1] = 0
        tempmaze[:,0] = 0
        tempmaze[:,len(tempmaze[0])-1] = 0
        grid, maze_map = self.preprocess(tempmaze)
        end=end
        g_score={cell:float('inf') for cell in grid}
        g_score[end]=0
        f_score={cell:float('inf') for cell in grid}
        f_score[end]=self.h(end,start)

        open=PriorityQueue()
        open.put((self.h(end,start),self.h(end,start),end))
        aPath={}
        while not open.empty():
            currCell=open.get()[2]
            if currCell==start:
                break

            for d in range(4):
                if  maze_map[currCell][d]==True:
                    if d==0:
                        childCell=(currCell[0],currCell[1]+1)
                    if d==1:
                        childCell=(currCell[0],currCell[1]-1)
                    if d==2:
                        childCell=(currCell[0]-1,currCell[1])
                    if d==3:
                        childCell=(currCell[0]+1,currCell[1])

                    temp_g_score=g_score[currCell]+1
                    temp_f_score=temp_g_score+self.h(childCell,start)

                    if temp_f_score < f_score[childCell]:
                        g_score[childCell]= temp_g_score
                        f_score[childCell]= temp_f_score
                        open.put((temp_f_score,self.h(childCell,start),childCell))
                        aPath[childCell]=currCell
        fwdPath={}
        cell=start
        while cell!=end:
            fwdPath[aPath[cell]]=cell
            cell=aPath[cell]
        return fwdPath
