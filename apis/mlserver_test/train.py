import json

model_name = "dummy-model.json"
payload = "hvzn-1"

if __name__=="__main__":

    with open(model_name,'w') as f:
        json.dump(payload, f)