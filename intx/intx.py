class intx:
    def __init__(self, arg, base: int = 10):
        if isinstance(arg, (int, str, intx, float)):
            if base != 10:
                self.val = int(str(arg), base)
            else:
                self.val = int(arg)
            self.itercur = 0
        elif isinstance(arg, (tuple, list, set)):
            if base != 10:
                total = ""
                for i in arg:
                    total += str(int(i, base))
                self.val = int(total)
            else:
                total = ""
                for i in arg:
                    total += str(int(i))
                self.val = int(total)

        else:
            raise ValueError(
                f"Tried intx({arg})\n{arg} has to be int, intx, str, float, list, tuple or set\nWas: {type(arg)}")

    def __int__(self):
        return self.val

    # Operators

    def __add__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val + int(other))

    def __radd__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val + int(other))

    def __sub__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val - int(other))

    def __rsub__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(intx(other).__sub__(self))

    def __mul__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val * int(other))

    def __rmul__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(int(other) * self.val)

    def __truediv__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val / int(other))

    def __rtruediv__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(int(other) / self.val)

    def __floordiv__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val // int(other))

    def __rfloordiv__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(int(other) // self.val)

    def __mod__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(self.val % int(other))

    def __rmod__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(other % self.val)

    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, intx)):
            raise TypeError(f"Can't use {type(power)} as intx")
        return intx(self.val ** int(power))

    def __rpow__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return intx(int(other) ** self.val)

    def __eq__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return self.val == int(other)

    def __ne__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return self.val != int(other)

    def __lt__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return self.val < int(other)

    def __le__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return self.val <= int(other)

    def __gt__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return self.val > int(other)

    def __ge__(self, other):
        if not isinstance(other, (int, intx)):
            raise TypeError(f"Can't use {type(other)} as intx")
        return self.val >= int(other)

    def __neg__(self):
        return intx(-self.val)

    def __index__(self):
        return self.val

    # Representers

    def __repr__(self):
        return f"{self.val}x"

    def __str__(self):
        return str(self.val)

    # Own

    def __and__(self, other):
        return intx(str(self) + str(other))

    def __rand__(self, other):
        return intx(str(other) + str(self))

    def __or__(self, other):
        # remainder div
        return self.val // int(other), self.val % int(other)

    def __ror__(self, other):
        return int(other) // self.val, int(other) % self.val

    def __len__(self):
        return len(str(self.val))

    def __iter__(self):
        self.itercur = 0
        return self

    def __next__(self):
        if self.itercur < len(self):
            self.itercur += 1
            return intx(str(self.val)[self.itercur - 1])
        raise StopIteration

    def hasNext(self):
        return self.itercur < len(self)

    def __reversed__(self):
        total = ""
        for i in self:
            total = str(i) + total
        return intx(total)

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start if item.start is not None else 0
            stop = item.stop if item.stop is not None else len(self)
            step = item.step if item.step is not None else 1
            total = []
            if start == stop:
                return None
            for i in range(start, stop, step):
                total.append(self[i])
            return intx(total)
        else:
            return intx(str(self.val)[item])

    def isEven(self):
        return self.val % 2 == 0

    def isOdd(self):
        return self.val % 2 != 0

    def isPrime(self):
        n = self.val
        if n == 2 or n == 3:
            return True, None
        if n == 0:
            return False, intx(0)
        if n == 1:
            return False, intx(1)
        if n % 2 == 0:
            return False, intx(2)
        if n < 9:
            return True, None
        if n % 3 == 0:
            return False, intx(3)
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False, intx(f)
            if n % (f + 2) == 0:
                return False, intx(f + 2)
            f += 6
        return True, None

    def dividers(self):
        total = []
        for i in range(1, (self.val // 2) + 1):
            if self.val % i == 0:
                total.append(intx(i))
        total.append(intx(self.val))
        return total

    def split(self, base: int = 10):
        num = self // base
        new = str(self % base)
        while num != 0:
            new += str(num % base)
            num //= base

        total = ""
        for i in range(len(new) - 1, -1, -1):
            if int(new[i]) != 0:
                total += f"({new[i]} * ({base} ^{i})) + "
            else:
                pass
                #total += "0 + "
        return total[:-3]

    def pysplit(self, base: int = 10):
        num = self // base
        new = str(self % base)
        while num != 0:
            new += str(num % base)
            num //= base

        total = ""
        for i in range(len(new) - 1, -1, -1):
            if int(new[i]) != 0:
                total += f"({new[i]} * ({base} **{i})) + "
        return total[:-3]

    def insert(self, pos: int, num):
        if self.val is None:
            raise IndexError("Empty intx")
        lis = list(str(self.val))
        lis.insert(pos, str(int(num)))
        self.val = int("".join(lis))

    def append(self, num):
        self.val = int(str(self.val) + str(int(num)))

    def pop(self, index: int):
        lis = list(str(self.val))
        out = lis.pop(index)
        self.val = int("".join(lis))
        return out

    def remove(self, num: int):
        for i, x in enumerate(self):
            if x == num:
                val = self[:i]
                val2 = self[i+1:]
                if val is None:
                    if val2 is None:
                        raise ValueError("Can't have empty intx")
                    self.val = self[i+1:]
                elif val2 is None:
                    if val is None:
                        raise ValueError("Can't have empty intx")
                    self.val = self[:i]
                else:
                    self.val = self[:i] & self[i + 1:]
                return i

    @staticmethod
    def fibo(length):
        if length == 0:
            return [intx(0)]
        elif length == 1:
            return [intx(0), intx(1)]
        fibolist = [intx(0), intx(1)]
        i = 0
        while i + 2 < length + 1:
            fibolist.append(fibolist[i] + fibolist[i + 1])
            i += 1
        return fibolist

    @staticmethod
    def fibonum(num):
        return intx((((1 + (5 ** 0.5)) ** num) - ((1 - (5 ** 0.5)) ** num)) / ((2 ** num) * (5 ** 0.5)))

    @staticmethod
    def seval(calc):
        for i in calc:
            if i not in "0123456789+-*/()^=!<> ":
                raise ValueError("Unsafe expression")
        return intx(eval(calc))