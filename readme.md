# Chat with Raga.ai Docs

This is a Streamlit application that allows users to interact with the Raga.ai documentation through a conversational interface. The application uses various APIs and models to generate responses based on user queries and the provided context from the documentation.

## Features

- **Interactive Query Input**: Users can input their questions related to Raga.ai documentation.
- **Contextual Responses**: The application searches for relevant context within the documentation and provides detailed, accurate responses.
- **Integration with Qdrant and Cohere**: Utilizes Qdrant for vector storage and similarity search, and Cohere for generating embeddings.

## Installation

To run this application, you need to have Python installed. Then, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Ensure you have the necessary API keys for Cohere, Groq, and Qdrant services. Update the `cohere_api_key`, `groq_api_key`, and `qdrant_api_key` variables in the script with your keys.

## Usage

To start the Streamlit application, run the following command in your terminal:

```sh
streamlit run app.py
```

Replace `app.py` with the name of your Python script if it's different.

## How It Works

1. **Embedding Generation**: The application uses Cohere's embedding model to generate embeddings for the documents.
2. **Vector Storage**: Qdrant Cloud is used to store and retrieve document embeddings.
3. **Query Handling**: When a user enters a query, the application searches for relevant documents using the similarity search feature of Qdrant.
4. **Response Generation**: A prompt is created using the found context and passed to the Groq model to generate a detailed response.

## Example

1. **Start the application**.
2. **Enter a query** in the input box.
3. The application will **search for relevant context** within the Raga.ai documentation.
4. A detailed response will be generated and displayed based on the context found.

## Dependencies

- **Streamlit**: For creating the web application interface.
- **Qdrant-client**: For interacting with the Qdrant vector database.
- **Langchain-cohere**: For generating embeddings using Cohere's models.
- **Langchain-community-vectorstores**: For managing vector stores.
- **Langchain-groq**: For generating responses using Groq's language model.
- **Langchain-core**: For core functionality and utilities.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Qdrant](https://qdrant.tech/)
- [Cohere](https://cohere.ai/)
- [Groq](https://groq.com/)
```
