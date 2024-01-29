# image-classification-deployment

Build an image and run Docker container.
```bash 
docker build -t image_classification .
docker run -p 8080:5000 image_classification 
```

Image classification app is accessible on host at `http://127.0.0.1:8080/`.