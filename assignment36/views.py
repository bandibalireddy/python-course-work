from django.shortcuts import render
import random

class Character:
    def __init__(self, name, health, attack_power, defense):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def attack(self, other):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def is_alive(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def heal(self, amount):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

    def get_status(self):
        # ── STUDENT CODE START ──
        pass
        # ── STUDENT CODE END ──

def index(request):
    hero_name = request.POST.get('hero_name', '')
    hero_health = int(request.POST.get('hero_health', 100))
    hero_attack = int(request.POST.get('hero_attack', 20))
    hero_defense = int(request.POST.get('hero_defense', 10))
    villain_name = request.POST.get('villain_name', '')
    villain_health = int(request.POST.get('villain_health', 100))
    villain_attack = int(request.POST.get('villain_attack', 20))
    villain_defense = int(request.POST.get('villain_defense', 10))
    action = request.POST.get('action', '')
    battle_state = request.POST.get('battle_state', '')
    
    hero = None
    villain = None
    battle_log = []
    battle_state_output = ''

    if request.method == 'POST':
        # ── STUDENT CODE START ──────────────────────────
        # TASK: Implement RPG battle using Character class
        # - Parse battle_state to restore characters
        # - Create characters, attack, heal based on action
        # - Serialize battle state back to string
        pass  # ← Remove this line when you write your code
        # ── STUDENT CODE END ────────────────────────────

    context = {
        'hero_name': hero_name,
        'hero_health': hero_health,
        'hero_attack': hero_attack,
        'hero_defense': hero_defense,
        'villain_name': villain_name,
        'villain_health': villain_health,
        'villain_attack': villain_attack,
        'villain_defense': villain_defense,
        'action': action,
        'hero': hero,
        'villain': villain,
        'battle_log': battle_log,
        'battle_state_output': battle_state_output,
    }
    return render(request, 'assignment36/index.html', context)
