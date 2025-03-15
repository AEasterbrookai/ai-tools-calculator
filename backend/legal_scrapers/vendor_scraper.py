import requests
from bs4 import BeautifulSoup

class VendorScraper:
    def __init__(self, tool_name):
        self.tool_name = tool_name
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'LegalAI-Evaluator/1.0'
        })

    def get_pricing(self):
        try:
            # Example scraping logic - would need to be adapted for actual vendor sites
            url = f"https://{self.tool_name}.com/pricing"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract pricing information
            price_tag = soup.find('span', class_='price')
            price = float(price_tag.text.replace('$', '')) if price_tag else None
            
            # Extract features
            features = [f.text.strip() for f in soup.select('.feature-item')]
            
            return {
                'price': price,
                'features': features
            }
        except Exception as e:
            print(f"Error scraping vendor data: {e}")
            return {
                'price': None,
                'features': []
            }
