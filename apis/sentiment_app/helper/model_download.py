from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification



if __name__ == "__main__":
    pretrained= "sahri/indonesiasentiment"

    print("downloading model to memmory")
    model = AutoModelForSequenceClassification.from_pretrained(pretrained)
    tokenizer = AutoTokenizer.from_pretrained(pretrained)

    sentiment_analysis = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
    print("Save model to directory")
    sentiment_analysis.save_pretrained("./model/indosentiment")