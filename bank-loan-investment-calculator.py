# 🏦 Bank Loan & Investment Calculator

print("=" * 45)
print("   🏦 BANK LOAN & INVESTMENT CALCULATOR")
print("=" * 45)

print("\nWhat do you want to calculate?")
print("1. Simple Interest (Loan)")
print("2. Investment Returns")

choice = input("\nEnter choice (1 or 2): ")

if choice == "1":
    print("\n--- 💰 LOAN CALCULATOR ---")
    principal = float(input("Enter loan amount (₹): "))
    rate = float(input("Enter interest rate (% per year): "))
    time = float(input("Enter time (in years): "))

    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    monthly_payment = total_amount / (time * 12)

    print("\n" + "=" * 45)
    print(f"  💵 Principal Amount  : ₹{principal:,.2f}")
    print(f"  📈 Interest Rate     : {rate}% per year")
    print(f"  📅 Time Period       : {time} years")
    print("-" * 45)
    print(f"  💸 Total Interest    : ₹{simple_interest:,.2f}")
    print(f"  💳 Total Amount      : ₹{total_amount:,.2f}")
    print(f"  📆 Monthly Payment   : ₹{monthly_payment:,.2f}")
    print("=" * 45)

elif choice == "2":
    print("\n--- 📈 INVESTMENT CALCULATOR ---")
    principal = float(input("Enter investment amount (₹): "))
    rate = float(input("Enter return rate (% per year): "))
    time = float(input("Enter time (in years): "))

    returns = (principal * rate * time) / 100
    total_amount = principal + returns

    print("\n" + "=" * 45)
    print(f"  💵 Investment Amount : ₹{principal:,.2f}")
    print(f"  📈 Return Rate       : {rate}% per year")
    print(f"  📅 Time Period       : {time} years")
    print("-" * 45)
    print(f"  💰 Total Returns     : ₹{returns:,.2f}")
    print(f"  🏆 Final Amount      : ₹{total_amount:,.2f}")
    print("=" * 45)

else:
    print("Invalid choice!")