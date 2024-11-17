
Marketing Campaign Generator 🔥

This project is a **Streamlit** application designed to assist users in generating creative marketing campaigns, logo concepts, and personalized email content using **OpenAI GPT-4** and **DALL-E**. The app provides an easy-to-use interface for businesses and individuals to create professional marketing assets tailored to their brands.

---

## Features

1. **Marketing Campaign Generator**  
   - Generates comprehensive marketing campaigns based on user input.
   - Responses are delivered in Markdown format for readability and easy sharing.

2. **Logo Concept Generator**  
   - Creates detailed logo descriptions for brand identity.
   - Uses OpenAI's DALL-E to generate logo images based on the descriptions.

3. **Personalized Email Generator**  
   - Produces engaging and customized email content tailored to user specifications.
   - Ideal for marketing emails targeting specific audiences.

4. **Customizable UI**  
   - Aesthetic and user-friendly interface styled with CSS.
   - Responsive design for seamless user experience.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/marketing-campaign-generator.git
   cd marketing-campaign-generator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts ctivate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

5. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Launch the application and access the interface in your browser.
2. Fill out the required input fields for:
   - **Marketing Campaign**: Enter a brief description of your brand.
   - **Logo Concept**: Provide details about your brand's identity.
   - **Personalized Email**: Describe your product and target audience.
3. Click the respective **Generate** button to receive the output.
4. View and download your results directly from the app.

---

## Project Structure

- `app.py` - Main application code.
- `requirements.txt` - List of Python dependencies.
- `.env` - File to store sensitive environment variables like API keys.
- `README.md` - Documentation file (this file).

---

## Dependencies

- **Streamlit**: For creating the interactive web app.
- **OpenAI**: For GPT-4 and DALL-E API integration.
- **Pillow**: For processing and displaying images.
- **Requests**: For handling HTTP requests.
- **python-dotenv**: For managing environment variables.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## API Integration

This app uses the following APIs:

1. **OpenAI GPT-4**:
   - Used for generating text-based content like campaigns and emails.
   - Requires an API key from [OpenAI](https://openai.com/).

2. **OpenAI DALL-E**:
   - Used for generating logo images from descriptive text.

---
Enjoy using the **Marketing Campaign Generator**! 🚀
