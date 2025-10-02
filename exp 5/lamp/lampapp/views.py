from django.shortcuts import render

def calculate_power(request):
    power = None
    error = None
    if request.method == "POST":
        try:
            intensity = float(request.POST.get('intensity', ''))
            resistance = float(request.POST.get('resistance', ''))
            if intensity <= 0 or resistance <= 0:
                error = "Please enter positive numbers for intensity and resistance."
            else:
                power = intensity ** 2 * resistance  # P = I^2 * R
        except ValueError:
            error = "Invalid input. Please enter numeric values."

    return render(request, 'calculate_power.html', {'power': power, 'error':error})