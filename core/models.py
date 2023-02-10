from django.db import models
import uuid
# Create your models here.
from django.db import models
from decimal import Decimal
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle = models.CharField(max_length=30)


class Group(models.Model):
    name = models.CharField(max_length=100)
    discount_percent = models.PositiveSmallIntegerField()
class costumer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    credit = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    identity = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birthday = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

class OrderItem(models.Model):
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    def _calculate_total(self):
        return self.price * self.quantity

    total = property(_calculate_total)

class Order(models.Model):
    customer = models.ForeignKey(costumer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    # total = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    date_placed = models.DateTimeField(auto_now_add=True)

    def _calculate_total(self):
        sumof = sum(item.total for item in self.items.all())
        self.customer.credit = Decimal(self.customer.credit) + Decimal((sumof*self.customer.group.discount_percent/100))
        self.customer.save()
        
        

        return sumof

    
    total = property(_calculate_total)

    def save(self, *args, **kwargs):
        # print(self.items)
        # # self.total = 10 - self.customer.credit
        # if self.customer.group:
        #     self.total = self.total*Decimal((100 - self.customer.group.discount_percent) / 100)
        # self.customer.credit = ((self.total*self.customer.group.discount_percent/100) +(self.customer.credit))
        # sumof = sum(item.total for item in self.items.all())
        # self.customer.credit = Decimal(self.customer.credit) + Decimal((sumof*self.customer.group.discount_percent/100))
        # self.customer.save()
        super().save(*args, **kwargs)


class OrderItemRelation(models.Model):
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)