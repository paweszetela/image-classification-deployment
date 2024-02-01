---
sdk: docker
app_port: 5000
---

# Image Classification Demo
**current state:** This is work in progress, a temporary torchvision model is used for basic image classification functionality.
## Overview
Flask-based demo app for image classification with pytorch models. It features REST API for image uploads and class label predictions, and utilizes Docker for consistent deployment and runtime environment. The app is hosted on Hugging Face Spaces:

[![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-md-dark.svg)](https://huggingface.co/spaces/paweszetela/image-classification)

## CI/CD and Deployment

### GitHub Actions
- Automated synchronization of code changes to Hugging Face Spaces upon updates to the main branch.

### Hugging Face Spaces
- Utilizes Docker for containerized deployment, ensuring automated builds and runs on Hugging Face Spaces.

## Accessibility
- App is hosted on HF Spaces, publicly accessible and includes a basic UI for image uploads and displaying predictions.

## Running locally 
Build an image and run Docker container.
```bash 
docker build -t image_classification .
docker run -p 5000:5000 image_classification 
```
Image classification app is accessible on host at `http://127.0.0.1:5000/`.