from django.shortcuts import render, get_object_or_404, redirect
from .models import Room
from .forms import RoomForm

def room_dashboard(request):
    rooms = Room.objects.all().order_by('room_number')
    form = RoomForm()

    # CREATE
    if request.method == 'POST' and 'create_room' in request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_dashboard')

    # UPDATE
    if request.method == 'POST' and 'update_room' in request.POST:
        room_id = request.POST.get('room_id')
        room = get_object_or_404(Room, id=room_id)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_dashboard')

    return render(request, 'rooms/room_list.html', {
        'rooms': rooms,
        'form': RoomForm(),  # fresh form always
    })

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
    return redirect('room_dashboard')
