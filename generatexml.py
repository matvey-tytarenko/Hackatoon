import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(elem):
    """Funkcja do ładnego formatowania XML"""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def generate_custom_xml(filename):
    # Tworzenie głównego elementu Deklaracja z odpowiednim xmlns
    root = ET.Element("Deklaracja", xmlns="http://crd.gov.pl/wzor/2023/12/13/13064/")

    # Tworzenie sekcji Naglowek
    naglowek = ET.SubElement(root, "Naglowek")

    kod_formularza = ET.SubElement(naglowek, "KodFormularza",
                                   kodSystemowy="PCC-3 (6)",
                                   kodPodatku="PCC",
                                   rodzajZobowiazania="Z",
                                   wersjaSchemy="1-0E")
    kod_formularza.text = "PCC-3"

    wariant_formularza = ET.SubElement(naglowek, "WariantFormularza")
    wariant_formularza.text = "6"

    cel_zlozenia = ET.SubElement(naglowek, "CelZlozenia", poz="P_6")
    cel_zlozenia.text = pole6

    data = ET.SubElement(naglowek, "Data", poz="P_4")
    data.text = pole4

    kod_urzedu = ET.SubElement(naglowek, "KodUrzedu")
    kod_urzedu.text = polekodurzedu

    # Tworzenie sekcji Podmiot1
    podmiot1 = ET.SubElement(root, "Podmiot1", rola="Podatnik")
    osoba_fizyczna = ET.SubElement(podmiot1, "OsobaFizyczna")

    pesel = ET.SubElement(osoba_fizyczna, "PESEL")
    pesel.text = polepesel

    imie = ET.SubElement(osoba_fizyczna, "ImiePierwsze")
    imie.text = poleimie

    nazwisko = ET.SubElement(osoba_fizyczna, "Nazwisko")
    nazwisko.text = polenazwisko

    data_urodzenia = ET.SubElement(osoba_fizyczna, "DataUrodzenia")
    data_urodzenia.text = poledataurodzenia

    # Adres Zamieszkania/Siedziby
    adres_zamieszkania = ET.SubElement(podmiot1, "AdresZamieszkaniaSiedziby", rodzajAdresu="RAD")
    adres_pol = ET.SubElement(adres_zamieszkania, "AdresPol")

    kod_kraju = ET.SubElement(adres_pol, "KodKraju")
    kod_kraju.text = polekodkraju

    wojewodztwo = ET.SubElement(adres_pol, "Wojewodztwo")
    wojewodztwo.text = polewojewodztwo

    powiat = ET.SubElement(adres_pol, "Powiat")
    powiat.text = polepowiat

    gmina = ET.SubElement(adres_pol, "Gmina")
    gmina.text = polegmina

    ulica = ET.SubElement(adres_pol, "Ulica")
    ulica.text = poleulica

    nr_domu = ET.SubElement(adres_pol, "NrDomu")
    nr_domu.text = polenrdomu

    nr_lokalu = ET.SubElement(adres_pol, "NrLokalu")
    nr_lokalu.text = polenrlokalu

    miejscowosc = ET.SubElement(adres_pol, "Miejscowosc")
    miejscowosc.text = polemiejscowosc

    kod_pocztowy = ET.SubElement(adres_pol, "KodPocztowy")
    kod_pocztowy.text = polekodpocztowy

    # Pozycje Szczegółowe
    pozycje_szczegolowe = ET.SubElement(root, "PozycjeSzczegolowe")

    p7 = ET.SubElement(pozycje_szczegolowe, "P_7")
    p7.text = pole7

    p20 = ET.SubElement(pozycje_szczegolowe, "P_20")
    p20.text = pole20

    p21 = ET.SubElement(pozycje_szczegolowe, "P_21")
    p21.text = pole21

    p22 = ET.SubElement(pozycje_szczegolowe, "P_22")
    p22.text = pole22

    p23 = ET.SubElement(pozycje_szczegolowe, "P_23")
    p23.text = pole23

    p24 = ET.SubElement(pozycje_szczegolowe, "P_24")
    p24.text = pole24

    p25 = ET.SubElement(pozycje_szczegolowe, "P_25")
    p25.text = pole25

    p46 = ET.SubElement(pozycje_szczegolowe, "P_46")
    p46.text = pole46

    p53 = ET.SubElement(pozycje_szczegolowe, "P_53")
    p53.text = pole53

    p62 = ET.SubElement(pozycje_szczegolowe, "P_62")
    p62.text = pole62

    # Pouczenia
    pouczenia = ET.SubElement(root, "Pouczenia")
    pouczenia.text = polepouczenie

    # Zapisywanie do pliku XML z ładnym formatowaniem
    xml_string = prettify(root)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(xml_string)

    print(f"Plik {filename} został wygenerowany.")


# Wywołanie funkcji
generate_custom_xml("deklaracja.xml")
