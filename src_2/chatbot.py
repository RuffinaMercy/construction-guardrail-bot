from dotenv import load_dotenv
from openai import OpenAI
import os

from src_2.utils.normalizer import normalize_query
from src_2.utils.validator import is_valid_query
from src_2.utils.responder import generate_answer
from src_2.utils.guardrail import check_guardrail   # NEW

load_dotenv()

# Fix SSL issues (if any)
os.environ.pop("SSL_CERT_FILE", None)
os.environ.pop("REQUESTS_CA_BUNDLE", None)


class Chatbot:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

        self.model = "llama-3.3-70b-versatile"

    def ask(self, query: str) -> str:

        # Step 1: Basic validation
        if not is_valid_query(query):
            return "Please enter a valid question."

        # Step 2: Normalize query
        cleaned = normalize_query(query)

        # Debug (optional)
        # print("Original:", query)
        # print("Cleaned:", cleaned)

        # Step 3: Domain validation
        if not is_valid_query(cleaned, domain_check=True):
            return "I only answer construction-related queries."

        # Step 4: Guardrail INPUT check
        try:
            allowed = check_guardrail(cleaned)

            if not allowed:
                return "⚠️ This request violates safety policies."

        except Exception as e:
            return f"Guardrail error: {str(e)}"

        # Step 5: Generate response from Groq
        response = generate_answer(self.client, self.model, cleaned)

        # Step 6: Guardrail OUTPUT check
        try:
            allowed_output = check_guardrail(response)

            if not allowed_output:
                return "⚠️ Response blocked by safety guardrails."

        except Exception:
            pass

        return response