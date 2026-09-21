from django import forms
from .models import RepairTicket


class RepairTicketForm(forms.ModelForm):
    class Meta:
        model = RepairTicket
        fields = [
            'customer_name', 'customer_phone', 'device_type', 'device_model',
            'issue_description', 'status', 'estimated_cost',
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'device_type': forms.Select(attrs={'class': 'form-control'}),
            'device_model': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'estimated_cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }
