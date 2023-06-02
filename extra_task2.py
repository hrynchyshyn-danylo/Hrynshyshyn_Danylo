

def num_to_ip(num : int) -> str :
    binary_rep = bin(num)[2:]
    if len(binary_rep) > 32 :
        raise ValueError("IP address is not valid, number is too big")
    bit_32 = ('0' * max(0, 32 - len(binary_rep)) + binary_rep)
    bytes = [bit_32[i:i + 8] for i in range(0, len(bit_32), 8)]
    ip = '.'.join([str(int(byte, 2)) for byte in bytes])
    return ip

if __name__ == '__main__':
    assert num_to_ip(2149583361) == "128.32.10.1"
    assert num_to_ip(32) == "0.0.0.32"
    assert num_to_ip(0) == "0.0.0.0"
    assert num_to_ip(sum(2 ** i for i in range(32))) == '255.255.255.255'
    try :
        num_to_ip(sum(2 ** i for i in range(33)))
        raise AssertionError("IP address is not valid, but method works")
    except ValueError :
        pass


