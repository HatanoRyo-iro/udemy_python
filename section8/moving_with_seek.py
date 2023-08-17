with open('section8/test.txt', 'r') as f:
    print(f.tell())
    """
    こういう感じになってる
    
    0123
    AAA
    
    4567
    BBB
    
    891011
    CCC
    
    12131415
    D D D
    """
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))