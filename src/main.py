from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv
import logging
import sys
import os.path
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,

)
from llama_index.readers.database import DatabaseReader
from sqlalchemy import create_engine
from constants import SQLITE_QUERY


def main():

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

    load_dotenv()

    index = getIndex()

    query_engine = index.as_query_engine()
    response = query_engine.query("Qual o nome do vendedor que fez mais vendas?")
    print(response)

    pass

def getIndex():
    PERSIST_DIR = "./storage"

    existStorage = os.path.exists(PERSIST_DIR)

    if not existStorage:
        sqlite_url = 'sqlite:///' + os.environ['ABSOLUTE_PATH_TO_SDB']
        engine = create_engine(sqlite_url)
        dbReader = DatabaseReader(
            engine=engine,
        )

        query = SQLITE_QUERY
        documents = dbReader.load_data(query=query)

        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    return index


if __name__ == "__main__":
    main()