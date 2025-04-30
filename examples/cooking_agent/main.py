# examples/cooking_agent/main.py
import os
from dotenv import load_dotenv
from examples.cooking_agent.agent.cooking_agent import CookingAgent


def main():
    load_dotenv()
    agent = CookingAgent()
    source = input("Enter video URL or local audio path: ").strip()

    print("\n🔄 Processing video and extracting information...")
    result = agent.run(source)

    # Print transcript
    print(f"\n📝 Transcript:\n{result['transcript']}\n")

    # Print ingredients list
    print("🍅 Ingredients:")
    for item in result['ingredients']:
        print(f"  - {item}")

    # Print cooking steps
    print("\n👩‍🍳 Steps:")
    for idx, step in enumerate(result['steps'], 1):
        print(f"  {idx}. {step}")


if __name__ == '__main__':
    main()
