
import openai
import os
from openai.embeddings_utils import cosine_similarity, get_embedding

# get your API key from https://beta.openai.com/account/api-keys
openai.api_key = os.getenv("OPENAI_API_KEY")
# get the model ID from https://beta.openai.com/models
EMBEDDING_MODEL = "text-embedding-ada-002"

positive_review = get_embedding("Positive Feedback")
negative_review = get_embedding("Negative Feedback")

positive_example = get_embedding("""
The silver version I bought is really nice-looking, and it arrived in just one day. 
I started using it at night and found the system to be very smooth and responsive. 
The build quality is solid, and the touch feeling is delicate and exquisite. 
Apple has always provided good quality products.
""")
negative_example = get_embedding("The price drop is significant, but the price protection policy is unreasonable. I do not recommend it.")

def get_score(sample_embedding):
  return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)

positive_score = get_score(positive_example)
negative_score = get_score(negative_example)

print("Positive review rating : %f" % (positive_score))
print("negative review rating : %f" % (negative_score))