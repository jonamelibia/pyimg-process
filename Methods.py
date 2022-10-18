from Read import Read


from Read import Read
import numpy as np
class Methods(Read):

    def __init__(self):
        super().__init__()
    

    def resize(self, img, output_size):
        new_x = output_size[0]
        new_y = output_size[1]
        x = len(img)     
        y = len(img[0])  
        new = [[ img[int(x * r / new_x)][int(y * c / new_y)] for c in range(new_y)] for r in range(new_x)]
        return np.array(new)