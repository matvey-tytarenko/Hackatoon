import requests
from bs4 import BeautifulSoup
from googlesearch import search


def get_text_from_url(url):
    """Pobiera treść strony z URL i zwraca jako tekst"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy nie wystąpił błąd HTTP
        soup = BeautifulSoup(response.content, "html.parser")

        # Pobieranie tekstu ze strony, wyłączając skrypty i style
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()  # Usuwa skrypty i style

        text = soup.get_text()  # Pobieranie całego tekstu

        # Czyszczenie tekstu, usuwanie białych znaków
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)

        return text
    except Exception as e:
        print(f"Nie udało się pobrać zawartości z {url}: {e}")
        return ""


def get_first_500_words(text):
    """Zwraca pierwsze minimum 500 wyrazów, kontynuując do końca zdania"""
    words = text.split()

    if len(words) < 500:
        return text  # Zwracamy cały tekst, jeśli ma mniej niż 500 wyrazów

    # Dołączamy kolejne wyrazy, aż do końca zdania (kropka, wykrzyknik, przecinek)
    result = ' '.join(words[:500])
    extra_words = words[500:]

    for word in extra_words:
        result += ' ' + word
        if word.endswith(('.', '!', '?')):
            break

    return result


def google_search_with_content(query):
    results = []

    try:
        # Wyszukiwanie zapytania i pobranie 3 pierwszych wyników
        for result in search(query, num_results=3):
            # Pobieranie treści z każdej strony
            page_text = get_text_from_url(result)

            if page_text:
                # Pobranie minimum 500 wyrazów
                first_500_words = get_first_500_words(page_text)
                results.append({
                    "url": result,
                    "content": first_500_words
                })
    except Exception as e:
        print(f"Wystąpił błąd podczas wyszukiwania: {e}")

    return results


# Przykład użycia:
query = "Jak zapłacić podatek przy kupnie samochodu?"
search_results = google_search_with_content(query)

# Wyświetlenie wyników
for index, result in enumerate(search_results):
    print(f"Wynik {index + 1}: {result['url']}")
    print(f"Treść:\n{result['content']}\n")
