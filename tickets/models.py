from django.db import models


class RepairTicket(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('WAITING_PARTS', 'Waiting for Parts'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    DEVICE_TYPE_CHOICES = [
        ('MOBILE', 'Mobile Phone'),
        ('LAPTOP', 'Laptop'),
        ('DESKTOP', 'Desktop PC'),
        ('TABLET', 'Tablet'),
        ('TV', 'Television'),
        ('OTHER', 'Other'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES, default='OTHER')
    device_model = models.CharField(max_length=100, help_text="e.g. iPhone 13, Dell Inspiron 15")
    issue_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    date_received = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.customer_name} ({self.device_model})"

    class Meta:
        ordering = ['-date_received']
