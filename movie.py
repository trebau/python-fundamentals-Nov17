#date_reviewed = datetime.date(2025, 11, 20)

from datetime import date

class MovieReview:

    def __init__(self, movie_title, reviewer_name, score, date_reviewed, *args, **kargs):
        print("Generating Review")
        self.title = movie_title
        self.name = reviewer_name
        self.score = score
        self.date = date_reviewed
        

    def pretty_print(self):
        return f"{self.title} review by {self.name} on {self.date}: {self.score}/5 stars"
    
    def increase_score(self):
        if self.score < 5:
            self.score += 1
        else:
            raise ValueError("score cannot exceed 5")
        return self.score
    
    def update_review(self, new_score, new_reviewer=None):
        self.score = new_score
        self.date = date.today()
        if new_reviewer:
            self.name = new_reviewer


    @classmethod
    def review_bomb(cls, movie_title, num_reviews):
        new_list = []
        for num in range(num_reviews):
            new_review = cls(movie_title = movie_title, reviewer_name = "Statler & Waldorf", score=1, date_reviewed = date.today())
            new_list.append(new_review)

        return new_list

        

