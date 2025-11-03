from core import get_response


def main():
    """Simple CLI interface using core.get_response"""
    print("✅ Welcome! I'm your AI Python Tutor. Type 'quit' to exit.\n")
    print("Teaching style: Visual (diagrams & flowcharts)")
    print("Available topics: Variables, Loops, Functions, Lists, and more!\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() == "quit":
                print("\n👋 Goodbye! Keep practicing!")
                break

            if not user_input:
                continue

            print("\nAssistant: ", end="", flush=True)
            response = get_response(user_input)
            print(response)
            print()

        except KeyboardInterrupt:
            print("\n\n👋 Session ended. Goodbye!")
            break
        except Exception as e:
            print(f"\n⚠️ Error: {e}")


if __name__ == "__main__":
    main()