# Import the required libraries
import streamlit as st  # Streamlit is used for creating the web app interface
import openai  # OpenAI library for interacting with GPT and DALL-E models
import os  # Library to access environment variables
import requests  # Library to send HTTP requests
from PIL import Image  # Pillow for image processing
from io import BytesIO  # Input/output stream for handling binary data
from dotenv import load_dotenv  # Load environment variables from a .env file

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to trim the description to fit within the limit
def trim_prompt(prompt, max_length=1000):
    """
    Trims the input prompt to the specified max_length. Adds ellipsis if trimmed.

    Args:
        prompt (str): The input string.
        max_length (int): Maximum allowed length of the string.

    Returns:
        str: Trimmed string.
    """
    if len(prompt) > max_length:
        return prompt[:max_length - 3] + "..."  # Truncate and add ellipsis
    return prompt

# Function to generate a marketing campaign using OpenAI
def get_response_openai(prompt):
    """
    Generates a marketing campaign based on the user's prompt using OpenAI GPT.

    Args:
        prompt (str): User's input describing their brand and requirements.

    Returns:
        str: Generated marketing campaign in markdown format.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are an expert creative marketer. Create a campaign for the brand the user enters. Respond in markdown format."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message['content']
    except Exception as e:
        print("Error in creating campaigns from OpenAI:", str(e))
        return "Failed to generate campaign. Please try again later."

# Function to generate a logo description using OpenAI
def get_logo_description(prompt):
    """
    Generates a detailed description for a logo based on the user's brand input.

    Args:
        prompt (str): User's input describing their brand identity.

    Returns:
        str: Logo description.
    """    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are an expert logo designer. Create a description for a logo based on the brand the user enters. Be descriptive and imaginative."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message['content']
    except Exception as e:
        print("Error in generating logo description from OpenAI:", str(e))
        return "Failed to generate logo description. Please try again later."

# Function to generate a logo image using OpenAI's DALL-E based on the description
def generate_logo_image(description):
    """
    Generates a logo image based on a description using OpenAI's DALL-E.

    Args:
        description (str): Logo description to guide the image generation.

    Returns:
        str: URL of the generated image or None if an error occurs.
    """
    try:
        # Ensure the description fits the prompt limit
        trimmed_description = trim_prompt(description, max_length=1000)
        
        response = openai.Image.create(
            prompt=trimmed_description,
            n=1,
            size="1024x1024"  # You can adjust the size based on your requirements
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print("Error in generating logo image:", str(e))
        return None

# Function to generate personalized emails using OpenAI
def generate_personalized_email(prompt):
    """
    Creates personalized email content based on the user's brand and target audience.

    Args:
        prompt (str): User's input with brand details and audience.

    Returns:
        str: Generated email content.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a creative copywriter specializing in crafting personalized, engaging email content. Generate an email based on the details the user provides. Make it captivating and tailored to the target audience."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message['content']
    except Exception as e:
        print("Error in generating personalized email from OpenAI:", str(e))
        return "Failed to generate personalized email. Please try again later."

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f8f9fa, #e2e6ea);
            font-family: 'Segoe UI', sans-serif;
            color: #333;
        }
        .main-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 0px 30px rgba(0,0,0,0.1);
            margin-top: 30px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }
        .title {
            font-family: 'Segoe UI', sans-serif;
            font-size: 3.2em;
            color: #1a73e8;
            text-align: center;
            margin-top: 0;
            margin-bottom: 30px;
        }
        .prompt-box {
            font-size: 1.15em;
            color: #444;
        }
        button {
            background-color: #1a73e8;
            color: white;
            font-size: 1.2em;
            border: none;
            border-radius: 8px;
            padding: 14px 28px;
            cursor: pointer;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
            width: 100%;
            text-align: center;
        }
        button:hover {
            background-color: #1669c1;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
        }
        .generated-content {
            background-color: #f1f3f4;
            padding: 25px;
            border-radius: 12px;
            font-family: 'Courier New', monospace;
            font-size: 1.1em;
            margin-top: 25px;
            box-shadow: 0px 2px 15px rgba(0,0,0,0.08);
        }
        footer {
            text-align: center;
            font-size: 0.85em;
            padding: 25px;
            color: #6c757d;
        }
        .section-title {
            text-align: center;
            font-size: 2.8em;
            color: #1a73e8;
            margin-top: 50px;
            margin-bottom: 25px;
        }
        hr {
            border-top: 2px solid #1a73e8;
            margin: 50px 0;
        }
        .logo-image {
            margin-top: 20px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 60%;
            border: 3px solid #1a73e8;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "campaign_text" not in st.session_state:
    st.session_state.campaign_text = ""
if "logo_description" not in st.session_state:
    st.session_state.logo_description = ""
if "logo_image_url" not in st.session_state:
    st.session_state.logo_image_url = None
if "email_content" not in st.session_state:
    st.session_state.email_content = ""

# Set the title of the Streamlit application
st.markdown('<h1 class="title">Marketing Campaign Generator 🔥</h1>', unsafe_allow_html=True)

# Create main container for the content
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Create a text area for the user to input their brand name and a short description of their brand
prompt = st.text_area(
    "Enter your brand name and a short description of your brand. We will generate a marketing campaign for you 🚀.",
    placeholder="Example: 'Awesome Coffee - A specialty coffee brand that focuses on ethically sourced, organic beans with a rich and smooth flavor.'",
    height=150,
)

# If the "Generate" button is clicked, generate the marketing campaign
if st.button("Generate Campaign", key="generate-campaign-button", help="Click to generate your marketing campaign"):
    if prompt.strip() == "":
        st.error("Please enter a brand name and description.")
    else:
        with st.spinner('Generating your campaign... Please wait...'):
            st.session_state.campaign_text = get_response_openai(prompt)
        
        st.subheader("Generated Campaign")
        st.markdown(f'<div class="generated-content">{st.session_state.campaign_text}</div>', unsafe_allow_html=True)

# Display previously generated campaign if available
if st.session_state.campaign_text:
    st.subheader("Generated Campaign")
    st.markdown(f'<div class="generated-content">{st.session_state.campaign_text}</div>', unsafe_allow_html=True)

# Divider for UI enhancement
st.markdown('<hr>', unsafe_allow_html=True)

# Add another section for logo generation
st.markdown('<h2 class="section-title">Generate a Brand Logo 🎨</h2>', unsafe_allow_html=True)

# Text input for logo prompt
logo_prompt = st.text_area(
    "Enter your brand name and a brief description of your brand identity. We will create a logo concept for you.",
    placeholder="Example: 'Awesome Coffee - Warm, inviting, and artisanal with a focus on eco-friendly packaging.'",
    height=150,
)

# If the "Generate Logo" button is clicked, generate the logo description and image
if st.button("Generate Logo", key="generate-logo-button", help="Click to generate your logo concept"):
    if logo_prompt.strip() == "":
        st.error("Please enter a brand name and description.")
    else:
        with st.spinner('Creating your logo concept... Please wait...'):
            st.session_state.logo_description = get_logo_description(logo_prompt)
        
        st.subheader("Logo Concept")
        st.markdown(f'<div class="generated-content">{st.session_state.logo_description}</div>', unsafe_allow_html=True)
        
        # Generate logo image
        with st.spinner('Generating logo image... Please wait...'):
            st.session_state.logo_image_url = generate_logo_image(st.session_state.logo_description)
        
        if st.session_state.logo_image_url:
            try:
                # Display the image
                response = requests.get(st.session_state.logo_image_url)
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    st.markdown(f'<img src="{st.session_state.logo_image_url}" alt="Generated Logo" class="logo-image">', unsafe_allow_html=True)
                else:
                    st.error("Failed to fetch the image from the URL.")
            except Exception as e:
                st.error(f"Error loading image: {e}")
        else:
            st.error("Failed to generate logo image. Please try again later.")

# Display previously generated logo description and image if available
if st.session_state.logo_description:
    st.subheader("Logo Concept")
    st.markdown(f'<div class="generated-content">{st.session_state.logo_description}</div>', unsafe_allow_html=True)
if st.session_state.logo_image_url:
    st.markdown(f'<img src="{st.session_state.logo_image_url}" alt="Generated Logo" class="logo-image">', unsafe_allow_html=True)

# Divider for UI enhancement
st.markdown('<hr>', unsafe_allow_html=True)

st.markdown('<h2 class="section-title">Generate Personalized Emails ✉️</h2>', unsafe_allow_html=True)

# Text input for email prompt
email_prompt = st.text_area(
    "Enter your brand name, product details, and target audience. We will generate a personalized email for you.",
    placeholder="Example: 'Awesome Coffee - Introducing a new flavor - Pumpkin Spice Latte. Targeting young professionals who love seasonal flavors.'",
    height=150,
)

# If the "Generate Email" button is clicked, generate the personalized email
if st.button("Generate Personalized Email", key="generate-email-button", help="Click to generate your personalized email"):
    if email_prompt.strip() == "":
        st.error("Please enter your brand, product details, and target audience.")
    else:
        with st.spinner('Creating your personalized email... Please wait...'):
            st.session_state.email_content = generate_personalized_email(email_prompt)
        
        st.subheader("Generated Personalized Email")
        st.markdown(f'<div class="generated-content">{st.session_state.email_content}</div>', unsafe_allow_html=True)

# Display previously generated email content if available
if st.session_state.email_content:
    st.subheader("Generated Personalized Email")
    st.markdown(f'<div class="generated-content">{st.session_state.email_content}</div>', unsafe_allow_html=True)

# Add a footer
st.markdown('</div>', unsafe_allow_html=True)  # Close main container
st.markdown('<footer>Created by ANTHONY TABET - Powered by LLMs </footer>', unsafe_allow_html=True)