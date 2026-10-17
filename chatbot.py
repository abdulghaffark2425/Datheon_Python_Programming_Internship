import json
import os
import re

DATASET_FILE = "sample_faq.json"
EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}


def load_faq_data(filepath):
    if not os.path.exists(filepath):
        print(f"[Warning] Dataset file '{filepath}' not found. Loading default responses.")
        return {"greetings": ["hello", "hi", "hey"], "faqs": []}

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def get_response(user_input, faq_data):
    clean_input = user_input.strip().lower()

    if not clean_input:
        return "Please enter a query or type 'exit' to quit."

    if clean_input in EXIT_COMMANDS:
        return None

    # Check for greetings
    greetings = faq_data.get("greetings", [])
    if any(re.search(rf"\b{re.escape(g)}\b", clean_input) for g in greetings):
        return "Hello! How can I assist you with your internship queries today?"

    # Check for FAQ match using keyword matching
    faqs = faq_data.get("faqs", [])
    best_match = None
    max_score = 0

    for faq in faqs:
        question = faq["question"].lower()
        # Count overlapping keywords between input and question
        keywords = [word for word in clean_input.split() if len(word) > 2]
        score = sum(1 for word in keywords if word in question)

        if score > max_score:
            max_score = score
            best_match = faq["answer"]

    if max_score > 0 and best_match:
        return best_match

    # Graceful fallback response
    return (
        "I'm sorry, I don't have an answer for that. You can ask about: "
        "hours of operation, submitting internship projects, or certificate issuance."
    )


def run_chatbot():
    faq_data = load_faq_data(DATASET_FILE)

    print("=" * 60)
    print("       Datheon Rule-Based Terminal Assistant / Chatbot")
    print("=" * 60)
    print("Ask a question about the internship! Type 'exit' or 'bye' to stop.\n")

    while True:
        try:
            user_input = input("You: ")
            response = get_response(user_input, faq_data)

            if response is None:
                print("Bot: Thank you for using Datheon Assistant. Goodbye!")
                break

            print(f"Bot: {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session ended. Goodbye!")
            break


if __name__ == "__main__":
    run_chatbot() 
