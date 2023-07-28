def numbers(num: int) -> bool:
    if num < 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
def main():
    user_input = int(input("enter natural value: "))
    if numbers(user_input):
        print(f"{user_input} -- is prime number")
    else:
        print(f"{user_input} -- isn't prime number")
        
if __name__ == '__main__':
    main()
