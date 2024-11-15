import openai
import os

# Ustawienie klucza API
openai.api_key = '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'

def read_article(file_path):
    # Odczytanie treści artykułu z pliku
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html_content(article_text):
    # Wysyłamy artykuł do OpenAI i otrzymujemy przetworzoną wersję HTML
    prompt = f"""
    Zaktualizuj poniższy artykuł, stosując odpowiednie tagi HTML:
    - Zastosuj odpowiednią strukturę HTML (nagłówki, akapity, listy).
    - Umieść w odpowiednich miejscach grafikę.
    - Nie dodawaj kodu CSS ani JavaScript. Skup się tylko na strukturze HTML w obrębie <body>..
    - Nie dołączaj nagłówków HTML, <html>, <head> ani <body>, tylko treść między tagami <body> i </body>.

    Artykuł: {article_text}
    """

    # Zapytanie do API OpenAI z użyciem modelu GPT-3.5 Turbo w trybie czatu
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=4096,  
        temperature=0.7,
    )

    # Otrzymujemy treść HTML
    content = response['choices'][0]['message']['content'].strip()

    # Usuwamy apostrofy i cudzysłowy na początku i końcu
    content = content.strip('\'"')

    # Opcjonalnie możesz dodać dodatkowe oczyszczanie, jeśli trzeba
    content = content.strip()

    return content

def save_html(content, output_path):
    # Zapisz wygenerowany kod HTML do pliku
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # Ścieżka do pliku z artykułem
    article_path = 'artykul.txt'
    
    # Odczytanie artykułu z pliku
    article_text = read_article(article_path)
    
    # Generowanie treści HTML
    html_content = generate_html_content(article_text)
    
    # Zapisanie wygenerowanego kodu HTML
    output_path = 'artykul.html'
    save_html(html_content, output_path)
    
    print("Artykuł został przetworzony i zapisany do pliku artykul.html.")

if __name__ == "__main__":
    main()
