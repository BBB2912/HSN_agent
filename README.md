# HSN Code Validation Agent

An AI-powered agent built with Google ADK to validate Indian HSN (Harmonized System of Nomenclature) codes and provide their descriptions.

## Features

- Validates HSN codes against a reference database
- Provides detailed descriptions for valid codes
- Shows hierarchical breakdown of HSN codes
- Supports both single and multiple code validation

## Prerequisites

- Python 3.12 or higher
- Git
- Google API key

## Note:-
 
- run the vs code as administrator

## Installation

1. Clone the repository:
```sh
git clone https://github.com/BBB2912/HSN_agent.git
cd HSN_agent
```

2. Install dependencies:
```sh
pip install -r requirements.txt
```

3. Configure environment:
   - Navigate to `HSN_agent` directory 
   - Create or update `.env` file with your Google API key:
```sh
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

## Usage

### Web Interface
Run the agent in web interface mode:
```sh
adk web
```
Then open the provided URL in your browser (typically http://localhost:8080)

### Terminal Interface
Run the agent in terminal mode:
```sh
adk run HSN_agent
```

## Input Format
- Single HSN code: Enter a 2-8 digit code
- Multiple codes: Enter comma-separated codes

## Example
```
Enter HSN code: 8471
✅ Valid HSN Code: '8471'
Description: Automatic data processing machines and units thereof
Hierarchy:
  - 84: Nuclear reactors, boilers, machinery and mechanical appliances; parts thereof
```

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files.