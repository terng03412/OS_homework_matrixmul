import random
import string

from random import seed
from random import randint


def getrandom():
    value = randint(0, 10)
    return value


def gen_file(n):

    filename = "data_" + str(n) + ".txt"

      # Write-Overwrites
    file1 = open(filename,"w")#write mode

    file1.write(str(n) + "\n")

    for count in range(0,n*n):
        d = getrandom()
        file1.write(str(d)+"\n")

    for count in range(0,n*n):
        d = getrandom()
        file1.write(str(d)+"\n")

    file1.close()


gen_file(100)