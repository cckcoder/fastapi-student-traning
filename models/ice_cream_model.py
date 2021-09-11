from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class IceCream(Model):
    id = fields.IntField(pk=True)
    flavor = fields.CharField(100)
    price = fields.DecimalField(max_digits=10, decimal_places=3)
    is_active = fields.BooleanField(default=True)

    def __str__(self) -> str:
        return self.flavor


IceCreamPydantic = pydantic_model_creator(IceCream, name="IceCream")
IceCreamPydanticIn = pydantic_model_creator(
    IceCream, name="IceCreamIn", exclude_readonly=True
)
