# Assignment 37 — Vehicle Fleet Manager

## 🎯 What You Will Practice
Learn how to use inheritance, super(), method overriding, and polymorphism.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find the class methods:
```python
# ── STUDENT CODE START ──

# ── STUDENT CODE END ──
```

## 📝 Your Tasks
1. Vehicle.__init__: set make, model, year, fuel_type
2. Vehicle.get_info: return dict of basic info
3. Vehicle.calculate_fuel_cost: assume 10L per 100km, return cost
4. Car.__init__: use super() and add num_doors
5. Car.get_info: call super().get_info() and add num_doors
6. Truck.__init__: use super() and add payload_capacity
7. Truck.calculate_fuel_cost: call super() result and multiply by 1.3

## 💡 Hints
- Vehicle.__init__: `self.make = make`, `self.model = model`, `self.year = year`, `self.fuel_type = fuel_type`
- Vehicle.get_info: `return {'make': self.make, 'model': self.model, 'year': self.year, 'fuel_type': self.fuel_type}`
- Vehicle.calculate_fuel_cost: `liters = (distance_km / 100) * 10`, `return liters * fuel_price`
- Car.__init__: `super().__init__(make, model, year, fuel_type)`, `self.num_doors = num_doors`
- Car.get_info: `info = super().get_info()`, `info['num_doors'] = self.num_doors`, return info
- Truck.__init__: `super().__init__(make, model, year, fuel_type)`, `self.payload_capacity = payload_capacity`
- Truck.calculate_fuel_cost: `base_cost = super().calculate_fuel_cost(distance_km, fuel_price)`, `return base_cost * 1.3`

## 🔍 Example
Car: make = "Toyota", model = "Camry", year = 2022, fuel_type = "Gasoline", num_doors = 4
Expected Output: Car created with all attributes

Calculate fuel cost: distance_km = 100, fuel_price = 1.50
Expected Output (Car): $15.00
Expected Output (Truck): $19.50 (30% more)

## ✅ You Are Done When
- Vehicle base class works correctly
- Car inherits from Vehicle and adds num_doors
- Car.get_info includes num_doors
- Truck inherits from Vehicle and adds payload_capacity
- Truck.calculate_fuel_cost is 30% more than base
- Fleet state persists across form submissions
