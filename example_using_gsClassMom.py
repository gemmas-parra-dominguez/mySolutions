import gsClassMom as objMom

print(objMom.GsMom())
objMom.GsMom().show_personal_data()

print("\n")
# Customize class
mom_data = {"Name": "Gemma", "Age": 39, "Childs": 2, "Fav color": "purple", "Fav drink": "clericot", "Fav snack": "jicama", "Hobbie": "tv shows"}
gemma_mom = objMom.GsMom(mom_data)
gemma_mom()
gemma_mom.show_personal_data()

# Morning
print("\n")
print("It's 7am... how is : " + gemma_mom.personal_data["Name"])
gemma_mom.how_is_mom()
gemma_mom.what_is_mom_doing()

# Workout
print("\n")
print("It's gym time!")
gemma_mom.send_mom_to_gym()
gemma_mom.what_is_mom_doing()
gemma_mom.how_is_mom()

# Daily routine
print("\n")
print("It's time to do the magic!")
gemma_mom.mom_doing_magic()
gemma_mom.what_is_mom_doing()
gemma_mom.how_is_mom()

# Time to work
print("\n")
print("It's time to work!")
gemma_mom.mom_earning_money()
gemma_mom.what_is_mom_doing()
gemma_mom.how_is_mom()

# End of the day
print("\n")
print("Time to chill out!")
gemma_mom.send_mom_to_tecanasta()
gemma_mom.what_is_mom_doing()
gemma_mom.how_is_mom()

# Morning
print("\n")
print("It's 11pm... how is : " + gemma_mom.personal_data["Name"])
gemma_mom.send_mom_to_sleep()
gemma_mom.how_is_mom()
gemma_mom.what_is_mom_doing()