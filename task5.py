
def meeting(s):
    s = s.upper()
    s = s.split(';')
    s = [i.split(':') for i in s]
    s = sorted(s, key=lambda x: (x[1], x[0]))
    s = ''.join([f'({i[1]}, {i[0]})' for i in s])
    return s


if __name__ == '__main__':
    assert meeting("Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill") == \
          "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"