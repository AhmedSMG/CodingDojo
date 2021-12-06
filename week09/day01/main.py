import hashlib
import datetime as dt


def find_hash(x=7):
    t1 = dt.datetime.now()
    nonce = 0
    while True:
        _hash = hashlib.sha256(str(nonce).encode()).hexdigest()
        if _hash[:x] == "0" * x:
            t2 = dt.datetime.now()
            break
        else:
            nonce += 1
    duration = t2 - t1
    print("The hash is:", _hash)
    print("The nonce is:", nonce)
    print("Time elapsed:", duration)


if __name__ == "__main__":
    find_hash()
    find_hash(8)