"""
🍽️ AI Dish Recommender

This app allows users to select dietary restrictions, cuisine preferences, and spice tolerance to receive personalized dish recommendations with images and TTS playback.

Built with: Gradio + gTTS
"""

# =========================
# 📦 Install Required Libraries
# =========================
# !pip install gradio gtts
# ^ Uncomment above to install in Jupyter
# =========================

import gradio as gr
from gtts import gTTS
import tempfile

# =========================
# 🖼️ Dish Images
# =========================

dish_images = {
"Pasta": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Espaguetis_carbonara.jpg/1280px-Espaguetis_carbonara.jpg",
"Pizza": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Pizza-3007395.jpg/1280px-Pizza-3007395.jpg",
"Risotto": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Lemon_Pea_Risotto.jpg/1280px-Lemon_Pea_Risotto.jpg",
"Dumplings": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/HK_SYP_%E8%A5%BF%E7%87%9F%E7%9B%A4_Sai_Ying_Pun_Kwan_Yick_Building_%E5%90%8D%E6%98%9F%E6%B5%B7%E9%AE%AE%E9%85%92%E5%AE%B6_Star_Seafood_Restaurant_food_%E5%90%9E%E9%BA%B5_Wonton_dim_sum_October_2020_SS2_01.jpg/960px-HK_SYP_%E8%A5%BF%E7%87%9F%E7%9B%A4_Sai_Ying_Pun_Kwan_Yick_Building_%E5%90%8D%E6%98%9F%E6%B5%B7%E9%AE%AE%E9%85%92%E5%AE%B6_Star_Seafood_Restaurant_food_%E5%90%9E%E9%BA%B5_Wonton_dim_sum_October_2020_SS2_01.jpg?20240120034312",
"Kung Pao Chicken": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Kung-pao-shanghai.jpg/1280px-Kung-pao-shanghai.jpg",
"Mapo Tofu": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Chen_Mapo_Tofu.jpg/1280px-Chen_Mapo_Tofu.jpg",
"Tacos": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg/1280px-001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg",
"Enchiladas": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Enchilada_Rice_Beans.jpg",
"Quesadilla": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Chicken_Quesadilla_dish_at_Latin_Bistro_restaurant_Summit_NJ.JPG/1280px-Chicken_Quesadilla_dish_at_Latin_Bistro_restaurant_Summit_NJ.JPG",
}

# =========================
# 🎨 Custom Theme
# =========================

def create_custom_theme():
    """
    Create a custom Gradio theme with specific colors and styles.
    """
    primary = gr.themes.Color(
        c50="#fff0f5",
        c100="#ffd8e4",
        c200="#ffb0c8",
        c300="#f98aad",
        c400="#f46493",
        c500="#d43b6f",
        c600="#b0315e",
        c700="#8d274c",
        c800="#6a1e3a",
        c900="#471528",
        c950="#2f0b1d"
    )
    secondary = gr.themes.Color(
        c50="#fff0f5",
        c100="#fcd6e6",
        c200="#f9adc7",
        c300="#f683a8",
        c400="#f35a8a",
        c500="#ec7ca2",
        c600="#c26789",
        c700="#984f6e",
        c800="#6e3853",
        c900="#452139",
        c950="#2a1122"
    )

    return gr.themes.Soft(
        primary_hue=primary,
        secondary_hue=secondary,
        neutral_hue="stone",
        font=[gr.themes.GoogleFont("Quicksand"), "sans-serif"]
    ).set(
        # Buttons
        button_primary_background_fill="*primary_500",
        button_primary_background_fill_hover="*primary_600",
        button_primary_border_color="*primary_500",
        button_primary_text_color="white",
        button_secondary_background_fill="*secondary_500",
        button_secondary_background_fill_hover="*secondary_600",
        button_secondary_text_color="white",

        # Sliders / checkboxes / radio
        slider_color="*primary_500",
        checkbox_background_color_selected="*primary_500",
        radio_circle="*primary_500",

        # Typography
        body_text_color="*neutral_800",
        block_title_text_size="*text_lg",
        body_text_size="*text_md",

        # Feedback
        error_background_fill="#fbeaec",
        error_text_color="#7c2431",
    )

# =========================
# 🔊 Text-to-Speech (TTS)
# =========================

def speak_dish_name(dish_name):
    """
    Generate a TTS audio file from the given dish name using gTTS.
    """
    tts = gTTS(text=dish_name, lang="en")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

# =========================
# 🍽️ Dish Recommendation Logic
# =========================

