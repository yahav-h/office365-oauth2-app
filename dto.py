from dataclasses import dataclass, field, asdict

@dataclass
class UserDataTransferObject:
    uid: int = field(init=True)
    user: str = field(init=True)
    token: bytes = field(init=True)
    def __repr__(self): return "<UserDTO %r>" % asdict(self)
