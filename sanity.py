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
    if syöte.find(',') != -1: # Katsotaan sisältääkö pilkkuja
        syote = syote.replace(',', '.') # Korvataan pilkut pisteillä
    if syote.find('.') != -1:  # Katsotaan löytyykö pistettä
        osat = syote.split('.') # luodaan lista jossa pisteellä erotetut osat syötteestä
        if len(osat) > 2:
            arvo = 0
            virhekoodi = 1
            virhesanoma = 'Syötteessä useita desimaalierottimia'
        else:
            osa = str(osat[0])
            if osa.isnumeric():
               osa = str(osat[1]) 
                if osa.isnumeric():
                    arvo = float(syote)
                    virhekoodi = 0
                    virhesanoma = 'Syöte OK'
          
    else:
        if syote.isnumeric():
            arvo = float(syote)
            virhekoodi = 0
            virhesanoma = 'Syöte OK'
          
      
    return tulokset



# Koodi, joka suoritetaan vain jos tämä tiedosto käynnistetään konsolista, esim "testit"