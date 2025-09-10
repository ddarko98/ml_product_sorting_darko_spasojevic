import joblib
import pandas as pd

# Load the saved model
model = joblib.load("model/product_sorting_by_title.pkl")
 
print("Model loaded successfully!")
print("Type 'exit' at any point to stop.\n")
 
while True:
    title = input("Enter product title: ")
    if title.lower() == "exit":
        print("Exiting...")
        break
 
    
 
    # Create a DataFrame from input
    user_input = pd.DataFrame([{
        "product_title": title
        
    }])
 
    # Predict sentiment
    prediction = model.predict(user_input)[0]
    print(f"Predicted Title: {prediction}\n" + "-" * 40)