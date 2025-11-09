from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import subprocess
import joblib

app = FastAPI()
model = joblib.load("ddos_detector.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_features():
    cmd = [
    "tshark", "-i", "9", "-a", "duration:2",
    "-f", "tcp port 5173",
    "-T", "fields", "-e", "ip.src", "-e", "frame.len",
    "-E", "separator=,", "-E", "quote=d"
    ]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode("utf-8").strip().split("\n")
        print("\n📡 Tshark Raw Output:")
        for line in output:
            print("→", line)

        rows = [line.replace('"', '').split(",") for line in output if "," in line]
        print(f"\n📊 Parsed Rows: {len(rows)}")
        for r in rows[:5]:
            print("Row:", r)

        df = pd.DataFrame(rows, columns=["Source IP", "Length"])
        df["Length"] = pd.to_numeric(df["Length"], errors="coerce")
        df.dropna(inplace=True)

        features = {
            "Source IP count": df["Source IP"].nunique(),
            "Total Packets": len(df),
            "Total Bytes": df["Length"].sum(),
            "Avg packet Size": df["Length"].mean()
        }

        print("\n🧪 Extracted Features:")
        for k, v in features.items():
            print(f"{k}: {v}")

        return features

    except Exception as e:
        print("❌ Error during tshark capture:", e)
        return {
            "Source IP count": 0,
            "Total Packets": 0,
            "Total Bytes": 0,
            "Avg packet Size": 0.0
        }
    
@app.get("/predict")
def predict():
    print("\n🚀 Starting Prediction Request")
    features = extract_features()
    X = pd.DataFrame([features])
    print("\n📦 DataFrame for Model:")
    print(X)

    prediction = model.predict(X)[0]
    print("\n🎯 Model Prediction:", prediction)
    return {"prediction": int(prediction)}