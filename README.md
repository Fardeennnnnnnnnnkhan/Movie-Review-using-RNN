
# 🎬 Movie Review Sentiment Analysis (IMDB)

A **Deep Learning NLP project** that classifies movie reviews as **Positive** or **Negative** using a **SimpleRNN model** trained on the IMDB dataset and deployed with **Streamlit**.

---

## 📌 Project Overview

This project demonstrates an end-to-end **Natural Language Processing (NLP)** pipeline:
- Text preprocessing
- Word embeddings
- Recurrent Neural Network (SimpleRNN)
- Model deployment using Streamlit

Users can input any movie review, and the model predicts:
- **Sentiment** (Positive / Negative)
- **Confidence Score (%)**

---

## 🚀 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **NumPy**
- **Streamlit**
- **IMDB Movie Review Dataset**

---

## 🧠 Model Architecture

- Embedding Layer (128 dimensions)
- SimpleRNN (64 units, ReLU activation)
- Dense Layer (Sigmoid activation)

Loss Function:
- Binary Crossentropy

Optimizer:
- Adam

---

## 📂 Project Structure

```
Movie-Review-Sentiment-Analysis/
│
├── simplernn_imdb_model.h5      # Trained model
├── app.py                       # Streamlit application
├── README.md                    # Project documentation
└── requirements.txt             # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/movie-review-sentiment-analysis.git
cd movie-review-sentiment-analysis
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:
```
http://localhost:8501
```

---

## ✍️ Example Reviews to Test

**Positive Review**
```
This movie was absolutely amazing. The performances were outstanding and the story was very engaging.
```

**Negative Review**
```
This was a terrible movie with poor acting and a boring storyline.
```

---

## 📊 Output Example

- **Sentiment:** Positive  
- **Prediction Score:** 81.1 %

---

## 🎯 Key Learning Outcomes

- Text preprocessing for NLP
- Working with word embeddings
- Understanding RNN-based sequence models
- Handling TensorFlow–Keras version compatibility
- Deploying ML models using Streamlit

---

## 📈 Future Improvements

- Replace SimpleRNN with **LSTM / GRU**
- Improve accuracy with better preprocessing
- Add word cloud visualization
- Deploy on **Streamlit Cloud / Hugging Face Spaces**

---

## 👨‍💻 Author

**Fardeen Khan**  
Aspiring Machine Learning and Data Scientist & Full Stack Developer

---

## ⭐ Acknowledgements

- IMDB Dataset
- TensorFlow & Keras Documentation
- Streamlit Community

---

⭐ If you like this project, give it a star on GitHub!

## Access Project at :
[https://movie-review-using-rnn-by-fardeen.streamlit.app/]
