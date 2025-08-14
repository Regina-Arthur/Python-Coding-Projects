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
main(range(10))
main(range(2,9,3))
main(range(-4,6,2))
main(range(5,6))