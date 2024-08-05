class Character:
    def __init__(self,health,damage,speed):
        self.health=health
        self.damage=damage
        self.speed=speed
    def double_speed(self):
        self.speed*=2

warrior=Character(120,50,10)
ninja=Character(80,40,180)

print(f'warrior speed:{warrior.speed}')
print(f'ninja speed:{ninja.speed}')
warrior.double_speed()
print(f'warrior speed:{warrior.speed}')
print(f'ninja speed:{ninja.speed}')