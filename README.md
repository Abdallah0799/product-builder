# Product Builder for Elite Drip

This project is an extension of the Elit Drip Data Pipelines repository. To facilitate the creation of new products within the Elite Drip database, I developed a Python-based API that leverages OpenAI's capabilities. The API has a single endpoint: create_new_product, which automates the generation of a new product.

The API is deployed on Google Cloud Run, making it accessible and scalable.

You can generate a new product by clicking on this [endpoint](https://product-builder-main-883192161608.us-central1.run.app/get_new_product).

Here is the format of a response:

{
  "category": "Pants",
  "created_at": "Fri, 30 Aug 2024 17:32:57 GMT",
  "gender": "F",
  "title": "Court Queen Performance Joggers",
  "unit_amount": 150,
  "updated_at": "Fri, 30 Aug 2024 17:32:57 GMT"
}
