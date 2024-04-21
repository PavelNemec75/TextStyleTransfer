from pathlib import Path

from modules.PdfExtractor import PdfTextExtractor
from modules.TextCleaner import TextCleaner
# from modules.EmbeddingsCreator import EmbeddingsCreator


def main() -> None:

    settings = {
        "DATA_FOLDER": Path("data"),
        "PDF_FILE": Path("svejk_1_a_2.pdf"),
        "SKIP_PAGES": [0, 1, 2, 3, 4, 393],
        "RAW_TEXT_FILE": Path("raw_text.txt"),
        "WORDS_TOKENS_FILE": Path("words.pickle"),
        "SENTENCES_TOKENS_FILE": Path("sentences.pickle"),
        "CLEAN_TEXT_FILE": Path("clean_text.pickle"),
    }

    PdfTextExtractor.settings = settings
    TextCleaner.settings = settings
    # EmbeddingsCreator.settings = settings

    # PdfTextExtractor.extract_text_from_pdf()
    TextCleaner.clean_text()
    # EmbeddingsCreator.create_embeddings()


if __name__ == "__main__":
    main()
