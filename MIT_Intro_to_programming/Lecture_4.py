def main(i):
    sumOfEvenNumbers = 0
    for i in i:
        sumOfEvenNumbers += countEvenNumbers(i)
    print(sumOfEvenNumbers)

def countEvenNumbers(i):
    if i %2 == 0:
        return 1
    else: return 0
    
main(range(5))
