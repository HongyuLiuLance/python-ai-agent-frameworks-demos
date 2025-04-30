# examples/cooking_agent/main.py
import os
from dotenv import load_dotenv
from examples.cooking_agent.agent.cooking_agent import CookingAgent
from examples.cooking_agent.app import Main_App

def main():
    load_dotenv()
    agent = CookingAgent()

    main_app = Main_App()


    def process_url(self, url: str):

        print("\n🔄 Processing video and extracting information...")
        result = agent.run(url)

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

    main_app.on_url_submit(process_url)

    main_app.execute()



if __name__ == '__main__':
    main()
