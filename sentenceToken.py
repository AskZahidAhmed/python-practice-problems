import re, sys
from nltk.tokenize import sent_tokenize

def custom_sentence_tokenize(text):
    exlufixes = "(Q[0-9]+|[Mm]r|St|[Mm]rs|Ms|[Dd]r|etc|Jr|Inc|Smith|[Yy]es|[nN]o)[\.]"
    prefix_pattern = re.compile(rf'({exlufixes})\s')
    text = re.sub(prefix_pattern, r'\1<prd> ', text)
    print(text)
    sentences = sent_tokenize(text)

    tokenized_sentences = []
    for sentence in sentences:
        sentence = sentence.replace("<prd>", "")
        tokenized_sentences.append(sentence)
    
    return tokenized_sentences

text = "mr. Smith went to dr. Brown's house. Yes, he yes. did."
sentences = custom_sentence_tokenize(text)
print(sentences)



"""
def file_read(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        line = f.read()
        line = re.sub(r'\n', ' ', line)
    return line

def file_write(filename, content):
    with open(filename, 'a', encoding="utf-8") as w:
        w.write(content)
        w.write('\n')

if __name__=="__main__":
    text = file_read(sys.argv[1])
    filename = sys.argv[2]
    sentences = custom_sentence_tokenize(text)
    for sentence in sentences:
        file_write(filename, sentence)
        if 'abbreviation' in sentence:
            print(sentence)

"""