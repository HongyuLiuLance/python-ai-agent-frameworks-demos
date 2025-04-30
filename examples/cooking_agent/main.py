# examples/cooking_agent/main.py

import os
from dotenv import load_dotenv
from examples.cooking_agent.tools.transcribe_tool import TranscribeVideoTool
from examples.cooking_agent.tools.extract_ingredients_tool import ExtractIngredientsTool
from examples.cooking_agent.tools.extract_steps_tool import ExtractStepsTool
from examples.cooking_agent.app import Main_App
# from app import Main_App
# from tools.transcribe_tool import TranscribeVideoTool
# from tools.extract_ingredients_tool import ExtractIngredientsTool
# from tools.extract_steps_tool import ExtractStepsTool



def main():
    # Load environment variables
    load_dotenv()

    main_app = Main_App()

    # Initialize tools
    transcriber = TranscribeVideoTool()
    ingredient_extractor = ExtractIngredientsTool()
    step_extractor = ExtractStepsTool()

    # Prompt user for input
    video_source = input("Enter cooking tutorial video URL or local audio file path: ").strip()

    def process_url(url: str):
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
                ingredient = f"  - {name.strip()}: {qty.strip()}"
                # set the ingredient to widget
                main_app.add_ingredient(ingredient)
                print(ingredient)
            else:
                ingredient = f"  - {entry}"

                main_app.add_ingredient(ingredient)
                print(ingredient)
        
        # 3. Step extraction
        print("\n👩‍🍳 Extracted Cooking Steps:")
        steps = step_extractor.run(transcript)
        for idx, step in enumerate(steps, start=1):
            print(f"  {idx}. {step}")

    main_app.on_url_submit(process_url)

    main_app.execute()

if __name__ == "__main__":
    main()
