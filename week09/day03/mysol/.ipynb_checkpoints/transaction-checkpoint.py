import json


class Transaction:

    def __init__(self,
                 from_address: str,
                 to_address: str,
                 amount: float,
                 version_no: str = "1") -> None:
        self.version_no = version_no
        self.from_address = from_address
        self.to_address = to_address

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def __repr__(self) -> str:
        return "Transaction(" +\
            f"version_no={self.version_no}, " +\
            f"from_address={self.from_address}, " +\
            f"to_address={self.to_address}" +\
            ")"


def main():
    t1 = Transaction(from_address="0",
                     to_address="1",
                     amount=0.1)
    print(t1)
    print(t1.to_json())


if __name__ == "__main__":
    main()