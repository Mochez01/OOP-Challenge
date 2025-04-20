class Pet:
    # Constructor to initialize the pet's attributes
    def __init__(self, name):
        self.name = name
        self.hunger = 6   # Starts with medium hunger (0=full, 10=very hungry)
        self.energy = 6   # Starts with medium energy (0=tired, 10=fully rested)
        self.happiness = 6 # Starts with medium happiness (0–10)
        self.tricks = []   # Empty list to store learned tricks
    
    # Eat method: reduces hunger and increases happiness
    def eat(self):
        self.hunger -= 3
        if self.hunger < 0:  # Hunger can't go below 0
            self.hunger = 0
        self.happiness += 1
        if self.happiness > 10:  # Happiness can't go above 10
            self.happiness = 10
        print(f"{self.name} ate some food! Hunger is now {self.hunger}, Happiness is now {self.happiness}")
    
    # Sleep method: increases energy
    def sleep(self):
        self.energy += 5
        if self.energy > 10:  # Energy can't go above 10
            self.energy = 10
        print(f"{self.name} took a nap! Energy is now {self.energy}")
    
    # Play method: decreases energy, increases happiness and hunger
    def play(self):
        self.energy -= 2
        if self.energy < 0:  # Energy can't go below 0
            self.energy = 0
        self.happiness += 2
        if self.happiness > 10:  # Happiness can't go above 10
            self.happiness = 10
        self.hunger += 1
        if self.hunger > 10:  # Hunger can't go above 10
            self.hunger = 10
        print(f"{self.name} had fun playing! Energy is now {self.energy}, Happiness is now {self.happiness}, Hunger is now {self.hunger}")
    
    # Get status method: shows the current state of the pet
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
    
    # Train method: teaches the pet a new trick
    def train(self, trick):
        if trick not in self.tricks:  # Only add if trick is not already learned
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}!")

    # Show tricks method: displays all learned tricks
    def show_tricks(self):
        if self.tricks:  # Check if the list is not empty
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
