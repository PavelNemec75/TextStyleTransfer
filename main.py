from pathlib import Path

from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTTextLineHorizontal
import nltk
from nltk.tokenize import sent_tokenize
import spacy

nlp = spacy.load("xx_ent_wiki_sm")


class PdfTextExtractor:

    @classmethod
    def extract_text_from_pdf(cls, settings: dict) -> None:
        text = ""
        # page_number = 0

        with Path(settings["DATA_FOLDER"], settings["RAW_TEXT_FILE"]).open("w", encoding="utf-8") as f:
            for i, page_layout in enumerate(extract_pages(Path(settings["DATA_FOLDER"], settings["PDF_FILE"]))):
                if i not in settings["SKIP_PAGES"]:
                    # page_number += 1
                    # text += f"\n\n<page_{page_number}>"
                    for element in page_layout:
                        if isinstance(element, LTTextContainer):
                            text += element.get_text()
                    # text += f"</page_{page_number}>"
            f.write(text)


class TextCleaner:

    @classmethod
    def clean_text(cls, settings: dict) -> None:
        text = ""
        try:
            with Path(settings["DATA_FOLDER"], settings["RAW_TEXT_FILE"]).open("r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError as e:
            print(e)

        cleaned_text = (text
                        .replace("  ", " ")
                        .replace("„", "")
                        .replace("”", "")
                        .replace("‚", "")  # noqa: RUF001
                        .replace("‘", "")  # noqa: RUF001
                        .replace("…", "...")
                        .replace("“", "")
                        )

        cleaned_lines = ""
        maximum_characters_in_line = 0
        for line in cleaned_text.splitlines():
            if len(line) > maximum_characters_in_line:
                maximum_characters_in_line = len(line)
            if len(line.strip()) > 0 and not line.strip().isnumeric():
                cleaned_lines += line + "\n"

        sentences = sent_tokenize(cleaned_lines, language="czech")
        cleaned_sentences = ""
        for sentence in sentences:
            cleaned_sentence = sentence.replace("\n", "")
            if cleaned_sentence.startswith("– "):  # noqa: RUF001
                cleaned_sentence = (cleaned_sentence[2:])
            cleaned_sentences += cleaned_sentence + "\n"

        with Path(settings["DATA_FOLDER"], settings["CLEANED_TEXT_FILE"]).open("w", encoding="utf-8") as f:
            f.write(cleaned_sentences)


def main() -> None:
    settings = {
        "DATA_FOLDER": Path("data"),
        "PDF_FILE": Path("svejk_1_a_2.pdf"),
        "RAW_TEXT_FILE": Path("raw_text.txt"),
        "CLEANED_TEXT_FILE": Path("cleaned_text.txt"),
        "SKIP_PAGES": [0, 1, 2, 3, 4, 393],
    }

    # PdfTextExtractor.extract_text_from_pdf(settings)
    TextCleaner.clean_text(settings)


if __name__ == "__main__":
    main()
