from surprise import Dataset
from surprise import Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

# Load dataset
data = Dataset.load_builtin('ml-100k')  # MovieLens 100K

# Split into train/test
trainset, testset = train_test_split(data, test_size=0.25)

 
### 📁 Step 3: Train Collaborative Filtering Model (SVD)
# Train model using Singular Value Decomposition (SVD)
model = SVD()
model.fit(trainset)

# Test predictions
predictions = model.test(testset)

# Accuracy
print("RMSE:", accuracy.rmse(predictions))


### 📁 Step 4: Make Recommendations for a pi
from collections import defaultdict

# Get top-N recommendations for each user
def get_top_n(predictions, n=5):
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    
    # Sort predictions for each user and get top N
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    
    return top_n

top_n = get_top_n(predictions, n=5)

# Print top 5 movie IDs for a sample user
for uid, user_ratings in list(top_n.items())[:1]:
    print(f"\nTop 5 recommendations for User {uid}:")
    for iid, rating in user_ratings:
        print(f"Movie ID: {iid} | Predicted Rating: {rating:.2f}")

