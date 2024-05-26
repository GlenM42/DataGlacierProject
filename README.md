# Iris Classifier Deployment

This repository contains a simple data science project to train a model on the Iris dataset and deploy it using Flask. The project includes the following steps:

1. Loading and training a RandomForestClassifier on the Iris dataset.
2. Saving the trained model.
3. Deploying the model using a Flask web application.
4. Creating a PDF document summarizing the deployment steps.

## Project Structure

- `app.py`: Flask application to serve the model and handle prediction requests.
- `iris_model.joblib`: Serialized RandomForestClassifier model.
- `deployment_steps.pdf`: PDF document detailing the deployment steps.
- `requirements.txt`: List of Python packages required to run the project.

## Usage

### Predicting Iris Species

To make a prediction, send a POST request to the `/predict` endpoint with a JSON payload containing the features of an Iris flower. 

Example request using `curl`:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}' http://127.0.0.1:5000/predict
```

The response will be a JSON object containing the predicted class of the Iris flower.

### Example Response

```json
{
  "prediction": 0
}
```

## PDF Document

The `deployment_steps.pdf` document contains snapshots and descriptions of each step involved in deploying the model using Flask. It includes:

- Loading and training the model.
- Saving the model.
- Creating the Flask application.
- Instructions for running and testing the Flask application.

## Usage

`curl -X POST -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}' http://127.0.0.1:5000/predict`
