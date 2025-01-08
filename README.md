# Synthetic Data Generator

This project provides a Streamlit-based web application for generating synthetic data based on user-provided schemas and hints. It leverages the power of Google's Gemini large language model (LLM) to create realistic and diverse synthetic data for various testing and development purposes.

## Features

*   **User-Friendly Interface:** A simple and intuitive Streamlit web interface guides users through the data generation process.
*   **Schema-Driven Generation:** Generates data that conforms to user-defined schemas, either tabular (CSV) or JSON.
*   **Flexible Schema Input:**
    *   Upload a structured CSV file to define tabular schemas.
    *   Upload a text file containing a JSON schema for generating JSON data.
*   **Hints and Constraints:** Allows users to provide hints at the column/field level (in the CSV) and additional hints through a text box to guide the data generation process.
*   **Multiple Output Formats:** Supports generating data in CSV, Parquet, or JSON formats.
*   **LLM Backend:** Uses Google's Gemini large language model for intelligent data generation.
*   **Data Preview:** Displays a sample of the generated data before saving.
*   **Error Handling:** Includes basic error handling for invalid schemas, API errors, and parsing issues.

## Project Structure
synthetic_llm/
├── app.py               # Streamlit application
├── synthetic_data/
│   ├── init.py
│   ├── generator.py       # Core data generation logic
│   ├── input_parser.py    # Schema and hints parsing
│   ├── llm_client.py      # Interaction with the LLM (Gemini)
│   ├── output_processor.py # Data parsing, validation, post-processing
│   └── output_writer.py   # Writing data to files (currently not used)
└── requirements.txt      # Project dependencies

## Getting Started

### Prerequisites

1.  **Python 3.8+:** Make sure you have Python 3.8 or a newer version installed.
2.  **Virtual Environment (Recommended):** Create and activate a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Google AI Gemini API Key:**
    *   Obtain an API key from Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
    *   Set the API key as an environment variable named `GOOGLE_API_KEY`:

        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"
        ```

        Or, for a more permanent solution, add the `export` line to your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`).

### Running the Application

1.  **Navigate to the project directory:**

    ```bash
    cd synthetic_data_gen
    ```

2.  **Run Streamlit:**

    ```bash
    streamlit run app.py
    ```

    This will open the app in your default web browser.

## Usage

1.  **Schema Input:**
    *   **Schema Type:** Select "tabular" or "json" from the dropdown.
    *   **Upload Schema:** Click "Browse files" and upload a CSV file for a tabular schema or a TXT file for a JSON schema. The parsed schema and hints (if any) will be displayed.
2.  **Additional Hints:** Enter any extra hints or instructions in the "Additional Hints" text area (one per line).
3.  **Other Parameters:**
    *   **Number of Rows/Objects:** Specify the number of rows (for tabular) or JSON objects to generate.
    *   **Output Format:** Select the desired output format (CSV, Parquet, or JSON).
4.  **Generate Data:** Click the "Generate Data" button.
5.  **View Sample:** A sample of the generated data will be displayed directly in the app.

## Example Input Files

### Tabular Schema (CSV)

Create a CSV file (e.g., `tabular_schema.csv`) with the following columns:

*   **`name`:** The name of the column.
*   **`data_type`:** The data type of the column (e.g., `INT`, `VARCHAR`, `DATE`, `DECIMAL`, `BOOLEAN`).
*   **`constraints`:** Any constraints for the column (e.g., `PRIMARY KEY`, `NOT NULL`, `UNIQUE`).
*   **`hint`:** Optional hints for the column (e.g., "Normally distributed between 18 and 65").

**Example `tabular_schema.csv`:**

```csv
name,data_type,constraints,hint
customer_id,INT,"PRIMARY KEY, NOT NULL","Unique identifier for each customer"
first_name,VARCHAR,NOT NULL,
last_name,VARCHAR,NOT NULL,
age,INT,"",Normally distributed between 18 and 80, with an average of 35.
city,VARCHAR,"",Choose from a list of major US cities.
registration_date,DATE,"",Between January 1, 2020, and today. Format: YYYY-MM-DD.

JSON Schema (TXT)
Create a text file (e.g., json_schema.txt) with a valid JSON schema.

Example json_schema.txt:

{
  "<span class="math-inline">schema"\: "\[http\://json\-schema\.org/draft\-07/schema\#\]\(http\://json\-schema\.org/draft\-07/schema\#\)",
"title"\: "User Profile",
"description"\: "Schema for a user profile in a social media application",
"type"\: "object",
"properties"\: \{
"user\_id"\: \{
"type"\: "integer",
"description"\: "Unique identifier for the user",
"minimum"\: 10000
\},
"username"\: \{
"type"\: "string",
"description"\: "User's chosen username",
"minLength"\: 3,
"maxLength"\: 20,
"pattern"\: "^\[a\-zA\-Z0\-9\_\]\+</span>"
    }
  },
  "required": [
    "user_id",
    "username"
  ]
}

Important Notes
API Key: Ensure that your Google AI Gemini API key is correctly set as the GOOGLE_API_KEY environment variable.
Prompt Engineering: The quality of the generated data heavily depends on the clarity and completeness of your schema, hints, and additional instructions. Experiment with different prompts to achieve the desired results.
Error Handling: The app includes basic error handling, but you might want to enhance it further for production use.
Modular Design: The code is structured into modules for better organization and maintainability. You can easily extend it to support other LLMs, input methods, or output formats.
Contributing
Contributions to this project are welcome! If you have any suggestions, bug fixes, or feature requests, please feel free to open an issue or submit a pull request 1  on the project's repository (if you choose to create one).