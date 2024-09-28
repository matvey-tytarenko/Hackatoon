import requests
from bs4 import BeautifulSoup

# Funkcja do parsowania strony i zwracania tekstu według opisu
def scrape_and_process(url):
    # Pobranie zawartości strony
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Zmienne do przechowywania wyniku
    result = []

    # Pobieranie całego tekstu ze strony
    full_text = soup.get_text(separator=' ', strip=True)

    # Nagłówki od h1 do h6
    headers = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    # Przechowywanie poprzedniego nagłówka
    previous_header = None
    previous_level = None

    # Przechodzenie przez elementy w dokumencie HTML
    for element in soup.find_all(headers + ['p']):
        if element.name in headers:
            # Sprawdzamy poziom nagłówka (np. 'h1' = 1, 'h2' = 2, itd.)
            current_level = int(element.name[1])


            if previous_header:
                result.append(previous_header)  # Dodaj poprzedni nagłówek do wyniku
                previous_header = element.get_text()
                previous_level = current_level
        elif element.name == 'p':
            if previous_header:
                # Połącz nagłówek z paragrafem i dodaj do wyniku
                result.append(f"{previous_header}: {element.get_text()}")
                previous_header = None  # Zerowanie nagłówka po jego użyciu

    # Zwrócenie wynikowego tekstu
    return "\n".join(result)

# URL strony do przetworzenia
url = "https://www.podatki.gov.pl/pcc-sd/rozliczenie-podatku-pcc-od-kupna-samochodu/"

# Uruchomienie funkcji i wyświetlenie wyników
output = scrape_and_process(url)
print(output)
