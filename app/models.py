from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField
# Create your models here.
STATE_CHOICES = (
    ("Dhaka", "Dhaka"),
    ("Chittagong", "Chittagong"),
    ("Rajshahi", "Rajshahi"),
    ("Khulna", "Khulna"),
    ("Barisal", "Barisal"),
    ("Sylhet", "Sylhet"),
    ("Rangpur", "Rangpur"),
    ("Mymensingh", "Mymensingh"),
    ("Netrokona", "Netrokona"),
    ("Kishoreganj", "Kishoreganj"),
    # Add more districts as needed
    ("Pirojpur", "Pirojpur"),
    ("Jhalokathi", "Jhalokathi"),
    ("Bhola", "Bhola"),
    ("Barguna", "Barguna"),
    ("Patuakhali", "Patuakhali"),
    ("Barishal", "Barishal"),
    ("Lakshmipur", "Lakshmipur"),
    ("Chandpur", "Chandpur"),
    ("Noakhali", "Noakhali"),
    ("Feni", "Feni"),
    ("Comilla", "Comilla"),
    ("Brahmanbaria", "Brahmanbaria"),
    ("Narsingdi", "Narsingdi"),
    ("Narayanganj", "Narayanganj"),
    ("Gazipur", "Gazipur"),
    ("Tangail", "Tangail"),
    ("Munshiganj", "Munshiganj"),
    ("Manikganj", "Manikganj"),
    ("Rajbari", "Rajbari"),
    ("Kishoreganj", "Kishoreganj"),
    ("Gopalganj", "Gopalganj"),
    ("Madaripur", "Madaripur"),
    ("Shariatpur", "Shariatpur"),
    ("Jamalpur", "Jamalpur"),
    ("Sherpur", "Sherpur"),
    ("Mymensingh", "Mymensingh"),
    ("Netrokona", "Netrokona"),
    ("Kurigram", "Kurigram"),
    ("Lalmonirhat", "Lalmonirhat"),
    ("Rangpur", "Rangpur"),
    ("Gaibandha", "Gaibandha"),
    ("Nilphamari", "Nilphamari"),
    ("Dinajpur", "Dinajpur"),
    ("Thakurgaon", "Thakurgaon"),
    ("Panchagarh", "Panchagarh"),
    ("Bogra", "Bogra"),
    ("Joypurhat", "Joypurhat"),
    ("Naogaon", "Naogaon"),
    ("Natore", "Natore"),
    ("Chapainawabganj", "Chapainawabganj"),
    ("Kushtia", "Kushtia"),
    ("Jhenaidah", "Jhenaidah"),
    ("Magura", "Magura"),
    ("Meherpur", "Meherpur"),
    ("Narail", "Narail"),
    ("Khulna", "Khulna"),
    ("Satkhira", "Satkhira"),
    ("Bagerhat", "Bagerhat"),
    ("Chuadanga", "Chuadanga"),
    ("Jashore", "Jashore"),
    ("Jhalokathi", "Jhalokathi"),
    ("Sarishabari", "Sarishabari"),
    ("Fulbari", "Fulbari"),
    ("Rajshahi", "Rajshahi"),
    ("Pabna", "Pabna"),
    ("Bogra", "Bogra"),
    ("Joypurhat", "Joypurhat"),
    ("Naogaon", "Naogaon"),
    ("Natore", "Natore"),
    ("Chapainawabganj", "Chapainawabganj"),
    # Add more districts as needed
)





CATEGORY_CHOICES=(
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)





class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50) 
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def ____str_(self):
        return self.name
    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models. PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
