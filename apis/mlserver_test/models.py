from cgitb import text
import json
import numpy as np
from mlserver import MLModel, types
from mlserver.utils import get_model_uri
import string
import random


class GenerateRandomText(MLModel):

    def _model(self, num:int):

        #generate random long string
        result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))
        result = f"{self.model}+{result}"

        return result

    async def load(self) -> bool:
        # open model
        model_uri = await get_model_uri(self._settings)
        with open(model_uri) as model_file:
            self.model = json.load(model_file)

        self._predictive = self._model

        self.ready = True
        return self.ready

    async def predict(self, payload: types.InferenceRequest) -> types.InferenceResponse:
        
        inputs = self._extract_inputs(payload)
        result = []
        for _inp in inputs['predict']:
            _inp = int(_inp)
            predictions = self._predictive(_inp)
            result.append(predictions)

        return self._decode_ouput(payload, result)

    def _decode_ouput(self, payload, data):
        if isinstance(data,list):
            shape = len(data)
        if isinstance(data, str):
            shape = len([data])
        
        shape = [shape]
        datatype = type(data).__name__
        return types.InferenceResponse(
            id=payload.id,
            model_name=self.name,
            model_version=self.version,
            outputs=[
                types.ResponseOutput(
                    name= "prediction_result",
                    shape= shape,
                    datatype= datatype,
                    data= data,
                )
            ],
        )


    def _extract_inputs(self, payload: types.InferenceRequest):
        inputs = {}
        for inp in payload.inputs:
            inputs[inp.name] = np.array(inp.data)

        print("## Input:")
        print(inputs)
        return inputs

