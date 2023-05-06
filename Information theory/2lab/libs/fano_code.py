from typing import NamedTuple

# ("a", 5467, 7)
class ShannonFanoCode(NamedTuple):
    letter: str
    probability: int
    code: int

    def to_dict(self):
        return self._asdict()


class ShannonFanoGenerator:
    pass
