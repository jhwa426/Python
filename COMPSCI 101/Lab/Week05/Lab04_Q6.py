"""
Lab 4:
"""

def main():
    result = test_number(33)
    print(result)
    print(test_number(28))
    print(test_number(30))

def test_number(value):
    if (value % 2 == 0) and ((value >= 30)and(value<=50)):
        return True
    else:
        return False

main()








