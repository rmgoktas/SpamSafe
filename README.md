# Spam Detection AI Model
AI Model that detects spam SMS or E-Mail's.
## How to test on my machine locally ?

- Clone the repository. Also you can download by ZIP.

- Install dependencies:
```bash
  pip install -r requirements.txt
```
- Run app.py:
```bash
  python app.py OR python3 app.py
```
- Create an API request to your localhost: 
```bash
  curl -X POST -H "Content-Type: application/json" -d '{"text": "This is a test message."}' http://127.0.0.1:5000/predict
```


