from legal_scrapers.vendor_scraper import VendorScraper
from ai_agent.review_analyzer import ReviewAnalyzer

class DataProcessor:
    def __init__(self, tool_name):
        self.tool_name = tool_name
        self.vendor_scraper = VendorScraper(tool_name)
        self.review_analyzer = ReviewAnalyzer()

    def collect_data(self):
        data = {}
        
        # Vendor data
        vendor_data = self.vendor_scraper.get_pricing()
        data.update(vendor_data)
        
        # Reviews (example data)
        reviews = [
            "Great tool for contract review",
            "Excellent compliance features",
            "Could improve user interface"
        ]
        review_analysis = self.review_analyzer.analyze_reviews(reviews)
        data.update(review_analysis)
        
        return data
