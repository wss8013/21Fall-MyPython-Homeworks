'''
def main():
    x = 3
    y = 12.5
    # print(f'The rabbit is {x}.')
    # print(f'The rabbit is {x} years old.')
    # print(f'{y} is average.')
    # print(f'{y} * {x}')
    print(f'{y} * {x} is {x * y}')
    

main()
'''
''' 
def ct1(s):
    t = ''
    for c in s:
        if ((c.isdigit() == True) and (int(c)%2 == 1)):
            t += c
    return t

def main():
    print(ct1('I had 253 dogs and 762 cats!'))
    
    
main()

def ct2(s):
    for i in range(len(s)):
        c = s[i]
        d = s[len(s)-1-i]
        if (int(c) - int(d) != 1):
            return i
    return -1

def main():

    print(ct2('578364'))
main()
'''
'''
def ct3(n):
    s = '1'
    m=2
    while(int(s) < n):
        s += str(m)
        m *= 2
    return s
def main():
    print(ct3(42))

main()
'''
'''
def ones_digit(n):
    return n % 10

def test_one_digit():
    print('Testing ones_digit()...', end='')
    assert(ones_digit(5) == 5)
    assert(ones_digit(123) == 3)
    assert(ones_digit(100) == 0)
    assert(ones_digit(-123) == 7) # Added this test
    print('passed!')
test_one_digit()
'''
'''
def main():
    fruit = 'banana'
    index = 0
    while index < len(fruit):
        letter = fruit[len(fruit) - 1 - index]
        print(letter, end='')
        index += 1
        
main()
'''
'''
def is_palindrome(x):
	return x[::-1] == x
print(is_palindrome('noon'))
'''
'''
def any_lowercase1(s):
    for c in s:
        if c.isupper():
            return False
    return True

print(any_lowercase1('ABcdeF'))
'''
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print(any_lowercase3('ABcsde'))