def recommend(diet_restriction, food_type, spicy_level): 
    """
    Filter and return a list of recommended dishes based on user input.
    Also returns associated image URLs and the list of dish names.
    """
    # Define the menu with dish metadata
    menu = {
        "Pasta": {
            "cuisine": "Italian",
            "spicy": 1,
            "diet": ["Vegetarian", "Nut-Free"]
        },
        "Pizza": {
            "cuisine": "Italian",
            "spicy": 1,
            "diet": ["Nut-Free"]
        },
        "Risotto": {
            "cuisine": "Italian",
            "spicy": 1,
            "diet": ["Vegetarian", "Vegan", "Nut-Free"]
        },
        "Dumplings": {
            "cuisine": "Chinese",
            "spicy": 2,
            "diet": []
        },
        "Kung Pao Chicken": {
            "cuisine": "Chinese",
            "spicy": 4,
            "diet": ["Dairy-Free", "Gluten-Free", "Nut-Free"]
        },
        "Mapo Tofu": {
            "cuisine": "Chinese",
            "spicy": 4,
            "diet": ["Vegetarian", "Vegan", "Dairy-Free", "Gluten-Free"]
        },
        "Tacos": {
            "cuisine": "Mexican",
            "spicy": 3,
            "diet": ["Dairy-Free", "Gluten-Free", "Nut-Free"]
        },
        "Enchiladas": {
            "cuisine": "Mexican",
            "spicy": 3,
            "diet": []
        },
        "Quesadilla": {
            "cuisine": "Mexican",
            "spicy": 2,
            "diet": ["Vegetarian", "Vegan"]
        },
    }

    # Filter by cuisine
    filtered_dishes = []
    for dish, details in menu.items():
        # Check if dish matches any selected cuisine
        if details["cuisine"] in food_type:
            filtered_dishes.append(dish)

    # Filter by dietary restrictions
    for restriction in diet_restriction:
        filtered_dishes = [
            # Keep dishes that match the dietary restriction
            dish for dish in filtered_dishes if restriction in menu[dish]["diet"]
        ]

    # Filter by spiciness
    if spicy_level < 3:
        filtered_dishes = [
            # Keep dishes that are less spicy than the selected level
            dish for dish in filtered_dishes if menu[dish]["spicy"] < 3
        ]
    elif spicy_level > 3:
        filtered_dishes = [
            # Keep dishes that are more spicy than the selected level
            dish for dish in filtered_dishes if menu[dish]["spicy"] >= 3
        ]

    # Return results
    if filtered_dishes:
        # Text summary
        summary = f"Recommended dishes: {', '.join(sorted(set(filtered_dishes)))}"
        # Image URLs
        images = [dish_images[dish] for dish in filtered_dishes if dish in dish_images]
        # Return the summary, images, and filtered dish names
        return summary, images, filtered_dishes
    else:
        # If no dishes match, return a default message
        return "No recommendations available based on your preferences.", [], []

# =========================
# 🖥️ Gradio App Layout
# =========================

with gr.Blocks(theme=create_custom_theme()) as demo:
    # Set the title of the app
    gr.Markdown("# 🍽️ AI Dish Recommender", elem_id="app-title")

    with gr.Row(elem_id="main-row"): # Main layout row
        # Create two columns: one for input and one for output
        with gr.Column(): # Input column
            # Dietary restrictions
            diet_input = gr.CheckboxGroup(
                ["Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free", "Nut-Free"],
                label="Dietary Restrictions", elem_id="diet-box"
            )
            # Cuisine preferences
            cuisine_input = gr.Dropdown(
                ["Italian", "Chinese", "Mexican"], multiselect=True, label="Cuisine", elem_id="cuisine-box"
            )
            # Spiciness level slider
            spice_slider = gr.Slider(1, 5, value=3, step=1, label="Spicy Level", elem_id="spice-slider")
            # Submit button
            submit = gr.Button("🍴 Recommend", elem_id="submit-btn")

        with gr.Column(): # Output column
            # Text summary
            text_output = gr.Text(label="Recommended Dishes", elem_id="result-text")
            # Gallery of dish images
            gallery = gr.Gallery(label="Dish Images", elem_id="result-gallery")
            # State to hold dish names for TTS
            dish_list = gr.State([])
            # TTS audio output
            tts_output = gr.Audio(label="Pronunciation", elem_id="tts-audio")

            # Predefined buttons, hidden by default
            dish_tts_buttons = {}
            for dish in dish_images:
                btn = gr.Button(f"🔊 {dish}", visible=False)
                btn.click(fn=lambda d=dish: speak_dish_name(d), outputs=tts_output)
                dish_tts_buttons[dish] = btn

    # Call recommend function
    submit.click(
        recommend,
        inputs=[diet_input, cuisine_input, spice_slider],
        outputs=[text_output, gallery, dish_list]
    )

    gr.Examples( # Add example inputs
    examples=[
        [[], ["Italian", "Chinese", "Mexican"], 2],
        [["Vegetarian"], ["Italian"], 3],
        [["Gluten-Free", "Nut-Free"], ["Chinese"], 2],
        [["Vegan"], ["Italian", "Chinese", "Mexican"], 5],
        [["Dairy-Free"], ["Italian", "Mexican"], 4],
    ],
    inputs=[diet_input, cuisine_input, spice_slider],
    outputs=[text_output, gallery, dish_list],
    fn=recommend,
    cache_examples=False,
    )

    # Show only the TTS buttons for returned dishes
    def update_button_visibility(dishes):
        updates = {}
        for dish, btn in dish_tts_buttons.items():
            # Update visibility based on whether the dish is in the returned list
            updates[btn] = gr.update(visible=dish in dishes)
        return updates

    # Update TTS button visibility when dish list changes
    dish_list.change(fn=update_button_visibility, inputs=dish_list, outputs=list(dish_tts_buttons.values()))

# =========================
# Launch the Gradio app
# =========================

if __name__ == "__main__":
    demo.launch(share=True)