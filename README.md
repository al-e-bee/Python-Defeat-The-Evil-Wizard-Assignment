# Python Text-Based RPG: Heroes vs. The Dark Wizard

Welcome to a terminal-based, Object-Oriented Programming (OOP) role-playing game built in Python. Players choose a hero class, manage tactical choices like special skills, shielding, and healing, and attempt to take down an escalating, dynamic boss: **The Dark Wizard**.

---

## Features

- **Four Unique Playable Classes:** Warrior, Mage, Archer, and Paladin—each equipped with tailored base stats and two custom strategic abilities.
- **Object-Oriented Architecture:** Leverages class inheritance and polymorphism to cleanly drive combat interactions from a shared baseline.
- **Advanced Dynamic Boss AI:** The Dark Wizard adapts dynamically by parsing a real-time list of legal moves, summoning persistent combat minions, and casting an active weather status effect.
- **Turn-Based Battle State Machine:** Includes strict defensive inputs handling input verification, capitalization formatting, state flags to combat "phantom turns," and shield-breaking logic.

---

## Project Structure & Architecture

The codebase relies heavily on clean OOP architecture to govern state changes across entities:

1. **`Character` (Base Class):** Contains baseline parameters (`health`, `min_damage`, `max_damage`) and universally inherited logic such as `attack()`, `heal()`, and `display_stats()`.
2. **Inherited Heroes:** Derived classes (`Warrior`, `Mage`, `Archer`, `Paladin`) that overwrite base attributes via initialization overrides and implement unique `use_special_ability()` selection inputs.
3. **`EvilWizard` (Boss AI Class):** Inherits from `Character` but updates the gameplay loop entirely through its automated `take_turn()` layout.

---

## Hero Archetypes & Abilities

## ⚔️ Hero Archetypes & Abilities

| Class       | Health | Base Damage | Special Ability 1                                                                       | Special Ability 2                                                            |
| :---------- | :----: | :---------: | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Warrior** |  140   |    10–30    | **Enrage:** Sacrifices 15 HP to deal a flat double-damage blow (50 Damage).             | **Iron Wall:** Raises a physical barrier that fully deflects the next hit.   |
| **Mage**    |  100   |    10–25    | **Fireball:** Channels an explosive spell scaling off attack power (52 Magic Damage).   | **Mana Shield:** Crafts a magical barrier that fully deflects the next hit.  |
| **Archer**  |  200   |    10–20    | **Quick Shot:** Fires two distinct, consecutive basic arrow attacks in a single turn.   | **Evade:** Prepares to entirely dodge incoming damage next turn.             |
| **Paladin** |  140   |    10–20    | **Holy Strike:** Imbues a massive single attack with raw divine light (45 Holy Damage). | **Divine Shield:** Surrounds the hero in an indestructible defensive shield. |

---

## The Boss Phase: Advanced Wizard Mechanics

The Dark Wizard is built to prevent passive play styles. His mechanics execute across systematic check-phases:

1. **Passive Regeneration:** The wizard channels dark magic at the opening of every single action turn, instantly healing for $+5$ HP up to his maximum capacity.
2. **The Lightning Storm:** Once activated, the environment shifts. At the opening of every round, the storm automatically zaps the player for $5$ to $15$ passive damage. If the player is shielded, the storm consumes the shield but keeps the player safe from the storm's tick damage.
3. **Shadow Minions:** The wizard can summon up to two persistent minions. Each minion currently alive grants him a permanent $+5$ damage bonus to his minimum and maximum standard attack output.

---

## How to Play & Run

### Prerequisites

- Python 3.x installed on your local machine.

### Execution

1. Download or clone the script file (e.g., `rpg_game.py`).
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the application using Python:

```bash
python battle.py

```

### Step-by-Step Gameplay

1. **Character Select:** Enter a number between `1` and `4` to pick your hero class. Input verification ensures an incorrect choice re-prompts you until a valid selection is made.
2. **Naming:** Enter your character's name. Blank spaces are rejected, and names are auto-formatted with proper title casing (e.g., `king arthur` becomes `King Arthur`).
3. **The Combat Loop:** On your turn, choose to execute a standard **Attack**, trigger a class-specific **Special Ability**, **Heal** for $25$ HP, or **View Stats** safely without losing your turn.
4. **Endgame:** Combat persists dynamically until either the hero or the wizard's health drops to $\le 0$, triggering customized victory or defeat wrap-around screens.
