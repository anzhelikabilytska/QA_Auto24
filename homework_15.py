class rhombus:
    def __init__(self, side_a, angle_a):
        self.set_side(side_a)
        self.set_angle_a(angle_a)

    def set_side(self, side_a):
        if side_a > 0:
            setattr(self, 'side_a', side_a)
        else:
            raise ValueError("The value of side_a must be greater than 0.")

    def set_angle_a(self, angle_a):
        if 0 < angle_a < 180:
            setattr(self, 'angle_a', angle_a)
            setattr(self, 'angle_b', 180 - angle_a)
        else:
            raise ValueError("Angle angle_a must be within (0, 180) degrees.")

    def __repr__(self):
        return f"rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"
