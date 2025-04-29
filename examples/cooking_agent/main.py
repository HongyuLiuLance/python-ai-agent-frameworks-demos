# examples/cooking_agent/main.py

import os
from dotenv import load_dotenv
from examples.cooking_agent.tools.transcribe_tool import TranscribeVideoTool
from examples.cooking_agent.tools.extract_ingredients_tool import ExtractIngredientsTool
from examples.cooking_agent.tools.extract_steps_tool import ExtractStepsTool


def main():
    # Load environment variables
    load_dotenv()

    # Initialize tools
    transcriber = TranscribeVideoTool()
    ingredient_extractor = ExtractIngredientsTool()
    step_extractor = ExtractStepsTool()

    # Prompt user for input
    video_source = input("Enter cooking tutorial video URL or local audio file path: ").strip()

    # 1. Transcription
    print("\n🔄 Transcribing audio...")
    transcript = transcriber.run(video_source)
    print(f"\n📝 Transcript:\n\n{transcript}\n")

    # 2. Ingredient extraction
    print("🔄 Extracting ingredients...")
    ingredients = ingredient_extractor.run(transcript)

    print("\n🍅 Extracted Ingredients:")
    for entry in ingredients:
        if ":" in entry:
            name, qty = entry.split(":", 1)
            print(f"  - {name.strip()}: {qty.strip()}")
        else:
            print(f"  - {entry}")

    # 3. Step extraction
    print("\n👩‍🍳 Extracted Cooking Steps:")
    steps = step_extractor.run(transcript)
    for idx, step in enumerate(steps, start=1):
        print(f"  {idx}. {step}")

if __name__ == "__main__":
    main()
