# Solid design priciples
from abc import ABC, abstractmethod

class InvalidPaymentProcessor(Exception):
    pass


class ValidatePayment:
    def validate(self, payments: list[dict[str, str]]):
        pass


class AvailablePayments:
    def available_payments(self) -> list[str]:
        return ["credit", "debit"]
    

class ChoicePayment:
    def choice(self, available_payments: list[str]):
        pass

       

class AnyOrder(ABC):
    @abstractmethod
    def add_item(self, name: str, quantity: int, price: float) -> None:
        pass

    @abstractmethod
    def get_items(self) -> list[dict]:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def set_status(self, new_value: str) -> None:
        pass

    
class Calculator(ABC):
    @abstractmethod
    def total_price(order: AnyOrder) -> float:
        pass


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: AnyOrder, security_code: str) -> None:
        pass


class Order(AnyOrder): 
    def __init__(self):
        self._items = []
        self._status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
         self._items.append({"name": name, "quantity": quantity, "price": price})
    
    @property
    def get_items(self) -> list[dict]:
        return self._items
    
    @property
    def get_status(self) -> str:
        return self._status
    
    
    def set_status(self, new_value: str) -> None:
        self._status = new_value
        

class PriceCalculator(Calculator):
    @staticmethod
    def total_price(order: AnyOrder) -> float:
        items = order.get_items
        return sum((item.get("quantity") * item.get("price") for item in items))


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order: AnyOrder, security_code: str) -> None:
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order: AnyOrder, security_code: str) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status("paid")


class PaypalPaymentProcessor(PaymentProcessor):
    pass


# class PaymentProcessor:
#     def pay_debit(self, order: AnyOrder, security_code: str) -> None:
#          print("Processing debit payment type")
#          print(f"Verifying security code: {security_code}")
#          order.set_status("paid")

#     def pay_credit(self, order: AnyOrder, security_code: str) -> None:
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.set_status("paid")


class App:
    def __init__(self) -> None:
        self.order = Order()
        self.price_calculator = PriceCalculator()
        self.payment_processor = self.get_payment_processor()

    def get_payment_processor(self) -> PaymentProcessor:
        user_choice = input("Choice a option ('credit', 'debit'): ")
        available_payments = 



    def run(self) -> None:
        self.order.add_item("compuradora", 1, 500)
        self.order.add_item("ssd", 1, 150)

        total_price = self.price_calculator.total_price(self.order)
        print(total_price)

        self.payment_processor.pay(self.order, "123")

    @staticmethod
    def main():
        order = Order()
        order.add_item("compuradora", 1, 500)
        order.add_item("ssd", 1, 150)
        
        total_price = PriceCalculator.total_price(order)
        print(total_price)

        proccesor = CreditPaymentProcessor()
        proccesor2 = DebitPaymentProcessor()
        proccesor.pay(order, "123")


if __name__ == "__main__":
    App.main()

    app = App()
    app.run()