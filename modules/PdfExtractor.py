from pathlib import Path

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


class PdfTextExtractor:
    @classmethod
    def extract_text_from_pdf(cls, source_path: Path, destination_path: Path, skip_pages: list) -> None:
        text = ""
        # page_number = 0

        with Path(destination_path).open("w", encoding="utf-8") as f:
            for i, page_layout in enumerate(extract_pages(source_path)):
                if i not in skip_pages:
                    for element in page_layout:
                        if isinstance(element, LTTextContainer):
                            text += element.get_text()
            f.write(text)
