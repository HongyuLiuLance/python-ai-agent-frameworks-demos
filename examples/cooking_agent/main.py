# examples/cooking_agent/main.py

from dotenv import load_dotenv
load_dotenv()

from examples.cooking_agent.agent.cooking_agent import CookingAgent
from examples.cooking_agent.app import Main_App

def clear_layout(layout):
    """
    Remove and delete all widgets from the given QLayout.
    """
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

def main():
    agent = CookingAgent()
    app = Main_App()

    def process_url(url: str):
        # 1. Empty the old list of ingredients and steps
        clear_layout(app.lst_layout_ingredient)
        clear_layout(app.lst_layout_recipt)

        # 2. Calling the Agent Full Pipeline
        result = agent.run(url)

        # 3. Populate new ingredient list
        for ing in result["ingredients"]:
            app.add_ingredient(ing)

        # 4. Fill in the new production steps
        for step in result["steps"]:
            app.add_steps(step)

    app.on_url_submit(process_url)
    app.execute()

if __name__ == "__main__":
    main()