---
title: Image classification 
emoji: 🦆
colorFrom: purple
colorTo: blue
sdk: docker
app_port: 5000
---

# image-classification-deployment

### Running locally 
Build an image and run Docker container.
```bash 
docker build -t image_classification .
docker run -p 8080:5000 image_classification 
```
Image classification app is accessible on host at `http://127.0.0.1:8080/`.

### Deployment
Code is automatically deployed to Hugging Face Spaces, Docker container is build, run and hosted at: 
https://huggingface.co/spaces/paweszetela/image-classification