# Legal AI Evaluation Calculator - Backend

## Deployment to DigitalOcean App Platform

### Prerequisites
1. DigitalOcean account
2. GitHub repository with the backend code
3. OpenAI API key

### Steps to Deploy

1. **Create a new App in DigitalOcean:**
   - Go to DigitalOcean App Platform
   - Click "Create App"
   - Choose "GitHub" as the source

2. **Configure the App:**
   - Select your repository
   - Choose the branch to deploy
   - Set the following configuration:
     - **Run Command:** `gunicorn app:app`
     - **Build Command:** `pip install -r requirements.txt`
     - **Environment Variables:**
       - `OPENAI_KEY`: Your OpenAI API key
       - `PORT`: 8080

3. **Deploy the App:**
   - Click "Next" and choose your plan
   - Click "Launch App"

4. **Verify Deployment:**
   - Once deployed, visit the provided URL
   - Test the API endpoint: `https://<your-app-url>/api/health`
   - Should return: `{"status": "healthy"}`

### API Endpoints
- POST `/api/evaluate`
  - Request Body:
    ```json
    {
      "tool": "tool-name",
      "firm_size": "small|medium|large",
      "priorities": {
        "performance": 1-10,
        "cost": 1-10,
        "compliance": 1-10,
        "integration": 1-10
      }
    }
    ```
  - Response:
    ```json
    {
      "tool": "tool-name",
      "sub_scores": {
        "performance": 0-10,
        "cost": 0-10,
        "compliance": 0-10,
        "integration": 0-10,
        "user_experience": 0-10
      },
      "overall_score": 0-100,
      "analysis": "AI-generated analysis",
      "metadata": {}
    }
    ```

### Maintenance
- To update the app, push changes to your GitHub repository
- DigitalOcean will automatically rebuild and redeploy
