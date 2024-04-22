from pathlib import Path

from modules.PdfExtractor import PdfTextExtractor
from modules.TextProcessor import TextProcessor
from modules.EmbeddingsCreator import EmbeddingsCreator


def main() -> None:

    DATA_FOLDER = Path("data")
    PDF_FILE = Path(DATA_FOLDER, "svejk_1_a_2.pdf")
    RAW_TEXT_FILE = Path(DATA_FOLDER, "raw_text.txt")
    SKIP_PAGES = [0, 1, 2, 3, 4, 393]

    WORD_TOKENS_FILE = Path(DATA_FOLDER, "words.pickle")
    SENTENCE_TOKENS_FILE = Path(DATA_FOLDER, "sentences.pickle")
    PARAGRAPH_TOKENS_FILE = Path(DATA_FOLDER, "paragraphs.pickle")

    WORD_EMBEDDING_FILE = Path(DATA_FOLDER, "word_embeddings.pickle")
    SENTENCE_EMBEDDING_FILE = Path(DATA_FOLDER, "sentence_embeddings.pickle")
    PARAGRAPH_EMBEDDING_FILE = Path(DATA_FOLDER, "paragraph_embeddings.pickle")

    # PdfTextExtractor.extract_text_from_pdf(PDF_FILE, RAW_TEXT_FILE, SKIP_PAGES)
    # TextProcessor.process_text_file(RAW_TEXT_FILE, WORD_TOKENS_FILE, SENTENCE_TOKENS_FILE, PARAGRAPH_TOKENS_FILE)
    # EmbeddingsCreator.create_embeddings(WORD_TOKENS_FILE, WORD_EMBEDDING_FILE, 1000)
    EmbeddingsCreator.create_embeddings(SENTENCE_TOKENS_FILE, SENTENCE_EMBEDDING_FILE, 100)
    # EmbeddingsCreator.create_embeddings(PARAGRAPH_TOKENS_FILE, PARAGRAPH_EMBEDDING_FILE, 10)


if __name__ == "__main__":
    main()
