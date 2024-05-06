import Cell
class SubGrid:
    """ TODO """
    def __init__(self, i, cells=None):
        list_subgrid=[]
        r=0
        q=0
        self.i=i
        self.collected_values=[]
        if cells is None:
            self.grid=[[Cell.Cell(0,0), Cell.Cell(0,1), Cell.Cell(0,2)], [Cell.Cell(1,0), Cell.Cell(1,1), Cell.Cell(1,2)], [Cell.Cell(2,0), Cell.Cell(2,1), Cell.Cell(2,2)]]
        else: 
            for k in range(len(cells)):
                res=cells[k]
                self.collected_values.append(res.values[0])
                if(res.i==0):
                    list_subgrid.append(res.j)
                if(res.i==1):
                    list_subgrid.append(res.j+3)
                if(res.i==2):
                    list_subgrid.append(res.j+6)   
            for m in range (3):
                for n in range (3):
                    if not(r in list_subgrid):
                        list_subgrid.insert(r,Cell.Cell(m,n))   
                    else:
                        list_subgrid.insert(r,cells[q])
                        q=q+1
                    r=r+1               
            self.grid=([[list_subgrid[0],list_subgrid[1],list_subgrid[2]],
                        [list_subgrid[3],list_subgrid[4],list_subgrid[5]],
                        [list_subgrid[6],list_subgrid[7],list_subgrid[8]]])
    
    def update_values(self):
        '''
        The method updates the values_collected list by the cells that are in the same inner square whose value is known
        '''
        for i in range(3):
            for j in range(3):
                if (len(self.grid[i][j].values)==1):
                    if not(self.grid[i][j].values[0] in self.collected_values):
                        self.collected_values.append(self.grid[i][j].values[0])               
                    
    def remove_values(self, cell):
        '''
        The method accepts cell type input and deletes the impossible cell values from the same field's values
        '''
        if (len(cell.values)!=1):       
            for k in self.collected_values:
                for m in cell.values:
                    if (m==k):
                        self.grid[cell.i][cell.j].values.remove(k)
                        break
            self.update_values()
        else:
            self.update_values()
            
    def check_cells_possibilities(self):
        '''
        The method is responsible for updating the field values of all cells of the same internal square
        '''
        for i in range(3):
            for j in range(3):
                self.remove_values(self.grid[i][j])
