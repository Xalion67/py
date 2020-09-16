def sqrt(x):
    def sqrt_iter(guess, previous_guess):
        if good_enough(guess, previous_guess):
            return guess
        return sqrt_iter(improve(guess), guess)

    def good_enough(guess, previous_guess):
        if abs((guess - previous_guess) / previous_guess) < 0.001:
            return True
        return False

    def improve(guess):
        return average(guess, x / guess)

    def average(x, y):
        return (x + y) / 2

    return sqrt_iter(1.0, 0.5)
