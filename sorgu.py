
def sorgu(İSİM,SOYİSİM):
    with (open("yaşayanlar.txt","r",encoding="utf-8")) as file_value:
        file = file_value.read()
        sorgu_value= "{} {}".format(İSİM, SOYİSİM)
        isim_soyisim1 = "{} {}".format(İSİM, SOYİSİM.upper())
        isim_soyisim2 = "{} {}".format(İSİM, SOYİSİM.capitalize())
        isim_soyisim3 = "{} {}".format(İSİM, SOYİSİM.lower())
        isim_soyisim4 = "{} {}".format(İSİM.upper(), SOYİSİM)
        isim_soyisim5 = "{} {}".format(İSİM.capitalize(), SOYİSİM)
        isim_soyisim6 = "{} {}".format(İSİM.lower, SOYİSİM)
        if isim_soyisim1 in file :
            return "Kayıtlarımızda bulunmuştur"
        if isim_soyisim2 in file :

            return "Kayıtlarımızda bulunmuştur"
        if isim_soyisim3 in file :

            return "Kayıtlarımızda bulunmuştur"
        if isim_soyisim4 in file :

            return "Kayıtlarımızda bulunmuştur"
        if isim_soyisim5 in file :

            return "Kayıtlarımızda bulunmuştur"
        if isim_soyisim6 in file :

            return "Kayıtlarımızda bulunmuştur"
        if sorgu_value in file :

            return "Kayıtlarımızda bulunmuştur"
        else:
            return "kayıtlarımızda bulunmamaktadır"
