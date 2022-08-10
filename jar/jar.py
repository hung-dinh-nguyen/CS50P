class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size = self.size + n
        else:
            raise ValueError('Too Much Cookie')

    def withdraw(self, n):
        if 0 <= self.size - n:
            self.size = self.size - n
        else:
            raise ValueError('Not Enough Cookies')

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if 0 <= capacity:
            self._capacity = capacity
        else:
            raise ValueError('Capacity cannot be negative')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError('Size cannot be negative or over capacity')

total = Jar()
total.deposit(5)
print(total)


"""
class Jar:
    def __init__(self, capacity=12):
        self.cookies = 0
        if 0 <= capacity:
            self.capacity = capacity
        else:
            raise ValueError('Capacity cannot be negative')


    def __str__(self):
        cookies_str = ""
        while len(cookies_str) < self.cookies:
            coookies_str += '🍪'
        return cookies_str

    def deposit(self, n):
        if self.cookies + n <= self.capacity:
            self.cookies = self.cookies + n
        else:
            raise ValueError('Too Much Cookie')

    def withdraw(self, n):
        if 0 <= self.cookies - n:
            self.cookies = self.cookies - n
        else:
            raise ValueError('Not Enough Cookies')

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

cookies_total = Jar()

cookies_total.deposit(5)

print(cookies_total)
"""