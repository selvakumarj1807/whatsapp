class ATM():
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print("Your balance is", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")
        self.check_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.check_balance()
        else:
            print("Insufficient funds.")
a = 0
atm = ATM()
user={123:"sasi",111:"admin",222:"vig"}
# print("keys",user.keys())
# print("values",user.values())
u_name=input("Enter Username :")
pwd=int(input("Enter Password :") )   
if u_name in set(user.values()) and pwd in set(user.keys()):   
    while True:    
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
         atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
else:
        print("Enter correct Username and Password")
