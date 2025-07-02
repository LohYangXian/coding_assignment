

class WordReverserProcessor:
    def __init__(self):
        pass

    def reverse_words(self, words):
        def reverse_word(word):
            left_pointer, right_pointer = 0, len(word) - 1
            reversed_word = list(word)
            while left_pointer < right_pointer:
                if not reversed_word[left_pointer].isalnum(): left_pointer += 1
                elif not reversed_word[right_pointer].isalnum(): right_pointer -= 1
                else:
                    reversed_word[left_pointer], reversed_word[right_pointer] = reversed_word[right_pointer], reversed_word[left_pointer]
                    left_pointer += 1
                    right_pointer -= 1
            return "".join(reversed_word)

        return " ".join([reverse_word(word) for word in words.split(" ")])

def main():
    word_reverser = WordReverserProcessor()
    print(word_reverser.reverse_words("String; 2be reversed..."))
    assert word_reverser.reverse_words("String; 2be reversed...") == "gnirtS; eb2 desrever..."
    return 0

if __name__ == "__main__":
    main()