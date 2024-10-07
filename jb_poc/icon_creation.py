import openai
import os
import requests

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt for the image creation
prompt = "Create an UI icon for a SaaS product, it should be black and white, abstract, and have a hand drawn look and feel with a white background. This is the description for the icon: A stylized tree with deep roots and spreading branches, encircled by a ribbon with the words “Core Values” and “Mission” and nothing else."

# Make a request to the OpenAI API to create an image
response = openai.Image.create(
    model="dall-e-3",
    prompt=prompt,
    n=1,  # Number of images to generate
    size="1024x1024"  # Size of the image
)

# Extract the image URL from the response
image_url = response['data'][0]['url']

# Download the image
image_data = requests.get(image_url).content

# Save the image to a file
with open('sample_image.png', 'wb') as image_file:
    image_file.write(image_data)

print("Image created and saved as 'sample_image.png'")