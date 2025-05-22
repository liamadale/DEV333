# Starter code - complete the missing parts
import gradio as gr

def recommend(food_type, spicy_level, diet_restriction):
    menu = { "Italian": ["Pasta", "Pizza", "Risotto"], 
         "Chinese": ["Dumplings", "Kung Pao Chicken", "Mapo Tofu"], 
         "Mexican": ["Tacos", "Enchiladas", "Quesadilla"] } 
    
    # Task: Add your recommendation logic here

    # Consider food types:

    # Consider spicy level:

    # Consider dietary restrictions:

    return "Recommended dish: ..."

# Task: Create input components for:
# - Food type dropdown (Italian, Chinese, Mexican)
# - Spiciness slider (1-5)
# - Submit button

gradioGUI = gr.Interface(
    recommend,
    [
        gr.CheckboxGroup(["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free"], label="Dietary Restrictions", info="Select any dietary preferences or restrictions"),
        gr.Dropdown(
            ["Italian", "Chinese", "Mexican"], label="Cuisine", multiselect=True, info="Choose what cuisine you're interested in!"
        ),
        gr.Slider(1, 5, value=3, label="Spicy Level", info="Choose between 1 and 5"),
    ],
    "text",
    examples=[
        [["Vegetarian"], ["Italian"], 3],
        [["Gluten-Free", "Nut-Free"], ["Chinese"], 2],
        [["Vegan"], ["Italian, Chinese, Mexican"], 5],
        [["Dairy-Free"], ["Italian, Mexican"], 4],
    ]
)

# Task: Launch interface with shareable URL

# Task: 
# 1. Add a checkbox for dietary restrictions (Vegetarian/Vegan)
# 2. Use gr.Examples() to add pre-set combinations
# 3. Implement image output showing of Example dishes in step 2.

# Task: Apply these improvements:
# 1. Add CSS styling for a food-themed interface
# 2. Add audio output with pronunciation of dish names

if __name__ == "__main__":
    gradioGUI.launch()