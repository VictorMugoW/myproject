from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models

class Customer(models.Model):
    """
    Customer model to store customer information.
    Each customer can have multiple orders.
    """
    name = models.CharField(max_length=100)  # Customer's name
    email = models.EmailField(unique=True)    # Customer's email, must be unique

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Order model to store order details.
    Each order is associated with a single customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the order

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"