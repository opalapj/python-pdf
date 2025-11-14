import pypdf


def read_pdf(filepath):
    reader = pypdf.PdfReader(filepath)
    number_of_pages = len(reader.pages)
    text = ""
    for page_num in range(number_of_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


def main():
    filepath = "data/Kalendarz_RTPE_na_rok_2024.pdf"
    content = read_pdf(filepath)
    print(content)


if __name__ == "__main__":
    main()
