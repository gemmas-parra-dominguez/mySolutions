class gsMom:
    
    personal_data_keys = ["name", "age", "childs", "fav color", "fav drink", "fav snack", "fav food", "hobbie"]
    personal_data_values = ["mom", 30, 1, "purple", "water", "fries", "enchiladas", "breath"]
    mood_keys = ["isAngry", "isSleepy", "isHappy", "isStressFree", "isOutOfBussiness", "isBusy"]
    activity_keys = ["isWorking", "isCooking",  "isSleeping", "isWorkingOut", "isGettingTipsy", "IsKeepingYouAlive", "isHiding"]

    activity_msg = {"isWorking": "Mom is working.",
                    "isCooking": "Mom is cooking.", 
                    "isSleeping": "Mom is sleeping.", 
                    "isWorkingOut": "Mom is at the gym.",
                    "isGettingTipsy": "Mom is having fun.",
                    "IsKeepingYouAlive": "Mom is keeping you alive.",
                    "isHiding": "Mom is taking five minutes."}
    
    # Initializers
    def __init__(self, default_data={}):
        self.init_personal_data(default_data)
        self.init_mood()
        self.init_activity()
       
        
    def init_mood(self):
        self.mood = dict.fromkeys(self.mood_keys, False)
        # Moms are always happy that you're alive.
        self.mood ["isHappy"] = True
        # Moms are always busy because you're alive.
        self.mood ["isBusy"] = True
        
    def init_activity(self):
        self.activity = dict.fromkeys(self.activity_keys, False)
        # Moms are always keeping you alive.
        self.activity ["IsKeepingYouAlive"] = True

    def init_personal_data(self, default_data={}):
        self.personal_data = dict(zip(self.personal_data_keys, self.personal_data_values))
        self.modifyData(default_data)

    def __repr__(self):
        return f"Mom is called: {self.personal_data["name"]}"
    
    def __call__(self):
        print("This is " + self.personal_data["name"])

    # Resets
    def resetMomMood(self):
        self.mood.clear()
        self.init_mood()

    def resetMomActivities(self):
        self.activity.clear()
        self.init_activity()

    def sendMom2Gym(self):
        self.resetMomMood()
        self.resetMomActivities()
        # Set Mom's mood
        self.mood["isStressFree"] = True
        self.mood["isHappy"] = True
        self.mood["isBusy"] = True
        self.mood["isOutOfBussiness"] = True
        # Change Mom's activities
        self.activity["isWorkingOut"] = True  

    def sendMom2Sleep(self):
        self.resetMomMood()
        self.resetMomActivities()
        # Set Mom's mood
        self.mood["isSleepy"] = True
        self.mood["isHappy"] = True
        self.mood["isBusy"] = True
        self.mood["isOutOfBussiness"] = True
        # Change Mom's activities
        self.activity["isSleeping"] = True

    def sendMom2TeCanasta(self):
        self.resetMomMood()
        self.resetMomActivities()
        print("Mom is out with friends!")
        # Set Mom's mood 
        self.mood["isBusy"] = True
        self.mood["isOutOfBussiness"] = True
        self.mood["isStressFree"] = True
        self.mood["isHappy"] = True
        # Change Mom's activities
        self.activity["isGettingTipsy"] = True
        self.activity["IsKeepingYouAlive"] = False
        self.activity["isHiding"] = True

    # Print fuctions
    def howIsMom(self):
        print("Mom is happy!") if(self.mood["isHappy"]) else print("Run! Mom isn't happy.")
        print("Mom is relaxed!") if(self.mood["isStressFree"]) else print("Watch out! Mom is stressed out.")
        print("Careful! Mom is angry!") if(self.mood["isAngry"]) else print("Mom isn't angry.")
        print("Shhhh! Mom is sleepy!") if(self.mood["isSleepy"]) else print("Mom isn't sleepy.")
        print("Mom is out of bussiness! Look for dadda.") if(self.mood["isOutOfBussiness"]) else print("Mom is here!")
        print("Careful! Mom is Busy.") if(self.mood["isBusy"]) else print("Mom is available.")

    def whatIsMomDoing(self):
        for act in self.activity:
            if self.activity[act]:
                print(self.activity_msg[act])

    def showPersonalData(self):
        for data in self.personal_data:
            if (type(self.personal_data[data]) != str):
                print(data + " is " + str(self.personal_data[data]))
            else:
                print(data + " is " + self.personal_data[data])
            
    # Setters
    def modifyData(self, data2Set):
         for data in data2Set:
             if data in self.personal_data:
                 self.personal_data[data] = data2Set[data]
    
    def updateData(self, data2Set):
        self.personal_data.update(data2Set)
    
    # Getters
    def retrieveData(self, data2Get):
        resultData = {}
        for data in data2Get:
            if data in self.personal_data:
                resultData[data] = self.personal_data[data]
        
        return resultData