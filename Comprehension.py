numbers = [1,2,3,4,5,6,7,8,9,10]

squares = [n ** 2 for n in numbers]
odds = [n for n in numbers if n % 2 !=0]
divisible_by_3 = [n for n in numbers if n % 3 == 0]
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
even_or_odd = ['even' if n % 2==0 else 'odd' for n in numbers]


print(f'Squares: {squares}')
print(f'Odds: {odds}')
print(f'Divisible by 3: {divisible_by_3}')
print(f'Even or odd: {even_or_odd}')