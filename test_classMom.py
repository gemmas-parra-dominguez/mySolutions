import classMom as objMom

mom_maria = objMom.gsMom({"name": "Maria", "age": 39})
mom_maria()
mom_maria.showPersonalData()
dict_data = {"age": 40, "name": "Cacho", "childs": 2, "fav color": "pink", "fav drink": "beer", "city": "salamanca"}
mom_maria.modifyData(dict_data)
mom_maria.showPersonalData()

mom_maria.updateData(dict_data)
mom_maria.showPersonalData()
