import sys

def calculate_average_words_per_sentence(filename):
    with open(filename, 'r') as file:
        sentences = file.read().split('.')
        wordCounts = [len(sentence.split()) for sentence in sentences]
        averageWords = sum(wordCounts) / len(sentences)
        return averageWords

filename = sys.argv[1]
averageWords = calculate_average_words_per_sentence(filename)
print(f"Average words per sentence: {averageWords:.2f}")

def compare_sentences(filename1, filename2):
    with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
        sentences1 = file1.read().split('.')
        sentences2 = file2.read().split('.')

        for i, (sentence1, sentence2) in enumerate(zip(sentences1, sentences2)):
            print(f"Comparison {i + 1}:")
            print(f"File 1 Sentence: {sentence1.strip()}")
            print(f"File 2 Sentence: {sentence2.strip()}")
            # Perform your desired comparison logic here
            print("=" * 30)

filename1 = 'file1.txt'
filename1 = 'file2.txt'
compare_sentences(filename1, filename2)

def compare_sentence_lengths(filename1, filename2):
    with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
        sentences1 = file1.read().split('.')
        sentences2 = file2.read().split('.')

        for i, (sentence1, sentence2) in enumerate(zip(sentences1, sentences2)):
            length1 = len(sentence1.split())
            length2 = len(sentence2.split())
            length_difference = abs(length1 - length2)

            print(f"Comparison {i + 1}:")
            print(f"Sentence 1 Length: {length1} words")
            print(f"Sentence 2 Length: {length2} words")
            print(f"Length Difference: {length_difference} words")
            print("=" * 30)



filename1 = 'file1.txt'
filename2 = 'file2.txt'
compare_sentence_lengths(filename1, filename2)


