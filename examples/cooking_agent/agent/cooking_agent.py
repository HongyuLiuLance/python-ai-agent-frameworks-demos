from dotenv import load_dotenv
from examples.cooking_agent.tools.transcribe_tool import TranscribeVideoTool
from examples.cooking_agent.tools.extract_ingredients_tool import ExtractIngredientsTool
from examples.cooking_agent.tools.extract_steps_tool import ExtractStepsTool


class CookingAgent:
    """
    Orchestrates the cooking video processing pipeline:
    1. Download and transcribe video/audio
    2. Extract ingredients
    3. Extract cooking steps
    """

    def __init__(self):
        # Load environment variables
        load_dotenv()
        # Initialize tools
        self.transcriber = TranscribeVideoTool()
        self.ingredient_extractor = ExtractIngredientsTool()
        self.steps_extractor = ExtractStepsTool()

    def run(self, source: str) -> dict:
        """
        Run the complete pipeline on a video URL or local audio path.

        Args:
            source (str): YouTube URL or path to local audio file.

        Returns:
            dict: {
                "transcript": str,
                "ingredients": list[str],
                "steps": list[str]
            }
        """
        # 1. Transcription
        transcript = self.transcriber.run(source)

        # 2. Ingredient extraction
        ingredients = self.ingredient_extractor.run(transcript)

        # 3. Step extraction
        steps = self.steps_extractor.run(transcript)

        return {
            "transcript": transcript,
            "ingredients": ingredients,
            "steps": steps
        }


if __name__ == "__main__":
    # Example usage
    agent = CookingAgent()
    source = input("Enter video URL or local audio path: ").strip()
    result = agent.run(source)
    print("\nTranscript:\n", result["transcript"], "\n")
    print("Ingredients:")
    for item in result["ingredients"]:
        print(f" - {item}")
    print("\nSteps:")
    for i, step in enumerate(result["steps"], 1):
        print(f" {i}. {step}")
