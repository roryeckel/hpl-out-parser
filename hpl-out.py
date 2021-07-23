class LinpackTest:
    START_TEXT = 'T/V                N    NB     P     Q               Time                 Gflops\n'
    def __init__(self, number, tv, n, nb, p, q, time, gflops):
        self.number = number
        self.tv = tv
        self.n = int(n)
        self.nb = int(nb)
        self.p = int(p)
        self.q = int(q)
        self.time = float(time)
        self.gflops = float(gflops)

    def __str__(self):
        return f'Test #{self.number}: {self.tv} {self.n} {self.nb} {self.p} {self.q} {self.time} {self.gflops}'

    @classmethod
    def from_str(cls, number, string):
        string = string.strip()
        assert len(string) == 80
        return cls(number, *string.split(None))

if __name__ == '__main__':
    tests = list()
    with open('Initial.HPL.out', 'r') as f:
        for line in f:
            if line == LinpackTest.START_TEXT:
                next(f)
                tests.append(LinpackTest.from_str(len(tests), next(f)))
    tests.sort(key=lambda test: test.gflops, reverse=True)
    for test in tests:
        print(test)