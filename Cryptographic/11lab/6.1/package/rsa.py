from package.util import extended_euclidean_algorithm, euler_function


class RSA:
    e: int
    d: int
    n: int
    f: int

    def __init__(self, p: int, q: int, e: int = 257) -> None:
        self.n = p * q
        self.e = e
        self.f = euler_function(p, q)
        self.d = extended_euclidean_algorithm(self.f, self.e)[1]

    def encrypt(self, msg: str):
        byte_list = map(ord, msg)

        return list(map(lambda x: pow(x, self.d, self.n), byte_list))

    def decrypt(self, msg: str):
        byte_list = map(ord, msg)

        return list(map(lambda x: pow(x, self.e, self.n), byte_list))
