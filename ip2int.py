

def ip_to_int(ipstr):
    # values = [int(k) for k in ipstr.split('.')]
    # values = map(int, ipstr.split('.'))
    # return reduce(lambda x, y: (x << 8) + y, values, 0)

    return reduce(lambda x, y: (x << 8) + int(y), ipstr.split('.'), 0)
