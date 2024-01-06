class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Inavlid Data")
        self.cookies = 0

    def __str__(self):
        return f"🍪" * self.cookies

    def deposit(self, n):
        if n + self.cookies > self.capacity:
            raise ValueError("Invalid")
        self.cookies += n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError("Few Cookies")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies


def main():
    goza = Jar()
    goza.deposit(11)
    print(goza)
    goza.withdraw(10)
    print(goza)


if __name__ == "__main__":
    main()
