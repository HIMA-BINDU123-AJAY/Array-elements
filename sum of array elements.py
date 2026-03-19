
#finding sum of array elements

arr = [1,2,3,4,5]
output = 15


def count_sum(arr):
    total = 0
    for num in arr:
        total +=num
    return total
arr = [1,2,3,4,5]
print("Sum:",count_sum(arr))

#counting the digits in array
def count_digits(arr):
    total_digits = 0
    
    for num in arr:
        
        total_digits += len(str(abs(num)))  
    
    return total_digits

arr = [12,345,6,7890] 
result = count_digits(arr)
print("Total number of digits:", result)

def count_even_digits(arr):
    count = 0
    
    for num in arr:
        num = abs(num)
        
        while num > 0:
            digit = num % 10
            
            if digit % 2 == 0:
                count += 1
                
            num //= 10
    
    return count
arr = [12, 345, 6, 7890]
print("Even digits:", count_even_digits(arr))

def find_max(arr):
    max_value = arr[0]   
    
    for num in arr:
        if num > max_value:
            max_value = num
    
    return max_value

arr = [12, 45, 7, 89, 23]
print("Maximum value:", find_max(arr))


expenses = []
def export_expenses(expenses):
    with open ("expenses.txt","w")as file:
        for expense in expenses:
            file.write(expense ["name"]+"-"+ expenses["amount"]+"/n")
def main():
    while True:
        print("1.add expense")
        print("2.view expense")
        print("3.export to file")
        print("4.exit")
        choice = input("Enter choice:")
        if choice == "1":
            name = input ("Enter expense name:")
            amount = input("Enter amount:")
            expenses.append({"name":name,"amount":amount})

        elif choice == "2":
             for expenses in expenses:

                 Print (expense ["name"],"-", expense["amount"])

        elif choice == "3":

             export_expenses (expenses)

        elif choice == "4":

             Print ("Exiting the program")

             break

        else:
           Print ("Invalid choice. Try Again")
main()

