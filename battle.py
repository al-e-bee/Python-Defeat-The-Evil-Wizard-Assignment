import random
# Starter Code
# =========================================
#          BASE CHARACTER CLASS
# =========================================
class Character:
    def __init__(self, name, health, attack_power, min_damage, max_damage):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.is_shielded = False # Track if an attack should be blocked
        
    def attack(self, opponent):
      
        # Check if the opponent has an active shield/evade
        if opponent.is_shielded:
            print(f"{opponent.name} successfully blocked/evaded the attack from {self.name}!")
            opponent.is_shielded = False # Consume the shield
            return
        
          # Calculate random damage from attack
        damage = random.randint(self.min_damage, self.max_damage)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

#----Added healing method----      
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} healed for {amount} HP! Current Health: {self.health}/{self.max_health}")

# =========================================
#           PLAYER HERO CLASSES
# =========================================
        
# Warrior Class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, min_damage=10, max_damage=30)
        
    # ---Added special abilities----    
    def use_special_ability(self, opponent):
        print("\nChoose a Special Ability:")
        print("1. Enrage (Sacrifce 15 HP for Double Damage)")
        print("2. Iron Wall (Gain a Shield against the next attack)")
        ability_choice = input("Enter choice: ")
        
        if ability_choice == '1':
            
            double_damage = self.attack_power * 2
            print(f"\n{self.name} uses goes into a frenzy!")
            
            if opponent.is_shielded:
                print(f"{opponent.name} deflects {self.name}'s Enrage strike! No damage dealt.")
                opponent.is_shielded = False
            
            else:
                self.health -= 15 # Sacrifice health
                opponent.health -= double_damage
                print(f"{self.name} loses 15 HP but smashed {opponent.name} for {double_damage} damage!")
                
                # Checks if opponent's health has reached 0 so they don't get a phantom turn
                if opponent.health <= 0:
                    print(f"{opponent.name} has been defeated!")
    
        elif ability_choice == '2':
            print(f"\n{self.name} raises a massive iron shield!")
            self.is_shielded = True   
        else:
            print("Invalid choice. Ability failed!")
        
# Mage Class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, min_damage=10, max_damage=25)
        
    # ----Added special abilities----       
    def use_special_ability(self, opponent):
        print("\nChoose a Special Ability:")
        print("1. Fireball (Cast a massive explosion)")
        print("2. Mana Shield (Block the next attack with magic)")
        ability_choice = input("Enter choice: ")
        
        if ability_choice == '1':
            fireball_damage = int(self.attack_power * 1.5)
            print(f"\n{self.name} casts Fireball!")
            
            if opponent.is_shielded:
                print(f"{opponent.name} extinguishes {self.name}'s fireball! No damage dealt.")
                opponent.is_shielded = False
            else:
                opponent.health -= fireball_damage
                print(f"The blast hits {opponent.name} for {fireball_damage} spell damage!")
                # Checks if opponent's health has reached 0 so they don't get a phantom turn
                if opponent.health <=0:
                    print(f"{opponent.name} has been defeated!")
            
        elif ability_choice == '2':
            print(f"\n{self.name} weaves a defensive barrier of pure mana!")
            self.is_shielded = True
        else:
            print("Invalid choice. Ability failed!")
        
# Created Archer Class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=20, min_damage=10, max_damage=20)

# ---Added special abilities----    
    def use_special_ability(self, opponent):
        print("\nChoose a Special Ability:")
        print("1. Quick Shot (Double Attack)")
        print("2. Evade (Evades the next attack)")
        ability_choice = input("Enter choice: ")
        
        if ability_choice == '1':
            print(f"\n{self.name} uses Quick Shot!")
            
            if opponent.is_shielded:
                print(f"{opponent.name} diverts {self.name}'s Quick Shot! No damage dealt.")
                opponent.is_shielded = False
                
            else:
                # Attacks twice
                self.attack(opponent)
                if opponent.health > 0:
                    self.attack(opponent)
                    print(f"{self.name} deals a double attack on {opponent.name}!")
                    
        elif ability_choice == '2':
            print(f"\n{self.name} uses Evade! Preparing to dodge the next strike.")
            self.is_shielded = True
        else:
            print("Invalid choice. Ability failed!")

# Created Paladin Class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, min_damage=10, max_damage=20)
        
