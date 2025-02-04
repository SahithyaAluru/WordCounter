def count_words(text):
    """Counts the number of words in a given text."""
    words = text.split()
    return len(words)

def main():
    """Handles user input and displays the word count."""
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")

main()
