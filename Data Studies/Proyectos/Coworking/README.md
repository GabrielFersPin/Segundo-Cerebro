# Coworking Space Explorer & AI Analyzer

[Webpage](https://coworking.streamlit.app/)

A Streamlit web app to discover, compare, and analyze coworking spaces using advanced filtering, clustering, and AI-powered scoring.

## 🚀 Features

- **Filter & Search:**  
  Find coworking spaces by city, price range, and must-have amenities.

- **Amenity Extraction:**  
  Parses amenities from both structured lists and free-text descriptions, removing duplicates and irrelevant items (like WiFi).

- **Price Normalization:**  
  Normalizes prices within each country or city to enable fair comparisons across different currencies and markets.

- **Recommendation System:**  
  Suggests similar coworking spaces based on amenity and price similarity using cosine similarity.

- **Workspace Clustering:**  
  Groups spaces into categories (e.g., Budget-Friendly, Premium, Creative Studios) using KMeans clustering for style-based exploration.

- **Top Rated Spaces:**  
  Displays and maps the best-rated coworking spaces by city, including price and rating metrics.

- **AI Scoring:**  
  - Trains a RandomForestRegressor on a synthetic quality score (combining amenities, price, and random noise for realism).
  - Predicts a quality score (1–5) for each space.
  - Provides a color-coded, emoji-enhanced score display.
  - Offers detailed breakdowns: price analysis (relative to local market), amenities analysis, competitive ranking, and percentile.
  - Generates actionable recommendations for improvement.

- **Live Model Training:**  
  Retrain and reload the AI model at any time with a button in the AI tab, using the latest data.

- **Explainability:**  
  The app provides transparent, user-friendly explanations and recommendations for each space.

## 🏗️ How It Works

1. **Data Loading:**  
   Loads coworking and amenities data from CSV files in `/src/results/`.

2. **Data Processing:**  
   - Cleans and merges datasets.
   - Extracts and enhances amenities.
   - Normalizes prices and encodes categorical variables.

3. **User Interaction:**  
   - Users filter and select spaces in the sidebar and main tabs.
   - Similar spaces and clusters are visualized and compared.
   - In the AI tab, users can retrain the model and analyze any space.

4. **AI Model:**  
   - Feature engineering includes total amenities, normalized price, city encoding, and top amenities.
   - Synthetic target score is generated for supervised learning.
   - Model is trained and evaluated live in the app.
   - Model and features are saved to `/src/ai/` for persistence.

5. **Analysis & Recommendations:**  
   - Each space receives a detailed, explainable AI score.
   - The app provides pricing, amenity, and competitive analysis, plus actionable suggestions.

## 📦 File Structure
```
.
├── src
│   ├── ai
│   │   ├── model.pkl
│   │   └── features.pkl
│   ├── results
│   │   ├── extracted_amenities.csv
│   │   ├── merged_coworking_spaces.csv
│   │   └── MergedPlacesScoreDistance.csv
│   └── Images
│       ├── LocationMap.png
│       ├── CorrelationHeatmap.png
│       └── DataProcessing.png
├── app.py
├── requirements.txt
└── README.md
```

## Future Improvements

- **User Preferences**: Save user preferences for faster future searches
- **Additional Data Sources**: Integrate more coworking space databases
- **Advanced Filtering**: Add more granular filtering options like noise level and workspace type
- **Mobile Optimization**: Improve responsive design for mobile users
- **Community Reviews**: Incorporate user-generated feedback
- **Booking Integration**: Enable direct space reservations

---

📌 **Author:** Gabriel Fernandes Pinheiro  
🔗 [LinkedIn](https://www.linkedin.com/in/gabriel-fernandes-pinheiro) | [GitHub](https://github.com/gabriel-pinheiro) 