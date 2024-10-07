# import openai
import os
import requests
import yaml

# Replace 'your-api-key' with your actual OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the YAML file containing icon descriptions
with open('icons/descriptions.yaml', 'r') as file:
    descriptions = yaml.safe_load(file)

# Use the description from the YAML file as the prompt
# prompt:dict = descriptions['saas_product_icon']

# Define the prompt for the image creation

number_of_images = 3

for image_index, item in descriptions['saas_product_icon'].items():
    print(f"Generating image for: {item["description"]}")
    prompt = f"Create an UI icon for a SaaS product, it should be black and white, abstract, and have a hand drawn look and feel with a white background. This is the description for the icon: {item["description"]} and nothing else."
    # Make a request to the OpenAI API to create an image
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=number_of_images,  # Number of images to generate
        size="1024x1024"  # Size of the image
    )

    for i in range(number_of_images):
        # Extract the image URL from the response
        image_url = response['data'][i]['url']

        # Download the image
        image_data = requests.get(image_url).content

        file_name = f"icons/generated_icons/{image_index}_{i}.png"
        # Save the image to a file
        with open(file_name, 'wb') as image_file:
            image_file.write(image_data)
        print(f"Image created and saved as: '{file_name}'")