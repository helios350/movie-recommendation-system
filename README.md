# 🎬 Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/helios350/movie-recommendation-system?style=social)](https://github.com/helios350/movie-recommendation-system/stargazers)

---

An end-to-end, machine-learning-based movie recommendation engine built with **Python**, **Scikit-Learn**, and **Streamlit**. 

This application uses Natural Language Processing (NLP) to recommend movies based on user selections and dynamically fetches real-time, high-quality movie posters using the TMDB API.

---

## 🚀 Features

- **Advanced NLP:** Utilizes TF-IDF Vectorization for highly accurate, context-aware content filtering.
- **Dynamic API Integration:** Fetches real-time movie posters and data via the TMDB API.
- **Highly Optimized Architecture:** Uses Sparse Matrices to reduce deployment memory footprint by 99% (from 183 MB down to 1.7 MB).
- **Compute On-The-Fly:** Calculates Cosine Similarity in real-time to save RAM and ensure instant app load times.
- **Fault Tolerant:** Gracefully handles missing API data with fallback placeholder images.
- **Blazing Fast:** Implements Streamlit caching (`@st.cache_data`) to prevent redundant network calls.

---

## 🛠️ Installation

Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/helios350/movie-recommendation-system.git](https://github.com/helios350/movie-recommendation-system.git)
cd movie-recommendation-system
pip install -r requirements.txt
```
**Set up your TMDB API Key:** To run this project, you need a free API key from [TMDB](https://www.themoviedb.org/).

1.  Create a `.streamlit` folder in the root directory.
    
2.  Inside it, create a `secrets.toml` file and add your key:

```toml
TMDB_API_KEY = "your_api_key_here"
```

---

## ▶️ Usage

Run the app locally with:

```bash
streamlit run app.py
```

---

## 📦 Deployment

You can easily deploy this project on [Streamlit Cloud↗](https://streamlit.io/cloud):

1.  Push this repo to GitHub (Make sure your `.gitignore` includes `.streamlit/`).
    
2.  Go to Streamlit Cloud → Create new app.
    
3.  Connect your repo and set `app.py` as the entry file.
    
4.  **Important:** Go to your Streamlit app's Advanced Settings and paste your API key into the **Secrets** section just like your local `.toml` file.
    
5.  Deploy! 🚀

---

## 📂 Project Structure

```bash
movie-recommendation-system/
│── .streamlit/             # Local secrets (Ignored by Git)
│   └── secrets.toml        # TMDB API Key storage
│── app.py                  # Main Streamlit application
│── movies_dict.pkl         # Serialized movie dictionary
│── vectors.pkl             # Compressed Sparse Matrix (TF-IDF features)
│── requirements.txt        # Python dependencies
│── .gitignore              # Ignored files and folders
│── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📜 License

This project is licensed under the **MIT License**.
