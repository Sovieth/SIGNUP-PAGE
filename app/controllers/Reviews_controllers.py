from flask import request, redirect, url_for, render_template, flash
from ..models.Reviews_model import reviews

    
def review():
    if request.method == 'POST':
        # Get the review data from the request
        name = request.form['name']
        review_text = request.form['review_text']
        rating = request.form['rating']
        
        
        review_data = {
            'name': name,
            'review_text': review_text,
            'rating': int(rating)
        }
        reviews.review(review_data)
        return redirect(url_for('review_bp.review_display'))
    # Render the review template on GET request
    return render_template('review.html')

def review_display():
    review = reviews.display_review()
    return render_template('review.html', display=review)