from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat
import pandas as pd

from app.identity_match import identity_score
from app.logger import log_query

app = FastAPI()


# Request Schema
class QueryRequest(BaseModel):
    query: str
    email: str = ""


# Load Mock Database
mock_db = pd.read_csv("data/mocked_data.csv")


# API Endpoint
@app.post("/query")
def process_query(data: QueryRequest):

    user_query = data.query
    query_lower = user_query.lower()

    # Simple Intent Classification
    if "royalty" in query_lower:
        intent = "royalty_query"

    elif "live" in query_lower:
        intent = "book_live_status"

    elif "author copy" in query_lower:
        intent = "author_copy"

    elif "package" in query_lower or "add-on" in query_lower:
        intent = "add_on_status"

    elif "dashboard" in query_lower or "login" in query_lower:
        intent = "dashboard_access"

    else:
        intent = "general_query"

    # Confidence Logic
    if intent == "general_query":
        confidence = 50
    else:
        confidence = 92

    # Find User Record
    user_record = None

    if data.email:

        filtered = mock_db[
            mock_db["email"] == data.email
        ]

        if len(filtered) > 0:
            user_record = filtered.iloc[0]

    # Human Escalation
    if confidence < 80:

        final_response = (
            "Low confidence detected. "
            "Query escalated to human support."
        )

        log_query(
            user_query,
            final_response,
            confidence,
            True
        )

        return {
            "response": final_response,
            "confidence": confidence,
            "escalated": True
        }

    # -----------------------------
    # Intent Responses
    # -----------------------------
    if intent == "book_live_status":

        if user_record is not None:

            final_response = (
                f"Your book "
                f"'{user_record['book_title']}' "
                f"will go live on "
                f"{user_record['book_live_date']}"
            )

        else:
            final_response = "User record not found"

    elif intent == "royalty_query":

        if user_record is not None:

            final_response = (
                f"Your royalty status is "
                f"{user_record['royalty_status']}"
            )

        else:
            final_response = "User record not found"

    elif intent == "author_copy":

        if user_record is not None:

            final_response = (
                f"Author copy status: "
                f"{user_record['author_copy_status']}"
            )

        else:
            final_response = "User record not found"

    elif intent == "add_on_status":

        if user_record is not None:

            final_response = (
                f"Your active add-ons are: "
                f"{user_record['add_on_services']}"
            )

        else:
            final_response = "User record not found"

    elif intent == "dashboard_access":

        final_response = (
            "Please use the dashboard login page "
            "or contact support if login issues continue."
        )

    else:

        # -----------------------------
        # Optional Ollama Response
        # -----------------------------
        try:

            ollama_response = chat(
                model="llama3",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a publishing "
                            "support assistant."
                        )
                    },
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
            )

            final_response = (
                ollama_response["message"]["content"]
            )

        except Exception:

            final_response = (
                "Your query requires "
                "knowledge base lookup."
            )

    # -----------------------------
    # Log Query
    # -----------------------------
    log_query(
        user_query,
        final_response,
        confidence,
        False
    )

    # -----------------------------
    # Final API Response
    # -----------------------------
    return {
        "response": final_response,
        "confidence": confidence,
        "escalated": False
    }