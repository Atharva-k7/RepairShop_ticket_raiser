from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import RepairTicket
from .forms import RepairTicketForm


def ticket_list(request):
    tickets = RepairTicket.objects.all()
    status_filter = request.GET.get('status')
    if status_filter:
        tickets = tickets.filter(status=status_filter)
    context = {
        'tickets': tickets,
        'status_choices': RepairTicket.STATUS_CHOICES,
        'selected_status': status_filter,
    }
    return render(request, 'tickets/ticket_list.html', context)


def ticket_detail(request, pk):
    ticket = get_object_or_404(RepairTicket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


def ticket_create(request):
    if request.method == 'POST':
        form = RepairTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, f'Ticket #{ticket.id} created successfully.')
            return redirect('ticket_list')
    else:
        form = RepairTicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form, 'title': 'New Repair Ticket'})


def ticket_update(request, pk):
    ticket = get_object_or_404(RepairTicket, pk=pk)
    if request.method == 'POST':
        form = RepairTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ticket #{ticket.id} updated successfully.')
            return redirect('ticket_list')
    else:
        form = RepairTicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'title': f'Edit Ticket #{ticket.id}'})


def ticket_delete(request, pk):
    ticket = get_object_or_404(RepairTicket, pk=pk)
    if request.method == 'POST':
        ticket_id = ticket.id
        ticket.delete()
        messages.success(request, f'Ticket #{ticket_id} deleted.')
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})
