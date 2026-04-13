class Mom:

    personal_data = {"age": "",
                     "name": "", 
                     "childs": "", 
                     "fav color": "", 
                     "fav drink": "", 
                     "fav snak": "", 
                     "fav food": "", 
                     "hobbie": ""}

    activity_msg = {"isWorking": "Mom is working.",
                    "isCooking": "Mom is cooking.", 
                    "isSleeping": "Mom is sleeping.", 
                    "isWorkingOut": "Mom is at the gym.",
                    "isGettingTipsy": "Mom is having fun.",
                    "IsKeepingYouAlive": "Mom is keeping you alive.",
                    "isHiding": "Mom is taking five minutes."}
    
    def __init__(self, name):
        self.personal_data["name"] = name
        self.init_mood()
        # Moms are always happy that you're alive.
        self.mood ["isHappy"] = True
        # Moms are always busy because you're alive.
        self.mood ["isBusy"] = True

        self.init_activity()
        # Moms are always keeping you alive.
        self.activity ["IsKeepingYouAlive"] = True
        
    def init_mood(self):
        self.mood = {"isAngry": False, 
                "isSleepy": False, 
                "isHappy": False,
                "isStressFree": False,
                "isOutOfBussiness": False,
                "isBusy": False }
        
    def init_activity(self):
        self.activity = {"isWorking": False,
                    "isCooking": False, 
                    "isSleeping": False, 
                    "isWorkingOut": False,
                    "isGettingTipsy": False,
                    "IsKeepingYouAlive": False,
                    "isHiding": False}     

    def __repr__(self):
        return f"Mom is called: {self.personal_data["name"]}"
    
    def resetMomMood(self):
        for mood in self.mood:
            self.mood[mood] = False

    def resetMomActivities(self):
        for act in self.activity:
            self.activity[act] = False

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