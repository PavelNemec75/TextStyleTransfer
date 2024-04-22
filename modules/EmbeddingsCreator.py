import os
import sys
from pathlib import Path

from modules.Helpers import Helpers

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf  # noqa: E402
from transformers import BertTokenizer, TFBertModel  # noqa: E402
import keras  # noqa: E402
import chromadb  # noqa: E402


class EmbeddingsCreator:
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = TFBertModel.from_pretrained("bert-base-uncased")

    @classmethod
    def create_embeddings(cls, source_path: Path, destination_path: Path, chunk_size: int) -> None:

        # chroma_client = chromadb.PersistentClient()
        # collection = chroma_client.get_or_create_collection(name="svejk_words")

        items = Helpers.read_pickle_file(source_path)

        embeddings_list = []

        for i in range(0, len(items), chunk_size):
            chunk_words = items[i:i + chunk_size]
            inputs = cls.tokenizer(chunk_words, return_tensors="tf", padding=True, truncation=True)
            outputs = cls.model(inputs)
            last_hidden_states = outputs.last_hidden_state
            embeddings = last_hidden_states.numpy().tolist()
            embeddings_list.append(embeddings)

            sys.stdout.write(f"\r{len(embeddings_list) * chunk_size}\\{len(items)} ")
            sys.stdout.flush()

            if i >= 3 * chunk_size:
                break

        Helpers.save_to_pickle_file(Path(destination_path),
                                    embeddings_list)

        # inputs = cls.tokenizer(words, return_tensors="tf", padding=True, truncation=True)
        # outputs = cls.model(inputs)
        # last_hidden_states = outputs.last_hidden_state
        # word_embeddings = last_hidden_states.numpy().tolist()
        # word_embeddings_list = [word_embeddings]

# chroma_client = chromadb.PersistentClient()
# # chroma_client = chromadb.Client()
#
#
# window_site = 2000
# step = 200
#
#
# def sliding_window(text: str, window_size: int, step: int) -> list:
#     windows = []
#     for i in range(0, len(text) - window_size + 1, step):
#         window = text[i:i + window_size]
#         windows.append(window)
#     return windows
#
#
# def process_file(file_path: Path) -> None:
#     with Path(file_path).open("r", encoding="utf-8") as file:
#         text = file.read()
#
#     inputs = tokenizer(text, return_tensors="tf", padding=True, truncation=True)
#     outputs = model(inputs)
#     last_hidden_states = outputs.last_hidden_state
#     sentence_embedding = tf.reduce_mean(last_hidden_states, axis=1)
#     embedding_list = sentence_embedding.numpy().tolist()
#
#     id_list = [str(i) for i, _ in enumerate(embedding_list)]
#
#     print("aa")
#
#     collection.add(
#         embeddings=embedding_list,
#         ids=id_list,
#     )
#     import sys
#     sys.exit()
#
#     # collection.add(
#     #     embeddings=embedding_list,
#     #     documents=["This is a document"],
#     #     metadatas=[{"source": "my_source"}],
#     #     ids="1",
#     # )
#
#     results = collection.query(
#         query_texts=["This is a query document"],
#         n_results=2,
#     )
#     print(results)
#
