import ollama
import json

MODEL = "phi"

INTENT_SYSTEM_PROMPT = """
You are an intent classification engine.

Your job is to classify user input into ONE of these intents:
- chat
- create_calendar_event
- unknown

You MUST respond with ONLY valid JSON.
Do NOT explain anything.
Do NOT add extra text.

JSON schema:
{
  "intent": "chat | create_calendar_event | unknown",
  "confidence": number between 0 and 1,
  "reply": string or null
}

CRITICAL RULES:
- Casual conversation MUST be classified as "chat".
- Greetings, small talk, and questions like:
  "hi", "hello", "how are you", "what can you do", "who are you"
  are ALWAYS "chat".
- For intent = "chat", reply MUST be ONE short natural sentence.
- If the user is asking to schedule, plan, remind, or set something,
  intent MUST be "create_calendar_event" and reply MUST be null.
- Use "unknown" ONLY if the input is incomplete or ambiguous.

EXAMPLES:

User: hello
Output:
{"intent":"chat","confidence":0.9,"reply":"Hello. How can I help you?"}

User: how are you
Output:
{"intent":"chat","confidence":0.9,"reply":"I'm doing well and ready to help."}

User: what can you do
Output:
{"intent":"chat","confidence":0.9,"reply":"I can help plan tasks, schedules, and goals."}

User: schedule a meeting tomorrow at 6
Output:
{"intent":"create_calendar_event","confidence":0.95,"reply":null}

User: remind me to study
Output:
{"intent":"create_calendar_event","confidence":0.9,"reply":null}

User: tomorrow
Output:
{"intent":"unknown","confidence":0.4,"reply":null}
"""


def get_intent(user_input: str):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": INTENT_SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ],
    )

    raw = response["message"]["content"]

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "intent": "unknown",
            "confidence": 0.0,
            "reply": None,
        }


def main():
    print("Personal AI Assistant started.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Assistant: Goodbye.")
            break

        intent_data = get_intent(user_input)

        intent = intent_data["intent"]

        if intent == "chat":
            print("Assistant:", intent_data["reply"])

        elif intent == "create_calendar_event":
            print("Assistant: I detected a scheduling request. (Tool handling coming next.)")

        else:
            print("Assistant: Could you clarify what you want to do?")


if __name__ == "__main__":
    main()
