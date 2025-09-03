def calculate_invoice():
    try:
        number_of_items = int(input("Enter a number items: "))
        if number_of_items <= 0:
            raise ValueError("Enter a non-negative number")

        total = 0
        for i in range(number_of_items):
            print(f"\n{i+1}th Item")
            price = float(input("Enter a price:"))
            quantity = int(input("Enter a quantity: "))

            if price <= 0 and quantity <= 0:
                print("price and quantity shouldn't be zero and non-negative.")

            total += price * quantity

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError:
        print("quantity shouldn't be zero")
    except Exception as e:
        print("Unexpected error occured.")

    else:
        print(f"total of the invoice amount: {total:.2f}")

    finally:
        print("Invoice calculation complete.")

calculate_invoice()