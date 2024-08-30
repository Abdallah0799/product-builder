import random
import datetime
from connectors.s3 import S3Connector
from connectors.chatgpt import ChatGPTConnector

# Set product features
genders = {"men": "M", "women": "F"}
categories = ["T-shirt", "Pants"]

# Define the response format we want for chatgpt response
response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "new_prodcut",
        "schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "unit_amount": {"type": "number"},
            },
            "required": ["title", "unit_amount"],
            "additionalProperties": False,
        },
    },
}


def run() -> dict:

    # Init external connections
    chatgptconn = ChatGPTConnector()
    s3conn = S3Connector("fictive-company")

    # Get exsiting products
    products = s3conn.fetch_data("products", 360)
    existing_products = ", ".join(list(products["title"].values))

    # Randomly choose if we want to generate a product for M or F
    # and a T-Shirt or a Pants
    gender = random.choice(list(genders.keys()))
    category = random.choice(categories)

    # Define the system instructions to create a new product
    system_informations = f"""
    Here’s a refined version of the prompt:

    Role: You are a product developer for Elite Drip, a clothing company with a
    brand deeply rooted in the basketball community. Unlike traditional clothing
    brands, Elite Drip has cultivated a unique space that specifically caters to
    professional basketball players and enthusiasts. The company primarily offers
    high-quality t-shirts and pants.

    Objective: Your task is to conceptualize a new {category} product for {gender}.
    The product should align with the brand's basketball-centric identity and
    resonate with the community of professional players. The new product should
    include:

    A compelling title that reflects both the style and inspiration behind the
    design.
    A unit price that falls within the range of $90 to $200.

    Examples of Product Titles: {existing_products}

    Requirement: Generate a distinctive {category} for {gender} that embodies the
    brand’s essence.
    """

    # API call
    res = chatgptconn.chat_create_json(
        model="gpt-4o-mini",
        system_instructions=system_informations,
        response_format=response_format,
    )

    # Enriching the response with additional fields
    now = datetime.datetime.now()
    additional_fields = {
        "created_at": now,
        "updated_at": now,
        "gender": genders[gender],
        "category": category
    }
    final_res = {**eval(res), **additional_fields}

    return final_res
