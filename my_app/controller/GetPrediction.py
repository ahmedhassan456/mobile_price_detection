def GetPrediction(model, inputs):

    result = {
        0: "low cost",
        1: "medium cost",
        2: "high cost",
        3: "very high cost"
    }

    prediction = model.predict([inputs])[0]

    return result[prediction]