import random
class MyLightCycleBot(LightCycleBaseBot):

    def get_next_step(self, arena, x, y, direction):
        # arena.shape[0] is the arena width
        # arena.shape[1] is the arena height
        # arena[x,y] is your current position
        #return random.choice(['N','W','E','S'])
        posibles = self.pos_movs(arena,x,y,direction)
        
        if len(posibles) != 0:
            if direction in posibles:
                return direction #prioriza la linea recta
            return random.choice(posibles) #elige uno de los movimientos posibles
                                           #ToDo: debería hacer una pequenia busqueda sobre la
                                           #arena para determinar cual movimiento es mejor, por ejemplo
                                           #para no entrar en una zona cerrada de pocos movimientos
        else: 
            return direction #pierde pero tal vez choca de frente y empata
        
    def pos_movs(self,arena,x,y,direction):
        movs = ['N','S','W','E']
        
        #para que no vuelva sobre su luz
        if direction == 'N': movs.remove('S')
        elif direction == 'S': movs.remove('N')
        elif direction == 'E': movs.remove('W')
        else: movs.remove('E')
        
        #para que no pise el borde del tablero
        if y == arena.shape[1]-1 and 'S' in movs: movs.remove('S')
        if y == 1 and 'N' in movs: movs.remove('N')
        if x == arena.shape[0]-1 and 'E' in movs: movs.remove('E')
        if x == 1 and 'W' in movs: movs.remove('W')

        #para que no pise ninguna traza
        if 'E' in movs: #con esto y el filtro anterior evitamos el error
            if arena[x+1,y]!= 0: movs.remove('E')
        if 'W' in movs:
            if arena[x-1,y]!= 0: movs.remove('W')
        if 'S' in movs:
            if arena[x,y+1]!= 0: movs.remove('S')
        if 'N' in movs:
            if arena[x,y-1]!= 0: movs.remove('N')
        
        return movs
