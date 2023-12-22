from funtions import salary, hello_who
def test_hello_who_max():
    assert hello_who('Max') == 'Hello,Max'
    assert hello_who('Neon') == 'Hello,Neon'
    assert hello_who('Cat') == 'Hello,Cat'
    assert hello_who('Tom') == 'Hello,Tom'
    assert hello_who('Mouse') == 'Hello,Mouse'

def test_salary():
    assert salary(2, 2) != 8
    assert salary(3, 1) != 6
