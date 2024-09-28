import requests
from bs4 import BeautifulSoup


# Funkcja, która sprawdza, czy po danym headerze są headery niższego stopnia
def has_lower_headers(soup, current_header):
    current_level = int(current_header.name[1])
    next_elements = current_header.find_all_next(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    for element in next_elements:
        level = int(element.name[1])
        if level > current_level:
            return True
        elif level == current_level:
            break
    return False


# Funkcja do scrapowania i przetwarzania tekstu
def scrape_and_process(url):
    # Pobieramy stronę
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Szukamy wszystkich nagłówków i paragrafów
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    result = []

    for header in headers:
        if not has_lower_headers(soup, header):
            header_text = header.get_text(strip=True)
            content = []
            next_sibling = header.find_next_sibling()
            while next_sibling and next_sibling.name != header.name:
                if next_sibling.name == 'p':
                    content.append(next_sibling.get_text(strip=True))
                next_sibling = next_sibling.find_next_sibling()

            # Łączenie headera z paragrafami
            if content:
                combined_content = f"{header_text}: {' '.join(content)}"
                result.append(combined_content)

    return result


# Przykład użycia
url = 'https://example.com'
processed_content = scrape_and_process(url)

# Wyświetlenie wyniku
for section in processed_content:
    print(section)
