class ReverseString:

    def reverseString(sentence: str) -> str:
        words = sentence.split()
        print(words)
        reverse_sentence = ""
        for word in words:
            rev_word = ""
            for i in range(len(word) - 1, -1, -1):
                rev_word += word[i]
            reverse_sentence += rev_word + " "
        return reverse_sentence.strip()


reversed_sentence = ReverseString.reverseString(sentence="Ranjan Thapa")
print(reversed_sentence)
