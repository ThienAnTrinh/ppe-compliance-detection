FROM python:3.10-slim
ADD . /app
WORKDIR /app
# RUN wget https://files.pythonhosted.org/packages/8c/4d/17e07377c9c3d1a0c4eb3fde1c7c16b5a0ce6133ddbabc08ceef6b7f2645/torch-2.0.1-cp310-cp310-manylinux1_x86_64.whl
# RUN pip3 install --no-cache-dir torch-2.0.1-cp310-cp310-manylinux1_x86_64.whl
RUN pip install --no-cache-dir -r requirements1.txt
ENTRYPOINT ["python"]
CMD ["app.py"]