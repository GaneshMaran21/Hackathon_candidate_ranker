"""Shared constants for JD matching and trap detection."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_JD_PATH = REPO_ROOT / "data" / "job_description.txt"
DEFAULT_ARTIFACTS_DIR = REPO_ROOT / "artifacts"
EMBED_DIM = 384
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CHATGPT_CURIOUS_PHRASE = "Lately I've been curious about how AI tools could augment my work"

CONSULTING_FIRMS = {
    "tcs", "infosys", "wipro", "accenture", "cognizant", "capgemini",
    "hcl", "tech mahindra", "ltimindtree", "mindtree", "mphasis",
}

FICTION_EMPLOYERS = {
    "dunder mifflin", "hooli", "initech", "pied piper", "wayne enterprises",
    "stark industries", "globex inc", "acme corp",
}

PRODUCT_COMPANIES = {
    "swiggy", "zomato", "uber", "google", "meta", "netflix", "adobe",
    "flipkart", "phonepe", "razorpay", "paytm", "dream11", "aganitha",
    "mad street den", "locobuzz", "wysa", "glance", "upgrad", "genpact ai",
}

IR_KEYWORDS = [
    "hybrid retrieval", "bm25", "dense vector", "vector search", "vector recall",
    "learning-to-rank", "learning to rank", "ltr", "ndcg", "mrr", "map",
    "information retrieval", "embedding", "embeddings", "faiss", "pinecone",
    "qdrant", "milvus", "weaviate", "opensearch", "elasticsearch",
    "candidate-jd", "candidate jd", "relevance", "retrieval", "ranking",
    "search product", "recommendation", "recsys", "offline-online",
    "a/b test", "revenue-per-search", "embedding drift", "index refresh",
]

IR_TITLES = [
    "senior ai engineer", "lead ai engineer", "search engineer",
    "recommendation systems engineer", "applied scientist", "nlp engineer",
    "machine learning engineer", "ml engineer", "applied ml engineer",
    "ai engineer", "senior machine learning engineer", "senior nlp engineer",
]

JD_RELEVANT_SKILLS = {
    "python", "embeddings", "embedding", "vector search", "information retrieval",
    "learning to rank", "bm25", "faiss", "pinecone", "qdrant", "milvus",
    "elasticsearch", "opensearch", "sentence-transformers", "sentence transformers",
    "bge", "e5", "lora", "qlora", "fine-tuning llms", "fine tuning llms",
    "nlp", "retrieval", "ranking", "xgboost", "lightgbm", "mlflow",
    "weaviate", "rag", "llm", "evaluation", "ndcg", "mrr",
}

PROFICIENCY_SCORES = {
    "beginner": 0.25,
    "intermediate": 0.5,
    "advanced": 0.75,
    "expert": 1.0,
}

INDIA_LOCATIONS = {
    "india", "pune", "noida", "delhi", "ncr", "gurgaon", "gurugram",
    "hyderabad", "mumbai", "bangalore", "bengaluru", "chennai", "kolkata",
    "indore", "bhubaneswar", "kochi", "coimbatore", "vizag", "jaipur",
}

RECYCLED_BLOCK_MARKERS = [
    "content writing and seo strategy for a tech-focused publication",
    "mechanical engineering design role at a hardware-product company",
    "brand design and creative direction at a consumer-products company",
    "business analyst at a consulting firm, working primarily with retail",
    "customer support team lead at a saas product",
    "enterprise sales of cloud software solutions into the mid-market segment",
]

NON_ML_TITLES = {
    "hr manager", "marketing manager", "content writer", "graphic designer",
    "accountant", "mechanical engineer", "civil engineer", "customer support",
    "sales executive", "operations manager", "project manager", "business analyst",
}

CV_ONLY_KEYWORDS = [
    "computer vision engineer", "speech recognition", "robotics", "image classification",
    "gan", "tts", "speech",
]
