def find_word_difference(text1, text2):
    words1 = text1.split()
    words2 = text2.split()

    # Find words that are present in text1 but not in text2
    difference_text1 = [word for word in words1 if word not in words2]

    # Find words that are present in text2 but not in text1
    difference_text2 = [word for word in words2 if word not in words1]

    return difference_text1, difference_text2

difference_text1, difference_text2 = find_word_difference(text1, text2)
print("Words present in text1 but not in text2:", difference_text1)
print("Words present in text2 but not in text1:", difference_text2)

