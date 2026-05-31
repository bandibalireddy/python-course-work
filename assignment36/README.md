# Assignment 36 — Simple RPG Character

## 🎯 What You Will Practice
Learn how to use classes, methods, object interaction, and randomness.

## 📍 Where to Write Your Code
Open `views.py` in this folder and find the Character class methods:
```python
# ── STUDENT CODE START ──

# ── STUDENT CODE END ──
```

## 📝 Your Tasks
1. __init__: set all attributes, max_health = health
2. attack(other): calculate damage = max(0, self.attack_power - other.defense + random(-2,2))
3. is_alive: return True if health > 0
4. heal: restore min(amount, max_health - health), return amount healed
5. get_status: return dict of all stats

## 💡 Hints
- __init__: `self.name = name`, `self.health = health`, `self.max_health = health`, `self.attack_power = attack_power`, `self.defense = defense`
- attack: `damage = max(0, self.attack_power - other.defense + random.randint(-2, 2))`, `other.health -= damage`, return damage
- is_alive: `return self.health > 0`
- heal: `heal_amount = min(amount, self.max_health - self.health)`, `self.health += heal_amount`, return heal_amount
- get_status: `return {'name': self.name, 'health': self.health, 'max_health': self.max_health, 'attack_power': self.attack_power, 'defense': self.defense, 'is_alive': self.is_alive()}`

## 🔍 Example
Hero attacks Villain: hero.attack_power = 20, villain.defense = 10
Expected Output: damage between 8-14, villain.health reduced by damage

Hero heals: hero.health = 50, hero.max_health = 100, amount = 30
Expected Output: hero.health = 80, returns 30

## ✅ You Are Done When
- Characters are created with all stats
- Attack calculates damage correctly with randomness
- is_alive returns correct status
- Heal restores health up to max_health
- get_status returns all character info
- Battle state persists across form submissions
