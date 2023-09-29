import re
from transformers import BertForTokenClassification, BertTokenizer
import torch

# Define a function to preprocess and perform NER
def extract_named_entities(text):
    # Define a regex pattern to remove non-alphanumeric characters except spaces
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Load the pre-trained BERT model for NER
    model = BertForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

    # Tokenize the cleaned text
    tokens = tokenizer.tokenize(clean_text)

    # Predict named entities
    input_ids = tokenizer.encode(tokens, add_special_tokens=True)
    input_ids = torch.tensor(input_ids).unsqueeze(0)  # Batch size of 1

    with torch.no_grad():
        outputs = model(input_ids)

    predictions = torch.argmax(outputs.logits, dim=2)

    # Post-process results
    entity_labels = [model.config.id2label[label_id] for label_id in predictions[0].tolist()]
    named_entities = []

    current_entity = ""
    current_label = ""

    for token, label in zip(tokens, entity_labels):
        if label.startswith("B-"):  # Beginning of an entity
            if current_entity:
                named_entities.append((current_entity.strip(), current_label))
            current_entity = token
            current_label = label[2:]
        elif label.startswith("I-"):  # Inside an entity
            current_entity += " " + token
        else:  # O (Outside) or other labels
            if current_entity:
                named_entities.append((current_entity.strip(), current_label))
            current_entity = ""
            current_label = ""

    # Add the last entity if present
    if current_entity:
        named_entities.append((current_entity.strip(), current_label))

    return named_entities

# Example usage
input_text = "Apple Inc. is headquartered in Cupertino, California."
named_entities = extract_named_entities(input_text)
print(named_entities)

