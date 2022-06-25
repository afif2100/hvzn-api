import os
import falcon
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from simager.preprocess import TextPreprocess
from helper.base_logger import BaseLogger

logger = BaseLogger(__name__)
os.environ["MODEL_LOCATION"] = "./model/indosentiment"


class Sentiment(object):
    def __init__(self) -> None:
        self.pretrained = os.environ.get("MODEL_LOCATION", "sahri/indonesiasentiment")
        self.model = self._load_model()

    def _load_model(self):
        model = AutoModelForSequenceClassification.from_pretrained(self.pretrained)
        tokenizer = AutoTokenizer.from_pretrained(self.pretrained)
        return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    def _preprocess(self, text):
        methods = [
            "rm_hastag",
            "rm_mention",
            "rm_nonascii",
            "rm_emoticons",
            "rm_html",
            "rm_url",
            "sparate_str_numb",
            "pad_punct",
            "rm_punct",
            "rm_repeat_char",
            "rm_repeat_word",
            "rm_numb",
            "rm_whitespace",
            "normalize",
            "stopwords",
        ]
        cleaner = TextPreprocess(methods=methods)
        if isinstance(text, list):
            _data = []
            for txt in text:
                _data.append(cleaner(txt))
        else:
            _data = cleaner(text)
        return _data

    def predict(self, text):
        result = self.model(text)
        return result

    def on_post(self, req, resp):
        input_payload = req.get_media()
        text = input_payload.get("text", None)

        # Text cleaning
        _clean_text = self._preprocess(text)

        # if text are list predict list and return list
        if isinstance(_clean_text, list):
            result = self.predict(_clean_text)
            for _txt, _ctxt, _res in zip(text, _clean_text, result):
                _res["text"] = _txt
                _res["text_clean"] = _ctxt

        # if text are string predict single and return single
        else:
            result = self.predict(_clean_text)[0]
            result.update({"text": text, "text_clean": _clean_text})

        payload = {"result": result}
        resp.status = falcon.HTTP_200
        resp.media = payload
