from pathlib import Path

from nltk import sent_tokenize, word_tokenize

from modules.Helpers import Helpers


class TextProcessor:

    @classmethod
    def process_text_file(cls,
                          text_file: Path,
                          word_tokens_file: Path,
                          sentence_tokens_file: Path,
                          paragraph_tokens_file: Path) -> None:
        text = ""
        try:
            with Path(text_file).open("r", encoding="utf-8") as f:
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

        """paragraphs"""
        text_lines = cleaned_sentences.split("\n")
        chunk_size = 10
        chunks = [text_lines[i:i + chunk_size] for i in range(0, len(text_lines), chunk_size)]
        Helpers.save_to_pickle_file(paragraph_tokens_file, chunks)

        """sentences"""
        sentences_list = list(cleaned_sentences.splitlines())
        Helpers.save_to_pickle_file(sentence_tokens_file, sentences_list)

        """words"""
        words_list = []
        for line in sentences_list:
            words = (word_tokenize(line, language="czech", preserve_line=False))
            for word in words:
                words_list.append(word)  # noqa: PERF402
        Helpers.save_to_pickle_file(word_tokens_file, words_list)
