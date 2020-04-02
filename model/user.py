from ecomm.model.base_model import BaseModel


class User(BaseModel):

    def __init__(self, **kwargs):
        self.customer_id = kwargs.get('customer_id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.address = kwargs.get('address')
        self.table = "User"
        self.meta = ('customer_id', 'name', 'email', 'address')
        print(kwargs)
        super().__init__()


user1 = User(customer_id = 2222323, name = 'kdhushsdsal', email='khushalt5@gmail.com', address= 'Pune')
user1.on_delete()