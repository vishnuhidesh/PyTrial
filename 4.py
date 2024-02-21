square = 16

low = 0
high = square
guess = (high+low)/2.0

error = 0.0001

while abs(guess**2-square)>=error:
    if guess**2<square:
        low=guess
    else:
        high=guess
    guess = (high+low)/2.0


print(guess)