class Cell:
    """ TODO """
    def __init__(self, i, j, value=None):
        self.i=i
        self.j=j
        if value is None:
            self.values=[1,2,3,4,5,6,7,8,9]
        else:
            self.values=[value]
                        
    def __repr__(self):
        if len(self.values) == 1:
            return str(self.values[0])
        return '_'
    
