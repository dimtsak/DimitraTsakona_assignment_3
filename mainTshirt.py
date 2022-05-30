import characteristics as ch
import paymentStrategy as ps

class FinalPrice:
    """In this class the final cost is calculated, including additional costs or discounds"""
    
    def __init__(self,strategy = None):
        self.price = 20
        self.strategy = strategy

    def price_assesment(self):
        if self.strategy:
            paymentStrategy = self.strategy.paymentStrategy()
        else:
            paymentStrategy = 0
        return paymentStrategy

    def __str__(self):
        return f"Price: {self.price}, price after: {self.price_assesment()}"

# menu
if __name__ == "__main__":
    
    # initialize empty cart of zero cost
    cart = []
    cart_price = 0

    # creation of first T-shirt
    print("Hello! Please place your T-shirt order \1\nChoose color, size and fabric")
    order = ch.CreateTShirt().get_product()
    cart_price += order.price
    print(cart_price)
    cart.append(order)
    print(order)

    # add more t-shirts
    addItem = input("Do you want to add more T-shirts in your order? (y/n): ")
    while addItem == 'y':
        order = ch.CreateTShirt().get_product()
        cart_price += order.price
        cart.append(order)
        print(order)
        addItem = input("Do you want to add more T-shirts in your order? (y/n): ")

    # show order details
    print("\nYour cart: ")
    for item in cart:
        print(item)
    print("\nTotal cost of your cart: ")
    print(cart_price)
    print()
    
    # proceed to checkout
    order_payment = input("Do you want to proceed to checkout? (y/n): ")
    
    if order_payment=='y':
        payment_method = input("\tPlease choose a payment method:\n 1 --> Credit/Debit Card (10% discound)\n 2 --> Money/Bank Transfer (1 euro bank comission charge)\n 3 --> Cash (2 euros pay-on-delivery cost charge) ")
       
        # validation for existing payment options
        while payment_method not in ['1','2','3']:
            print("Not a valid payment method")
            payment_method = input("\tPlease choose a payment method:\n 1 --> Credit/Debit Card (10% discound)\n 2 --> Money/Bank Transfer (1 euro bank comission charge)\n 3 --> Cash (2 euros pay-on-delivery cost charge) ")

        if payment_method == '1':
            final_payment = FinalPrice(ps.CreditCard(cart_price)).price_assesment()
        elif payment_method == '2':
            final_payment = FinalPrice(ps.BankTransfer(cart_price)).price_assesment()
        elif payment_method == '3':
            final_payment = FinalPrice(ps.CashPaying(cart_price)).price_assesment()
        
        print(f"The final payment amount is: {final_payment} euros.\nThank you for your order!")
    else:
        print("Your order is canceled!")
    






