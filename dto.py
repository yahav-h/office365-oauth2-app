from dataclasses import dataclass, field, asdict
from pickle import loads

@dataclass
class UserDataTransferObject:
    uid: int = field(init=True)
    user: str = field(init=True)
    token: bytes = field(init=True)
    def decompress_token(self): return loads(self.token)
    def __repr__(self): return "<UserDTO %r>" % asdict(self)
