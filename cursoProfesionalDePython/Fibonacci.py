class Fibonacci():
    
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n0 = 0
        self.n1 = 1
        self.aux = 0
        return self

    def __next__(self):
        if not self.max or self.aux < self.max:
            if self.aux == 0:
                self.aux += 1 
                return self.n0
            elif self.aux == 1:
                self.aux += 1 
                return self.n1
            else:
                self.result = self.n0 + self.n1
                self.n0, self.n1 = self.n1, self.result
                self.aux += 1
                return self.result
        else:
            raise StopIteration