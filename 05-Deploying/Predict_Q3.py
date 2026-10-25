import pickle
import sys
 
path = sys.argv[1] if len(sys.argv) > 1 else "pipeline.bin"
 
with open(path, "rb") as f:
    pipeline = pickle.load(f)
 
lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}
 
proba = pipeline.predict_proba([lead])[0, 1]
print(f"conversion probability: {proba:.3f}")