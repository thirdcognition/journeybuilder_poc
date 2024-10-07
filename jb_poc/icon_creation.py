import openai
import os
import requests
import yaml

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the YAML file containing icon descriptions
with open('icons/descriptions.yaml', 'r') as file:
    descriptions = yaml.safe_load(file)

# Use the description from the YAML file as the prompt
# prompt:dict = descriptions['saas_product_icon']

# Define the prompt for the image creation


number_of_images = 3

negative_prompt = "Make sure that the he image has no additional text or other elements included besides the icon itself."

# Make a request to the OpenAI API to create an image
# response = openai.Image.create(
#     model="dall-e-3",
#
#     n=1,  # Number of images to generate
#     size="1024x1024"  # Size of the image
# )

for image_index, item in descriptions['saas_product_icon'].items():
    print(f"Generating image for: {item['description']}")
    prompt = f"Create a UI icon image which is used in a B2B SaaS product. The style should be black and white, ink, line drawing with a white background. This is the description of the icon: {item['description']}"
    # Make a request to the OpenAI API to create an image
    responses = []
    for i in range(0, number_of_images):
        print(f'Generate image version {i+1}')
        response = openai.Image.create(
           model="dall-e-3",
           prompt=f"{prompt} {negative_prompt}",
           n=1,  # Number of images to generate
           size="1024x1024"  # Size of the image
        )
        responses.append(response['data'][0]['url'])

    for i in range(0, number_of_images):
        # Download the image
        image_data = requests.get(responses[i]).content

        file_name = f"icons/generated_icons/{image_index}_{i+1}.png"
        # Save the image to a file
        with open(file_name, 'wb') as image_file:
           image_file.write(image_data)
        print(f"Image created and saved as: '{file_name}'")