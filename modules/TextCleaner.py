import pickle
from pathlib import Path
from typing import Union

from nltk import sent_tokenize, word_tokenize


class TextCleaner:

    settings: dict

    @classmethod
    def _save_to_pickle_file(cls, path: Path, content: Union[str, list, dict, tuple]) -> None:  # noqa: UP007
        with Path(path).open("wb") as f:
            pickle.dump(content, f)

    @classmethod
    def clean_text(cls) -> None:
        text = ""
        try:
            with Path(cls.settings["DATA_FOLDER"], cls.settings["RAW_TEXT_FILE"]).open("r", encoding="utf-8") as f:
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
            if cleaned_sentence.startswith(("– ", "— ")):  # noqa: RUF001
                cleaned_sentence = (cleaned_sentence[2:])
            cleaned_sentences += cleaned_sentence + "\n"

        cls._save_to_pickle_file(Path(cls.settings["DATA_FOLDER"], cls.settings["SENTENCES_TOKENS_FILE"]),
                                 cleaned_sentences)

        sentences_list = list(cleaned_sentences.splitlines())

        cls._save_to_pickle_file(Path(cls.settings["DATA_FOLDER"], cls.settings["SENTENCES_TOKENS_FILE"]),
                                 sentences_list)

        words_list = []

        for line in sentences_list:
            words = (word_tokenize(line, language="czech", preserve_line=False))
            for word in words:
                words_list.append(word)  # noqa: PERF402

        cls._save_to_pickle_file(Path(cls.settings["DATA_FOLDER"], cls.settings["WORDS_TOKENS_FILE"]),
                                 words_list)
