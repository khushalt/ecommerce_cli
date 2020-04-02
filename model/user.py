from ecomm.model.base_model import BaseModel


class User(BaseModel):

    def __init__(self, **kwargs):
        self.customer_id = kwargs.get('customer_id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.address = kwargs.get('address')
        self.table = "User"
        self.meta = ('customer_id', 'name', 'email', 'address')
        super().__init__()