import Cell
import SubGrid
class Grid:
    """ TODO """
    def __init__(self, sub_grids=None):
        q=0
        list_subgrid=[]
        self.rows=[[],[],[],[],[],[],[],[],[]]
        self.columns=[[],[],[],[],[],[],[],[],[]]
        if sub_grids is None: 
            self.sub_grids=[SubGrid.SubGrid(0), SubGrid.SubGrid(1), SubGrid.SubGrid(2), SubGrid.SubGrid(3), SubGrid.SubGrid(4), SubGrid.SubGrid(5), SubGrid.SubGrid(6), SubGrid.SubGrid(7), SubGrid.SubGrid(8)]
        else:
            for k in range(len(sub_grids)):
                list_subgrid.append(sub_grids[k].i)  
            for m in range (9):
                if not (m in list_subgrid):
                    list_subgrid.insert(m,SubGrid.SubGrid(m))   
                else:
                    list_subgrid.insert(m,sub_grids[q])
                    q=q+1              
            self.sub_grids=([list_subgrid[0],list_subgrid[1],list_subgrid[2],
                        list_subgrid[3],list_subgrid[4],list_subgrid[5],
                        list_subgrid[6],list_subgrid[7],list_subgrid[8]])    
                    
    def update_values(self):
        '''
        The method updates the rows and columns fields with the known cell values.
        '''
        for i in range(9):
            for j in range(3):
                for k in range(3):
                        a=self.sub_grids[i]
                        b=a.grid[j]
                        c=b[k]
                        if (len(c.values)==1):
                            if (i==0):        
                                if not (c.values[0] in self.rows[j]):
                                    self.rows[j].append(c.values[0])
                                if not (c.values[0] in self.columns[k]):
                                    self.columns[k].append(c.values[0])
                                continue
                            if (i==1): 
                                if not (c.values[0] in self.rows[j]):
                                    self.rows[j].append(c.values[0])
                                if not (c.values[0] in self.columns[k+3]):
                                    self.columns[k+3].append(c.values[0])
                                continue
                            if (i==2):                  
                                if not (c.values[0] in self.rows[j]):
                                    self.rows[j].append(c.values[0])
                                if not (c.values[0] in self.columns[k+6]):
                                    self.columns[k+6].append(c.values[0])
                                continue
                            if (i==3):
                                if not (c.values[0] in self.rows[j+3]):
                                    self.rows[j+3].append(c.values[0])
                                if not (c.values[0] in self.columns[k]):
                                    self.columns[k].append(c.values[0])
                                continue
                            if (i==4):   
                                if not (c.values[0] in self.rows[j+3]):
                                    self.rows[j+3].append(c.values[0])
                                if not (c.values[0] in self.columns[k+3]):
                                    self.columns[k+3].append(c.values[0])
                                continue
                            if (i==5):      
                                if not (c.values[0] in self.rows[j+3]):
                                    self.rows[j+3].append(c.values[0])
                                if not (c.values[0] in self.columns[k+6]):
                                    self.columns[k+6].append(c.values[0])
                                continue
                            if (i==6):                
                                if not (c.values[0] in self.rows[j+6]):
                                    self.rows[j+6].append(c.values[0])
                                if not (c.values[0] in self.columns[k]):    
                                    self.columns[k].append(c.values[0])
                                continue
                            if (i==7):       
                                if not (c.values[0] in self.rows[j+6]):
                                    self.rows[j+6].append(c.values[0])
                                if not (c.values[0] in self.columns[k+3]):
                                    self.columns[k+3].append(c.values[0])
                                continue
                            if (i==8):                 
                                if not (c.values[0] in self.rows[j+6]):
                                    self.rows[j+6].append(c.values[0])
                                if not (c.values[0] in self.columns[k+6]):
                                    self.columns[k+6].append(c.values[0])
                                continue 
   
    def remove_values(self, cell, grid_num):
        '''
        The method deletes the impossible values for the same cell according to the values we have collected so far in the row
        And in the column where the cell is located.
        '''
        x=0
        y=3        
        if (len(cell.values)!=1):
            if(grid_num>2):
                x=x+3
                if(grid_num>5):
                    x=x+3
            if(grid_num==2 or grid_num==5 or grid_num==8):
                y=y+3
            if(grid_num%3==0):
                y=y-3  
            for k in self.rows[cell.i+x]:
                if (k in self.sub_grids[grid_num].grid[cell.i][cell.j].values):
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(k)                          
            for m in self.columns[cell.j+y]:
                if (m in self.sub_grids[grid_num].grid[cell.i][cell.j].values):
                    self.sub_grids[grid_num].grid[cell.i][cell.j].values.remove(m) 
            self.update_values()
        else:
            self.update_values()
            
        
    def check_cells_possibilities(self):
        '''
        We go over all the internal squares, and for each square we call the method
        possibilities_cells_check Then we will call the values_update method
        To update the rows and columns field values. After updating the cell values accordingly
        For the internal squares they belong to, we will go through all the cells in the table, and call the values_remove method
        '''
        for i in range(9):
            SubGrid.SubGrid.check_cells_possibilities(self.sub_grids[i])
        self.update_values()
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    a=self.sub_grids[i]
                    b=a.grid[j]
                    c=b[k]
                    self.remove_values(c,i)
                    
                        
    def is_solved(self):
        '''
        The method returns True if we have finished solving the Sudoku board, otherwise False returns
        '''
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    a=self.sub_grids[i]
                    b=a.grid[j]
                    c=b[k]
                    if (len(c.values)!=1):
                        return False
        return True
    
    def solve(self):
        while (not self.is_solved()):
            self.check_cells_possibilities()
   
    def __repr__(self):
        res = ''
        for i in range(9):
            if i % 3 == 0:
                res = res + '\n\n'
            for j in range(9):
                if j % 3 == 0:
                    res = res + '    '
                res = res + str(self.sub_grids[3 * int(i / 3)+ int(j / 3)].grid[i % 3][j % 3]) + ' '
            res = res + '\n'
        return res
    




