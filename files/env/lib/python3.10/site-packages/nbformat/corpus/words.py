import uuid


def generate_corpus_id():
    return uuid.uuid4().hex[:8]
