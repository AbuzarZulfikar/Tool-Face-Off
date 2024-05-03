# Hackathon 
Tool Face-Off: OpenAI Assistants API VS Llama-Index/MongoDB. An Eval-Driven Battle. Unveil the ultimate AI Tool in the clash of titans, and win main &amp; special prize for Tool Set as Usage

## Description

The Emotion Detection Chatbot is a project that utilizes LLmaindex for data retrieval, MongoDB for data storage, and Assistant API for natural language processing. It's designed to detect emotions in user input and respond accordingly, providing counseling or emotional support.

## Features

- Emotion detection: The chatbot can identify emotions in user input.
- Counseling: Provides counseling or support based on detected emotions.
- Data storage: Stores user interactions in MongoDB for further analysis and improvement.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/emotion-detection-chatbot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd emotion-detection-chatbot
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up MongoDB:
   - Install MongoDB on your system.
   - Start MongoDB service.
   - Update the MongoDB URI in `config.py` if necessary.

5. Obtain API keys:
   - Obtain LLmaindex API key.
   - Obtain Assistant API key.

6. Update configuration:
   - Update LLmaindex and Assistant API keys in `config.py`.

## Usage

1. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

2. Start the application:
    ```bash
    python app.py
    ```

3. Open your web browser and navigate to `http://localhost:5000`.

4. Interact with the chatbot.

## Configuration

The project configuration is stored in `config.py`. You can update the following configurations:

- `MONGODB_URI`: MongoDB connection URI.
- `LLMAINDEX_API_KEY`: LLmaindex API key.
- `ASSISTANT_API_KEY`: Assistant API key.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- LLmaindex for data retrieval.
- MongoDB for data storage.
- Assistant API for natural language processing.

