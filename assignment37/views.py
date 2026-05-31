from django.shortcuts import render

class Vehicle:
    def __init__(self, make, model, year, fuel_type):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_info(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def calculate_fuel_cost(self, distance_km, fuel_price):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, num_doors):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_info(self):  # override
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_type, payload_capacity):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def calculate_fuel_cost(self, distance_km, fuel_price):  # override, trucks use 30% more fuel
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

def index(request):
    vehicle_type = request.POST.get('vehicle_type', '')
    make = request.POST.get('make', '')
    model = request.POST.get('model', '')
    year = request.POST.get('year', '')
    fuel_type = request.POST.get('fuel_type', '')
    num_doors = request.POST.get('num_doors', '')
    payload_capacity = request.POST.get('payload_capacity', '')
    distance_km = request.POST.get('distance_km', '')
    fuel_price = request.POST.get('fuel_price', '')
    fleet_data = request.POST.get('fleet_data', '')
    
    vehicle = None
    fuel_cost = None
    fleet = []
    fleet_data_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement vehicle fleet manager using inheritance
        # - Parse fleet_data to restore fleet
        # - Create Car or Truck based on vehicle_type
        # - Calculate fuel cost if distance and price provided
        # - Serialize fleet back to string
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'vehicle_type': vehicle_type,
        'make': make,
        'model': model,
        'year': year,
        'fuel_type': fuel_type,
        'num_doors': num_doors,
        'payload_capacity': payload_capacity,
        'distance_km': distance_km,
        'fuel_price': fuel_price,
        'vehicle': vehicle,
        'fuel_cost': fuel_cost,
        'fleet': fleet,
        'fleet_data_output': fleet_data_output,
    }
    return render(request, 'assignment37/index.html', context)
