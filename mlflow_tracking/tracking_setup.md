# MLflow Tracking Setup

This document explains how to set up MLflow tracking for the Personality Prediction ML model.

## MLflow Setup

1. **Install MLflow:**

```bash
pip install mlflow
Start MLflow Tracking Server:

Run the following command in your terminal to start the MLflow UI server:

bash
Copy
Edit
mlflow ui
This will start a local tracking server accessible at:

arduino
Copy
Edit
http://localhost:5000
Using MLflow Tracking:

During model training, MLflow logs parameters, metrics, and models automatically. Once the server is running, open the above URL in your browser to view:

Experiment runs

Logged parameters

Metrics such as accuracy, precision, recall, F1-score

Artifacts (e.g., saved models)

Screenshots:

Below are example screenshots of the MLflow UI to help you navigate:

Experiment Overview:


Run Details:


Model Artifacts:


Note: Replace the placeholder images above with your actual screenshots saved under screenshots/ folder.

End of tracking_setup.md

yaml
Copy
Edit

---

Let me know if you want me to generate example screenshots or if you need help creating those!