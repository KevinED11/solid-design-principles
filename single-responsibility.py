# Solid design priciples
from abc import ABC, abstractmethod
from enum import StrEnum
class InvalidPaymentProcessor(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PaymentProcessorType(StrEnum):
    CREDIT = "credit"
    DEBIT = "debit"
    PAYPAL = "paypal"


class ValidatePayment:
    @staticmethod
    def validate(self, payments: list[PaymentProcessorType]):
        pass


class AvailablePaymentProccesor:
    def get(self) -> list[PaymentProcessorType]:
        return [payment_processor for payment_processor in PaymentProcessorType]
    

class ChoicePaymentProcessor:
    def choice(self, availables_payment_processor: list[PaymentProcessorType]) -> PaymentProcessorType:
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
    def pay(self, order: AnyOrder) -> None:
        pass


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizerSms(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code: str):
        print(f"verifying SMS code {code}")

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerGoogle(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code: str):
        print(f"verifying google auth code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


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

class PaymentProcessorFactory:
    @staticmethod
    def create(payment_processor_type: PaymentProcessorType) -> PaymentProcessor:
        if payment_processor_type == PaymentProcessorType.CREDIT:
            return CreditPaymentProcessor()
        elif payment_processor_type == PaymentProcessorType.DEBIT:
            return DebitPaymentProcessor()
        else:
            raise ValueError("Tipo de procesador de pagos no soportado")

class App:
    def __init__(self) -> None:
        self.order = Order()
        self.price_calculator = PriceCalculator()
        self.payment_processor = self.get_payment_processor()


    def get_payment_processor(self) -> PaymentProcessor:
        while True:
            user_choice = input("Ingrese el método de pago (credito/debito): ").lower()
            if user_choice == PaymentProcessorType.CREDIT.value:
                return PaymentProcessorFactory.create(PaymentProcessorType.CREDIT)
            elif user_choice == PaymentProcessorType.DEBIT.value:
                return PaymentProcessorFactory.create(PaymentProcessorType.DEBIT)
            else:
                print("Opción inválida. Por favor, elija 'credito' o 'debito'.")



    def run(self) -> None:
        self.order.add_item("compuradora", 1, 500)
        self.order.add_item("ssd", 1, 150)

        total_price = self.price_calculator.total_price(self.order)
        print(total_price)

        self.payment_processor.pay(self.order, "123")



if __name__ == "__main__":
    app = App()
    app.run()