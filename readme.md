# Personality Prediction ML Application

This repository contains an end-to-end machine learning application to predict personality type (Introvert or Extrovert) based on behavioral features. The project includes model training, an API backend, and a frontend interface.

## Project Structure

ml_app_assignment/
├── ml/
│ ├── training.ipynb # Jupyter notebook for training and logging model with MLflow
│ └── model.pkl # Saved ML model
├── backend/
│ └── main.py # FastAPI backend with prediction endpoint
├── frontend/
│ └── streamlit_app.py # Streamlit frontend app
├── mlflow_tracking/
│ └── tracking_setup.md # MLflow setup instructions
├── requirements.txt # Required Python packages
└── README.md # Project overview and instructions



## Technologies Used

- Model Training: Jupyter/Colab, scikit-learn
- Backend API: FastAPI
- Frontend: Streamlit
- Experiment Tracking: MLflow
- Deployment (optional): Docker, Azure, AWS

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ml_app_assignment
2. Install dependencies

pip install -r requirements.txt
3. Run the FastAPI backend

uvicorn backend.main:app --reload
Visit http://localhost:8000/docs to see the Swagger UI and test the /predict endpoint.

4. Run the frontend app

streamlit run frontend/streamlit_app.py