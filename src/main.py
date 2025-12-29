import ollama


SYSTEM_PROMPT = (
    "You are a helpful, calm personal AI assistant. "
    "Keep responses concise, clear, and practical."
)


def main():
    print("Personal AI Assistant started.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Assistant: Goodbye.")
            break

        response = ollama.chat(
            model="phi",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )

        print("Assistant:", response["message"]["content"])


if __name__ == "__main__":
    main()

