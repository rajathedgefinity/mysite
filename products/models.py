from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ("read_category", "Can read the category"),
            ("create_category", "Can create the category"),
            ("update_category", "can update the category"),
            ("remove_category", "can remove the category"),
        )


class product(models.Model):
    prodcat = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=True)
    price = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ("read_product", "Can read the product"),
            ("create_product", "Can create the product"),
            ("update_product", "can update the product"),
            ("remove_product", "can remove the product"),
        )
