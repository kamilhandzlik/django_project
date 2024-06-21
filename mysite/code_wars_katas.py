#####################################################################################
###############   ZADANIE 138     ###################################################
#####################################################################################
"""The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";"""


# Rozwiązanie 1
def chromosome_check(chromosome):
    gender = ""
    if chromosome == "XX":
        gender = "daughter"
    elif chromosome == "XY":
        gender = "son"

    return f"Congratulations! You're going to have a {gender}."


# Rozwiązanie 2
def chromosome_check(chromosome):
    gender = {"XY": "son", "XX": "daughter"}
    return "Congratulations! You're going to have a {}.".format(gender[chromosome])


# Rozwiązanie 3
def chromosome_check(sperm):
    return "Congratulations! You're going to have a {}.".format(
        "son" if "Y" in sperm else "daughter"
    )


#####################################################################################
###############   ZADANIE 139     ###################################################
#####################################################################################
"""Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
Zero alone is fine, don't worry about it. Poor guy anyway"""


# Rozwiązanie 1
def no_boring_zeros(n):
    if n == 0:
        return n
    while n % 10 == 0:
        n //= 10

    return n


# Rozwiązanie 2
def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n


#####################################################################################
###############   ZADANIE 140     ###################################################
#####################################################################################
"""Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'"""


def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


#####################################################################################
###############   ZADANIE 141     ###################################################
#####################################################################################
"""In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code."""
# Rozwiązanie 1
from functools import reduce
import operator


def find_difference(a, b):
    list_a = reduce(operator.mul, a, 1)
    list_b = reduce(operator.mul, b, 1)
    result = list_a - list_b

    return result * (-1) if result < 0 else result


# Rozwiązanie 2
from numpy import prod


def find_difference(a, b):
    return abs(prod(a) - prod(b))


# Rozwiązanie 3
def find_difference(a, b):
    return abs((a[1] * a[2] * a[0]) - b[1] * b[2] * b[0])


#####################################################################################
###############   ZADANIE 142     ###################################################
#####################################################################################
"""Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"""


# Roziwiązanie 1
def to_jaden_case(string):
    new_string = string.split(" ")
    result = ""
    for word in new_string:
        result += word.capitalize() + " "

    return result[:-1]


# Rozwiązanie 2
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())


#####################################################################################
###############   ZADANIE 143     ###################################################
#####################################################################################
"""Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:

"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'."""


def dna_to_rna(dna):
    rna = ""
    for nuclei in dna.split():
        if nuclei == "T":
            nuclei = "U"
            rna += nuclei
        else:
            rna += nuclei
    return rna


#####################################################################################
###############   ZADANIE 144     ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 145     ###################################################
#####################################################################################


#####################################################################################
###############   ZADANIE 146     ###################################################
#####################################################################################
