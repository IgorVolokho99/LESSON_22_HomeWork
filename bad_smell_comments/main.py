class Unit:
    def __init__(self, field, state, speed = 1):
        self.field = field
        self.state = state
        self.speed = speed

    def move(self, x_coord: int, y_coord: int, direction, ):
        if self.state == "crawl":
            self.speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + self.speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - self.speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - self.speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + self.speed
        else:
            self.speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + self.speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - self.speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - self.speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + self.speed

            self.field.set_unit(x=new_x, y=new_y, unit=self)
