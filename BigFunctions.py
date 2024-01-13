class BigFuncClass:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __repr__(self):
        return f'{self.__class__.__name__}({self.attr1}, {self.attr2})'

    def __str__(self):
        return f'{self.attr1} - {self.attr2}'

    def __len__(self):
        return len(f'{self.attr1}{self.attr2}')

    def __add__(self, other):
        self.attr1 += other.attr1
        self.attr2 += other.attr2

    def __call__(self, *args, **kwargs):
        print(f'Был вызван объект {self}')

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self):
            self.current_value += 1
            return str(self)[self.current_value]
        else:
            raise StopIteration

    def __enter__(self):
        self.fp = open(self.attr1, self.attr2)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


bfc1 = BigFuncClass('1', '2')
bfc2 = BigFuncClass('3', '4')