# ---Added special abilities---
    def use_special_ability(self, opponent):
        print("\nChoose a Special Ability:")
        print("1. Holy Strike (Bonus damage)")
        print("2. Divine Shield (Blocks the next attack)")
        ability_choice = input("Enter choice: ")
        
        if ability_choice == '1':
            bonus_damage = self.attack_power + 20
            print(f"\n{self.name} channels divine light into Holy Strike!")
            
            if opponent.is_shielded:
                print(f"{opponent.name} blocked the Holy Strike!")
                opponent.is_shielded = False
            else:
                opponent.health -= bonus_damage
                print(f"{self.name} strikes {opponent.name} for a massive {bonus_damage} damage!")
                if opponent.health <= 0:
                    print(f"{opponent.name} has been defeated!")
        elif ability_choice == '2':
            print(f"\n{self.name} casts Divine Shield! An indestructible barrier surrounds them.")
            self.is_shielded = True
        else:
            print("Invalid choice. Ability failed!")

# =========================================
#           BOSS ENEMY CLASS
# =========================================
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, min_damage=15, max_damage=25)
        self.minions = 0
        self.is_storm_active = False
        
    def regenerate(self):
        print(f"{self.name} channels dark magic...")
        self.heal(5)
# Added advanced abilities to Evil Wizard        
    def take_turn(self, opponent):
        # 1. Wizard always regenerates health a the start of his turn
        self.regenerate()
        # 2. Handle ongoing effects first
        if self.is_storm_active:
            if opponent.is_shielded:
                print(f"{opponent.name}'s shield absorbs the lightning from the storm!")
                opponent.is_shielded = False # Consume the shield
            else:
                storm_damage = random.randint(5,15)
                opponent.health -= storm_damage
                print(f"The wizard summons a storm and zaps {opponent.name} for {storm_damage} damage!")
                if opponent.health <= 0:
                    return  #Stop turn if passive damage wins the game
    
    # 3. Randomly choose an action for this turn
    # Weigh choices by putting them in a list
        available_actions = ['attack']
    
        if self.minions < 2: # Only summon if the wizard has less than 2 minions
            available_actions.append('summon')
        if not self.is_storm_active: # Only start a storm if one isn't raging
            available_actions.append('storm')
        
        action = random.choice(available_actions)
    
    # 4. Execute the chosen action
        if action == 'attack':
        # Minions add bonus damage to his regular attack
            if self.minions > 0:
                bonus = self.minions * 5
                print(f"The wizard's {self.minions} minion(s) assist the attack against {opponent.name}!")
                self.min_damage += bonus
                self.max_damage += bonus
                self.attack(opponent)
                self.min_damage -= bonus # Reset stats back to normal
                self.max_damage -= bonus
            else:
                self.attack(opponent)
    
        elif action == 'summon':
            self.minions += 1
            print(f"{self.name} chants an incantation and summons a Shadown Minion! (Total: {self.minions})")
            print(f"Active minions grant the wizard +5 damage to standard attacks.")
    
        elif action == 'storm':
            print(f"{self.name} raises his staff! A lightning storm begins raging across the battlefield!")
            self.is_storm_active = True


# ======================================
#       GAME SYSTEM LOOP LOGIC
# ======================================       
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ").strip()
    # Safety loop: Keep asking user for input until they pick a valid number 1-4
    while class_choice not in ['1', '2', '3', '4']:
        print("Invalid selection! Please choose a cnumber between 1 and 4.")
        class_choice = input("Enter the number of your class choice: ").strip()
        
    # Now that we guarantee a valid class, ask for the character's name
    name = input("Enter your character's name: ").strip().title()
    while not name:
        print("A true hero needs a name! Please enter a valid name!")
        name = input("Enter your character's name: ").strip().title()
    
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        turn_taken = False # Wrapping EvilWizard's logic so it only fires if a valid action is taken
        
        if choice == '1':
            player.attack(wizard)
            turn_taken = True
        elif choice == '2':
            # ----- TEMPORARY TEST LINE -----
            # wizard.is_shielded = True # Forces the wizard's shield to be active for testing
            player.use_special_ability(wizard) # Implemented special abilities
            turn_taken = True
        elif choice == '3':
            player.heal(25) # Implemented heal method
            turn_taken = True
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")
       
       # The wizard only counters if the player actually completed an action turn
        if turn_taken and wizard.health > 0:
            wizard.take_turn(player) 
            
        if player.health <=0:
            print(f"Disaster strikes! {player.name} has been defeated by {wizard.name}!")
            print("\n=======================")
            print("\n====== GAME OVER ======")
            print("\n=======================")
            break
        
    if wizard.health <= 0:
        print(f"\nVictory! The wizard {wizard.name} has been defeated by {player.name}!")
        print("\n=======================")
        print("\n====== GAME OVER ======")
        print("\n=======================")
        

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)
    
if __name__ == "__main__":
    main()

