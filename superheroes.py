import random
class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)
    def total_health(self):
        hctr = 0
        for k in self.heroes:
            hctr+=k.health
        return hctr
    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        for k in self.heroes:
            if(name == k.name):
                self.heroes.remove(k)
        return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        for k in self.heroes:
            if(name == k.name):
                return k
        return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for k in self.heroes:
            print(k.name)
    # Keep all your current code, but add these methods
    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """

        dmg = 0
        for k in self.heroes:
            dmg += k.attack()

        killsToAdd=other_team.defend(dmg)
        print(killsToAdd)
        for i in range(killsToAdd):
            self.update_kills()

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

        defc = 0
        for k in self.heroes:
            defc += k.defend()
        return self.deal_damage(damage_amt-defc)

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        whatToDeal = damage / len(self.heroes)
        deathCtr = 0
        for k in self.heroes:
            k.health -= whatToDeal
            if(k.health <= 0):
                k.deaths +=1
                deathCtr+=1
        return deathCtr

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for k in self.heroes:
            k.health = 100


    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        for k in self.heroes:
            print(k.name + " Kills: " + str(k.kills) + " Deaths: " + str(k.deaths))
    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for k in self.heroes:
            k.kills += 1


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, int(self.defense))

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.attack_strength = attack_strength

    def attack(self):
        # return attack value
        return random.randint(0, int(self.attack_strength))

    def update_attack(self, attack_strength):
        # update attack value
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        return random.randint(0, self.attack_strength)
class Hero:
    def __init__(self, name, health=100):
        # Initialize starting values
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Add ability to abilities list
        add_ability = self.abilities.append(ability)

    def attack(self):
        total = 0
        # Run attack() on every ability hero has
        for ability in self.abilities:
            total += ability.attack()
        return total

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        count = 0
        for k in self.armors:
            if(self.health == 0):
                return 0
            count += k.defend()
        return count

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        self.health -= damage_amt
        if(health==0):
            self.deaths+=1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills


class Arena:
    def __init__(self):
        self.team_one = Team(raw_input("Team 1 Name:"))
        self.team_two = Team(raw_input("Team 2 Name:"))

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

        while(True):
            if(raw_input("Would you like to add a Hero? Y/N:")=="n"):
                break
            hero = Hero(raw_input("Enter hero's name: "))
            while(True):
                if(raw_input("Would you like to add an ability to " + hero.name + "? Y/N:")=="n"):
                    break
                ability = Ability(raw_input("Ability name:"), raw_input("Ability Power:"))
                hero.add_ability(ability)
            while(True):
                if(raw_input("Would you like to add armor to " + hero.name + "? Y/N:")=="n"):
                    break
                armor= Armor(raw_input("Armor name:"), raw_input("Armor Defense:"))
                hero.armors.append(armor)
            self.team_one.add_hero(hero)



    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        while(True):
            if(raw_input("Would you like to add a Hero? Y/N:")=="n"):
                break
            hero = Hero(raw_input("Enter hero's name: "))
            while(True):
                if(raw_input("Would you like to add an ability to " + hero.name + "? Y/N:")=="n"):
                    break
                ability = Ability(raw_input("Ability name:"), int(raw_input("Ability Power:")))
                hero.add_ability(ability)
            while(True):
                if(raw_input("Would you like to add armor to " + hero.name + "? Y/N:")=="n"):
                    break
                armor= Armor(raw_input("Armor name:"), int(raw_input("Ability Defense:")))
                hero.armors.append(armor)
            self.team_two.add_hero(hero)

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        ctr = 0
        ran = random.randint(1,2)#TO decide who gets first attack!
        while(self.team_one.total_health()>0 or self.team_two.total_health>0):
            if(ran==1):
                if(self.team_one.total_health()<=0):
                    print("Team: "+self.team_one.name+" has lost!")
                    exit()
                self.team_one.attack(self.team_two)
                ran = 2
            self.show_stats()
            if(ran==2):
                if(self.team_two.total_health()<=0):
                    print("Team: "+self.team_two.name+" has lost!")
                    exit()
                self.team_two.attack(self.team_one)
                ran = 1
            self.show_stats()
            if(self.team_one.total_health()<=0 or self.team_two.total_health<=0):
                self.show_stats()
                exit()
    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print("Team One!")
        self.team_one.stats()
        print("Team Two!")
        self.team_two.stats()
if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

    hero2 = Hero("Hulk")
    ability = Ability("Hulk Smash", 300)
    hero2.add_ability(ability)
    new_ability = Ability("Super Strength", 800)
    hero2.add_ability(new_ability)
    print(hero2.attack())
    print(hero2.defend())

    team1 = Team("Super Team")
    team1.add_hero(hero)
    team1.add_hero(hero2)
    team1.remove_hero("Hulk")
    team1.view_all_heroes()
    team1.add_hero(hero2)
    team1.view_all_heroes()
    team1.revive_heroes()
    team1.stats()
    #team1.update_kills()
    team1.stats()

    hero3 = Hero("Flash")
    ability = Ability("Speedy Punch", 300)
    hero3.add_ability(ability)
    hero4 = Hero("Sonic")
    ability = Ability("Speedy Kick", 300)
    hero4.add_ability(ability)

    team2 = Team("Speed Team")
    team2.add_hero(hero3)
    team2.add_hero(hero4)
    team2.stats()
    team2.view_all_heroes()
    team2.deal_damage(12)

    team1.attack(team2)
    team1.stats()
    team2.stats()
    print(team2.find_hero("Flash").health)
    a = Arena()
    a.build_team_one()
    print(a.team_one.stats())
    a.build_team_two()
    print(a.team_one.stats())
    a.team_battle()
    exit()
