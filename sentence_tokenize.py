import re

def custom_sentence_tokenize(text):
    exlufixes = "(Q[0-9]+|[Mm]r|St|[Mm]rs|[Mm]s|[Dd]r|etc|[Yy]es|[nN]o)[\.]"
    prefix_pattern = re.compile(rf'({exlufixes})\s')
    text = re.sub(prefix_pattern, r'\1<prd> ', text)
    # print(text)
    sentenceList = re.split(r'[\.\!\?\n]\s', text)
    tokenized_sentences = []
    for sentence in sentenceList:
        sentence = sentence.replace("<prd>", "")
        tokenized_sentences.append(sentence)
    
    return tokenized_sentences

def custom_word_tokenize(text):
    exlufixes = "(Q[0-9]+|[Mm]r|St|[Mm]rs|[Mm]s|[Dd]r|etc|[Yy]es|[nN]o)[\.]"
    prefix_pattern = re.compile(rf'({exlufixes})\s')
    text = re.sub(prefix_pattern, r'\1<prd>', text)
    sentences = text.split(' ')
    word_tokenize_list = list()
    for sentence in sentences:
        sentence = sentence.replace("<prd>", " ")
        word_tokenize_list.append(sentence)
    return word_tokenize_list

if __name__=="__main__":
    text = """Ms. Gandhi put across her demand during a brief conversation she had with Mr. Modi just before the House proceedings started. Sources claimed that the Prime Minister, Dr. rahul gandhi, etc. had spoken to Ms. Gandhi to inquire about her well-being after Tuesday’s incident when a plane she was on developed a technical snag and made an emergency landing.\na brief conversation """
    sentences = custom_sentence_tokenize(text)
    word = custom_word_tokenize(text)
    print(sentences)
    print(word)
