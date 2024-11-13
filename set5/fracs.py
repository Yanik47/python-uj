from math import gcd as greatest_common_divisor

def simplify_fraction(fraction):
    if fraction[0] == 0:
        return [0, 1]  
    divisor = greatest_common_divisor(fraction[0], fraction[1])
    numerator = fraction[0] // divisor
    denominator = fraction[1] // divisor
    if denominator < 0:  
        numerator *= -1
        denominator *= -1
    return [numerator, denominator]

def fraction_addition(fr1, fr2):
    numerator = fr1[0] * fr2[1] + fr2[0] * fr1[1]
    denominator = fr1[1] * fr2[1]
    return simplify_fraction([numerator, denominator])

def fraction_subtraction(fr1, fr2):
    numerator = fr1[0] * fr2[1] - fr2[0] * fr1[1]
    denominator = fr1[1] * fr2[1]
    return simplify_fraction([numerator, denominator])

def fraction_multiplication(fr1, fr2):
    numerator = fr1[0] * fr2[0]
    denominator = fr1[1] * fr2[1]
    return simplify_fraction([numerator, denominator])

def fraction_division(fr1, fr2):
    numerator = fr1[0] * fr2[1]
    denominator = fr1[1] * fr2[0]
    return simplify_fraction([numerator, denominator])

def is_fraction_positive(fraction):
    return fraction[0] >= 0 if fraction[0] == 0 else fraction[0] * fraction[1] > 0

def is_fraction_zero(fraction):
    return fraction[0] == 0

def compare_fractions(fr1, fr2):
    simplified_fr1 = simplify_fraction(fr1)
    simplified_fr2 = simplify_fraction(fr2)
    left = simplified_fr1[0] * simplified_fr2[1]
    right = simplified_fr1[1] * simplified_fr2[0]
    if left == right:
        return 0
    elif left > right:
        return 1
    else:
        return -1

def fraction_to_float(fraction):
    return float(fraction[0]) / float(fraction[1])
