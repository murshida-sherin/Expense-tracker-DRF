from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES=(
        ("food","food"),
        ("bill","bill"),
        ("fuel","fuel")
    )
    PAYMENT_CHOICES=(
        ("UPI","UPI"),
        ("card","card")
    )
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(default="food",choices=CATEGORY_CHOICES)
    payment=models.CharField(default="UPI",choices=PAYMENT_CHOICES)
    
    
    def __str__(self):
        return f"{self.title}-{self.amount}"