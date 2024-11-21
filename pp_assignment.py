import json
import random

# File to store flashcards
FLASHCARD_FILE = 'flashcards.json'


# Load flashcards from a file
def load_flashcards():
    try:
        with open(FLASHCARD_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save flashcards to a file
def save_flashcards(flashcards):
    with open(FLASHCARD_FILE, 'w') as file:
        json.dump(flashcards, file)


# Add a new flashcard
def add_flashcard(flashcards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards[question] = answer
    print("Flashcard added!")


# View all flashcards
def view_flashcards(flashcards):
    if not flashcards:
        print("No flashcards available.")
        return
    for question, answer in flashcards.items():
        print(f"Q: {question}")
        print(f"A: {answer}\n")


# Quiz with flashcards
def quiz(flashcards):
    if not flashcards:
        print("No flashcards available.")
        return

    questions = list(flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        print(f"Q: {question}")
        user_answer = input("Your answer: ")
        correct_answer = flashcards[question]
        if user_answer.lower().strip() == correct_answer.lower().strip():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
        print()


def main():
    flashcards = load_flashcards()

    while True:
        print("\nFlashcard App")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Quiz Yourself")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_flashcard(flashcards)
            save_flashcards(flashcards)
        elif choice == '2':
            view_flashcards(flashcards)
        elif choice == '3':
            quiz(flashcards)
        elif choice == '4':
            save_flashcards(flashcards)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()