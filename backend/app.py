from flask import Flask, request, jsonify
from flask_cors import CORS
from data_pipeline import DataProcessor
from scoring_engine.scoring import calculate_overall_score
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    tool_name = data.get('tool')
    firm_size = data.get('firm_size')
    priorities = data.get('priorities', {})

    processor = DataProcessor(tool_name)
    collected_data = processor.collect_data()

    sub_scores = {
        'performance': collected_data.get('performance', 7.0),
        'cost': 8.0 if collected_data.get('price', 0) < 1000 else 6.0,
        'compliance': collected_data.get('compliance', 7.0),
        'integration': 7.5,
        'user_experience': collected_data.get('usability', 7.0)
    }

    weights = {
        'performance': priorities.get('performance', 5),
        'cost': priorities.get('cost', 5),
        'compliance': priorities.get('compliance', 5),
        'integration': priorities.get('integration', 5)
    }

    overall_score = calculate_overall_score(sub_scores, weights)

    response = {
        'tool': tool_name,
        'sub_scores': sub_scores,
        'overall_score': overall_score,
        'analysis': collected_data.get('analysis', ''),
        'metadata': collected_data
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
