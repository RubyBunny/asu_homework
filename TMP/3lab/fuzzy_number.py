class FuzzyNumber:
    """This is FuzzyNumber class"""
    __counter: int = 0
    __x: float
    __xl: float
    __xr: float

    def __init__(self, x: float, xl: float, xr: float):
        self.__class__.__counter += 1
        self.x = x
        self.xl = xl
        self.xr = xr

    def __del__(self):
        self.__class__.__counter -= 1


    @property
    def x(self):
        print("Get x value")
        return self.__x

    @x.setter
    def x(self, value):
        print(f"Set in x new value = {value}")
        self.__x = value

    @property
    def xl(self):
        print("Get xl value")
        return self.__xl

    @xl.setter
    def xl(self, value):
        print(f"Set in xl new value = {value}")
        self.__xl = value

    @property
    def xr(self):
        print("Get xr")
        return self.__xr

    @xr.setter
    def xr(self, value):
        print(f"Set in xr new value = {value}")
        self.__xr = value


    def __add__(self, other):
        """Return sum"""
        return FuzzyNumber(
                self.x + other.x - self.xl - other.xl, 
                self.x + other.x, 
                self.x + other.x + self.xr + other.xr
            )

    def __sub__(self, other):
        """Return substraction"""
        return FuzzyNumber(
                self.x - other.x - self.xl - other.xl,
                self.x - other.x, 
                self.x - other.x + self.xr + other.xr
            )

    def __mul__(self, other):
        """Return multiply"""
        return FuzzyNumber(
                self.x * other.x - other.x * self.xl - self.x * other.xl + self.xl * other.xl,
                self.x * other.x, 
                self.x * other.x + other.x * self.xr + self.x * other.xr + self.xr * other.xr
            )
    
    def __truediv__(self, other):
        """Return divide"""
        if (other.x > 0):
            return FuzzyNumber(
                    (self.x - self.xl) / (other.x - other.xr),
                    self.x / other.x,
                    (self.x + self.xr) / (other.x - other.xl)
                )

    def __repr__(self) -> str:
        return f"({self.x, self.xl, self.xr})"

    def __str__(self) -> str:
        return f"({self.x, self.xl, self.xr})"


    def reverse(self):
        """Return reversed number"""
        if (self.x > 0):
            return FuzzyNumber(
                    1 / (self.x - self.xr),
                    1 / self.x,
                    1 / (self.x - self.xl)
                )

    @classmethod
    def get_counter(cls) -> int:
        """Return FuzzyNumber object count"""
        return cls.__counter


if __name__ == "__main__":
    obj1 = FuzzyNumber(10, 4, 14)
    obj2 = FuzzyNumber(15, 3, 25)

    print(obj1 + obj2)
    print(obj1 - obj2)
    print(obj1 * obj2)
    print(obj1 / obj2)
    print(obj1.reverse())

    print(FuzzyNumber.get_counter())
