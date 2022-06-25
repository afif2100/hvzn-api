import falcon
import falcon.testing
import pytest
from helper.health import HealthCheck
from api.sentiment import Sentiment

health = HealthCheck()
sentiment = Sentiment()

test_payload_single = {"text": "tiap ketiduran kesorot lampu selalu mimpi serem"}
text_payload_list = {
    "text": [
        "tiap ketiduran kesorot lampu selalu mimpi serem",
        "Doakan aku dapet kerja secepatnya guys. Aku mau bantu2 biayain adek kuliah, karna skrg biaya kuliah gak ngotak.",
        "Sebagai Siapman tetap harus hati-hati khususnya pas harus tanda tangan dokumen apapun yg riskan. Selama ada atasan, mending atasannya aja.",
    ]
}

endpoint_prefix = "api/v1"


@pytest.fixture
def client():
    # app route
    app = falcon.App()
    app.add_route(f"/{endpoint_prefix}/sentiment", sentiment)

    return falcon.testing.TestClient(app)


def test_sentiment_single(client):
    resp = client.simulate_post(
        "/api/v1/sentiment",
        json=test_payload_single,
    )
    assert isinstance(resp.json["result"], dict)
    assert list(resp.json["result"].keys()) == ["label", "score", "text", "text_clean"]


def test_sentiment_multi(client):
    resp = client.simulate_post(
        "/api/v1/sentiment",
        json=text_payload_list,
    )

    assert isinstance(resp.json["result"], list)
    assert len(resp.json["result"]) == 3
    for _rs in resp.json["result"]:
        assert list(_rs.keys()) == [
            "label",
            "score",
            "text",
            "text_clean",
        ]
