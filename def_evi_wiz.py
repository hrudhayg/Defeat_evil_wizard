import random

# ------------------------ Base Character Class ------------------------
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.block_next = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if opponent.block_next:
            print(f"{opponent.name} blocked the attack!")
            opponent.block_next = False
        else:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage! Curr Heal = {self.health}")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 20
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} healed for {heal_amount}. Current health: {self.health}")

    def display_stats(self, opponent): # type: ignore
        print(f"{self.name}'s Stats : Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print(f"{opponent.name}'s Stats : Health: {opponent.health}/{opponent.max_health}, Attack Power: {opponent.attack_power}")



# ------------------------ Warrior Class ------------------------
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_attack(self, opponent):
        damage = random.randint(35, 50)
        opponent.health -= damage
        print(f"{self.name} uses Power Attack for {damage} damage! CURR HEAL: {self.health}")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_block(self):
        self.block_next = True
        print(f"{self.name} raises shield and will block the next attack!")


# ------------------------ Mage Class ------------------------
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        damage = random.randint(40, 55)
        opponent.health -= damage
        print(f"{self.name} casts a powerful spell for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def mana_barrier(self):
        self.block_next = True
        print(f"{self.name} conjures Mana Barrier and blocks next attack!")


# ------------------------ Archer Class ------------------------
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)

    def quick_shot(self, opponent):
        total_damage = 0
        for i in range(2):
            damage = random.randint(10, 20)
            opponent.health -= damage
            total_damage += damage
        print(f"{self.name} fires two arrows for total {total_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.block_next = True
        print(f"{self.name} prepares to evade the next attack!")


# ------------------------ Paladin Class ------------------------
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)

    def holy_strike(self, opponent):
        damage = random.randint(30, 45)
        opponent.health -= damage
        print(f"{self.name} strikes with holy power for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.block_next = True
        print(f"{self.name} activates Divine Shield!")


# ------------------------ Evil Wizard Class ------------------------
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self, opponent):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")


# ------------------------ Character Creation ------------------------
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# ------------------------ Turn-Based Battle ------------------------
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Attack")
        print("3. Use Special Defence")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)

        elif choice == '3':
            if isinstance(player, Warrior):
                player.shield_block()
            elif isinstance(player, Mage):
                player.mana_barrier()
            elif isinstance(player, Archer):
                player.evade()
            elif isinstance(player, Paladin):
                player.divine_shield()

        elif choice == '4':
            player.heal()

        elif choice == '5':
            player.display_stats(wizard)

        else:
            print("Invalid choice. Try again.")

        if choice in ['1', '2', '3', '4'] and wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.attack(player)
            wizard.regenerate(player)


        if player.health <= 0:
            print(f"{player.name} has been defeated! Game Over.")
            return

    if wizard.health <= 0:
        print(f"\n🎉 Victory! {player.name} has defeated the evil wizard {wizard.name}!")


# ------------------------ Game Start ------------------------
def main():
    print("⚔️ Welcome to the Battle Against the Evil Wizard ⚔️")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
