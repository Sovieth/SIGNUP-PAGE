from ..import mongo

class reviews:
    
    def review(review_data):   
        return mongo.db.reviews.insert_one(review_data)
    
    def display_review():   
        return mongo.db.reviews.find()
    
    