# palindrome2 without using methods.

print(f'{'Palindrome checker.':>{29}}')
print('-'*40)

while True:
    a = int(input('Enter the number: '))

    d = a

    c = 0

    while a>0:
        b = a%10
        c = ( c*10) + b
        a //= 10

    if d == c:
        print(f'The number {d} is a palindrome number.')

    else:
        print(f'The number {d} is not a palindrome number.')

    x = input('Do you want to check another number (Enter yes or no): ')

    if 'yes' in x :
        continue
    else:
        print('Thank you for using this program.')
        break