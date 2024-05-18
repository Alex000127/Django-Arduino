from django.shortcuts import render
from django.http import JsonResponse
from .arduino_controller import ArduinoController
import serial

# Create your views here.
SERIAL_PORT = 'COM3'  # Puerto conde esta conectado el Arduino
BAUD_RATE = 9600 # bps velocidad podriamos decir

arduino = ArduinoController(SERIAL_PORT, BAUD_RATE)

# Vista general 
def prueba(request): 
    if request.method == "POST":
        pass
    else: 
        return render(request, 'Led/led.html', {})

# funcion para el control del led 
def control_led(request):
    command = request.GET.get('command', '')

    if command:
        response = arduino.send_command(command)
        return JsonResponse({'response': response})

    return JsonResponse({'response': 'No command sent'})