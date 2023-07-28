MASTER_WORK = 75
HUNDRED_PAPER_PRICE = 120
INC_PRICE = 20
def profit(p, n):
    if n % 100 != 0:
        return "error , not divided on 100"
    numbers_hundreds = n // 100
    return n * p - numbers_hundreds*(MASTER_WORK + HUNDRED_PAPER_PRICE+ INC_PRICE)
    
print(profit(2.5, 1000))

