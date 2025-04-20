from pet import Pet
# Create a new pet
if __name__ == "__main__":
    my_pet = Pet("Motina")
    
    # Test the pet's methods
    print("Testing My Motina Pet!")
    my_pet.get_status()  # Show initial status
    
    my_pet.eat()  # Feed the pet
    my_pet.get_status()  # Check status after eating
    
    my_pet.play()  # Play with the pet
    my_pet.get_status()  # Check status after playing
    
    my_pet.sleep()  # Let the pet sleep
    my_pet.get_status()  # Check status after sleeping
    
    # Test training and showing tricks
    my_pet.train("Sit")
    my_pet.train("Roll Over")
    my_pet.train("Sit")  # Try teaching the same trick again
    my_pet.show_tricks()  # Show all learned tricks