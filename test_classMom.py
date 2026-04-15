import classMom as objMom

mom_maria = objMom.GsMom({"name": "Maria", "age": 39})
mom_maria()
mom_maria.show_personal_data()
dict_data = {"age": 40, "name": "Cacho", "childs": 2, "fav color": "pink", "fav drink": "beer", "city": "salamanca"}
mom_maria.modify_data(dict_data)
mom_maria.show_personal_data()

mom_maria.update_data(dict_data)
mom_maria.show_personal_data()
