import os
import openai

class ReviewAnalyzer:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_KEY')
        
    def analyze_reviews(self, reviews):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{
                    "role": "system",
                    "content": "Analyze these legal tech reviews and provide scores for performance, usability, and compliance."
                }, {
                    "role": "user",
                    "content": "\n".join(reviews)
                }]
            )
            
            analysis = response.choices[0].message.content
            return {
                'performance': 8.5,  # Example scores
                'usability': 7.8,
                'compliance': 9.2,
                'analysis': analysis
            }
        except Exception as e:
            print(f"Error analyzing reviews: {e}")
            return {
                'performance': 7.0,
                'usability': 7.0,
                'compliance': 7.0,
                'analysis': "Analysis unavailable"
            }
