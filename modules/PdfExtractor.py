from pathlib import Path

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


class PdfTextExtractor:

    settings: dict

    @classmethod
    def extract_text_from_pdf(cls) -> None:
        text = ""
        # page_number = 0

        with Path(cls.settings["DATA_FOLDER"], cls.settings["RAW_TEXT_FILE"]).open("w", encoding="utf-8") as f:
            for i, page_layout in enumerate(extract_pages(Path(cls.settings["DATA_FOLDER"], cls.settings["PDF_FILE"]))):
                if i not in cls.settings["SKIP_PAGES"]:
                    # page_number += 1
                    # text += f"\n\n<page_{page_number}>"
                    for element in page_layout:
                        if isinstance(element, LTTextContainer):
                            text += element.get_text()
                    # text += f"</page_{page_number}>"
            f.write(text)
