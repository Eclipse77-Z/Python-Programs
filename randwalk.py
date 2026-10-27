from random import choice

class RandomWalk():
    def __init__(self, num_pnt=5000):
        self.num_pnt =num_pnt
    
        self.x = [0]
        self.y = [0]
    def fill_walk(self):
        while len(self.x)<self.num_pnt:
            x_direction  = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_length = x_direction * x_distance

            y_direction  = choice([1,-1])
            y_distance =  choice([0,1,2,3,4])
            y_length = y_direction * y_distance

            if x_length ==0 and y_length == 0:
                continue
            fol_x = self.x[-1] + x_length
            fol_y = self.y[-1] + y_length

            self.x.append(fol_x)
            self.y.append(fol_y)
            
            
    
