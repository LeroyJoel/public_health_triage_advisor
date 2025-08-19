"""
Custom tools for the CrewAI agent project
"""

import pandas as pd
import requests
from typing import List, Dict, Any, Optional
from crewai import Tool


def csv_lookup(path: str, query: str, max_rows: int = 10) -> List[Dict[str, Any]]:
    """
    Look up data in a CSV file based on a query.
    
    Args:
        path: Path to the CSV file
        query: Search query to match against any column
        max_rows: Maximum number of rows to return
        
    Returns:
        List of matching records as dictionaries
    """
    try:
        df = pd.read_csv(path)
        matches = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        return matches.head(max_rows).to_dict(orient="records")
    except Exception as e:
        return [{"error": f"Failed to read CSV file: {str(e)}"}]


def web_fetch(url: str, timeout: int = 10) -> str:
    """
    Fetch content from a web URL.
    
    Args:
        url: URL to fetch content from
        timeout: Request timeout in seconds
        
    Returns:
        Content from the URL as string
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching URL: {str(e)}"


# Create CrewAI Tool objects
csv_lookup_tool = Tool(
    name="csv_lookup",
    description="Look up data in a CSV file based on a search query",
    func=csv_lookup
)

web_fetch_tool = Tool(
    name="web_fetch", 
    description="Fetch content from a web URL",
    func=web_fetch
)
