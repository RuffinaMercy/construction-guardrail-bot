def generate_answer(client, model, query):
    try:
        response = client.chat.completions.create(
            model=model,
            temperature=0.3,
            max_tokens=300,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a construction expert assistant. "
                        "Only answer construction-related queries. "
                        "If the query is unrelated, say: 'This is outside my domain.' "
                        "Give clear, practical, and concise answers."
                    ),
                },
                {"role": "user", "content": query},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"