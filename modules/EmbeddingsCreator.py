import os
from pathlib import Path

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from multiprocessing import Pool  # noqa: E402
import tensorflow as tf  # noqa: E402
from transformers import BertTokenizer, TFBertModel  # noqa: E402
import keras  # noqa: E402
import chromadb  # noqa: E402


class EmbeddingsCreator:

    @classmethod
    def create_embeddings(cls) -> None:
        pass






# chroma_client = chromadb.PersistentClient()
# # chroma_client = chromadb.Client()
# collection = chroma_client.get_or_create_collection(name="verofi")
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
