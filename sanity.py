"""
Moduli, jonka funktioilla tarkistetaan syötteen järkevyys
Sisältää joukon funktioita, joita käyttämällä saadaan:
1. Virhekoodi (int), 2. Virhesanoma (string) ja 3. arvo (float)
Funktiot palauttavat nämä tiedot listana
"""

# Kirjastojen lataukset


# Luokkien ja funktioiden määritykset
def liukuluku_syote(syote):
    """Tutkii onko syöte sopiva liukuluvuksi

    Args:
        syote (string): näppäimistöltä syötetty arvo

    Returns:
        list: virhekoodi (int), sanoma (string), arvo (float)
    """
    syote = syote.strip() # Poistetaan tulostumattomat merkit molemmista päistä
    if syote.find(',') != -1: # Katsotaan sisältääkö pilkkuja
        syote = syote.replace(',', '.') # Korvataan pilkut pisteillä

    if syote.find('.') != -1:  # Katsotaan löytyykö pistettä
        osat = syote.split('.') # luodaan lista jossa pisteellä erotetut osat syötteestä
        if len(osat) > 2: # Jos osia on enemmän kuin 2, pisteitä on liikaa
            arvo = 0 # Virheellisen tiedon tapauksessa annetaan arvoksi 0
            virhekoodi = 1 # Tämä on virhe nro 1
            virhesanoma = 'Syötteessä useita desimaalierottimia'
        else: # Osia korkeintaan 2
            osa = str(osat[0]) # Otetaan  listan ensimmäinen alkio ja muutetaan merkkijonoksi
            if osa.isnumeric(): # Jos se on numeerinen
                osa = str(osat[1]) # Otetaan toinen alkio ja muutetaan se merkkijonoksi
            
                if osa.isnumeric(): # Jos toinenkin osa on numeeerinen
                    arvo = float(syote) # Muutetaan syöte liukuluvuksi
                    virhekoodi = 0 # Paluukoodi 0 -> ei virhettä
                    virhesanoma = 'Syöte OK'
                else: # TODO: Tähän virhekoodin 2 asettaminen
                    pass

            else:  # TODO: Tähän virhekoodin 2 asettaminen
                pass

    else: # Jos pistettä ei löytynyt
        if syote.isnumeric(): # Onko syöte numeerinen
            arvo = float(syote) # Muutetaan liukuluvuksi
            virhekoodi = 0 # 0 -> ei virhettä
            virhesanoma = 'Syöte OK'
          
    # TODO: Koosta arvo ja virhetiedot listaksi tulokset  
    return tulokset



# Koodi, joka suoritetaan vain jos tämä tiedosto käynnistetään konsolista, esim "testit"