move = input("Does it move? (yes/no)")

if move == "yes":
    should = input("Should it? (yes/no)")
    if should == "yes": 
        print("No problem")
    elif should == "no":
        print("Then duct tape should do the trick")
    else:
        print("Answer my question! You should type yes or no.")
    
elif move == "no": 
    should = input("Should it? (yes/no)")
    if should == "no":
        print("No problem")
    elif should == "yes":
        print("Then WD-40 should do the trick")
    else:
        print("Answer my question! You should type yes or no.")
else:
    print("Answer my question! You didn't type yes or no.")

