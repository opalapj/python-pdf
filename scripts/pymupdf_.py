import pymupdf


def read_pdf(filepath):
    text = ""
    with pymupdf.open(filepath) as doc:
        number_of_pages = doc.page_count
        for page_num in range(number_of_pages):
            page = doc[page_num]
            text += page.get_text()
    return text


def main():
    filepath = "data/Kalendarz_RTPE_na_rok_2024.pdf"
    content = read_pdf(filepath)
    print(content)


if __name__ == "__main__":
    main()
