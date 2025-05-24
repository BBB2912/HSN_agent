import pandas as pd
from typing import List
from google.adk.agents import Agent

# Load and cache the dataset once for efficiency
def load_hsn_data():
    url = "https://docs.google.com/spreadsheets/d/1UD4JAAQ6Fgeyc5a1OwBiLV2cPTAK_D2q/export?format=csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    return df

hsn_data = load_hsn_data()

def validate_single_hsn(hsn_code: str, df: pd.DataFrame) -> str:
    hsn_code = str(hsn_code).strip()

    # Format Validation
    if not hsn_code.isdigit() or not (2 <= len(hsn_code) <= 8):
        return f"❌ Invalid format: '{hsn_code}'. Must be 2–8 digit number."

    # Existence Validation
    match = df[df["HSNCode"] == hsn_code]
    if match.empty:
        return f"❌ Not Found: HSN code '{hsn_code}' not found."

    # Hierarchical Validation
    hierarchy = []
    for i in [2, 4, 6]:
        if len(hsn_code) > i:
            parent_code = hsn_code[:i]
            parent_match = df[df["HSNCode"] == parent_code]
            if not parent_match.empty:
                hierarchy.append(f"  - {parent_code}: {parent_match.iloc[0]['Description']}")

    desc = match.iloc[0]["Description"]
    response = f"✅ Valid HSN Code: '{hsn_code}'\nDescription: {desc}"
    if hierarchy:
        response += "\nHierarchy:\n" + "\n".join(hierarchy)
    return response

# Tool: Single or multiple HSN input
def validate_hsn_codes(hsn_input: str) -> str:
    try:
        codes = [c.strip() for c in hsn_input.split(",") if c.strip()]
        if not codes:
            return "❌ No valid HSN codes provided."
        results = [validate_single_hsn(code, hsn_data) for code in codes]
        return "\n\n".join(results)
    except Exception as e:
        return f"❌ Unexpected error during validation: {e}"

# Define the ADK Agent
root_agent = Agent(
    name="hsn_validator_agent",
    model="gemini-2.0-flash",
    description="Agent to validate HSN codes and return their descriptions and hierarchy from Google Sheet.",
    instruction=(
        "You are a helpful assistant that validates Indian HSN codes. When a user provides one or more HSN codes, "
        "check each for format, existence in the dataset, and parent hierarchy. Return clear messages accordingly."
    ),
    tools=[validate_hsn_codes],
)
