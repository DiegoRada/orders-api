from models.customer import Customer as CustomerModel
from schemas.customer import Customer


class CustomerService():

    def __init__(self, db) -> None:
        self.db = db

    def get_customers(self):
        result = self.db.query(CustomerModel).all()
        return result

    def get_customer(self, id):
        result = self.db.query(CustomerModel).filter(
            CustomerModel.customerid == id).first()
        return result
