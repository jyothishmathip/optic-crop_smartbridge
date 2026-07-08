# OptiCrop — Smart Agricultural Production Optimization Engine

This repo contains **two versions** of the same crop recommendation app:

1. **`index.html`** — a single, self-contained static site (the model runs client-side in
   JavaScript). No server needed. This is what **GitHub Pages** will serve automatically.
2. **`app.py`** + **`templates/`** — the full Flask version with a real Python backend and
   the trained scikit-learn model (`model.pkl`). Deploy this to Render for a proper
   Flask-based live site.

## 1. Static site on GitHub Pages (already works out of the box)

Once this repo is pushed to GitHub:
- Go to **Settings → Pages**
- Source: **Deploy from a branch** → Branch: **main**, folder: **/ (root)** → **Save**
- Your site goes live at `https://yourusername.github.io/opticrop/`

GitHub Pages automatically serves `index.html`, so no extra setup is needed.

## 2. Flask app on Render (matches the project's Flask requirement)

1. Push this repo to GitHub (steps below).
2. Go to **https://render.com** → sign up/log in → **New +** → **Web Service**.
3. Connect this GitHub repo.
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**. Render builds and gives you a live URL like
   `https://opticrop.onrender.com`.

(`Procfile` and `gunicorn` are already included in this repo for this exact purpose.)

## 3. Run it locally (Flask version)

```bash
pip install -r requirements.txt
python app.py
```
Open the URL printed in the terminal (usually `http://127.0.0.1:5000`).

## 4. Run it locally (static version)

Just double-click `index.html` — it opens directly in your browser, no install needed.

## Pushing this folder to GitHub

```bash
git init
git add .
git commit -m "Initial commit - OptiCrop"
git branch -M main
git remote add origin https://github.com/yourusername/opticrop.git
git push -u origin main
```

## Retraining with your real dataset

This build ships with a synthetic dataset (`generate_dataset.py`) shaped like the Kaggle
`Crop_recommendation.csv`. To use the real one:
1. Replace `Crop_recommendation.csv` with the real file (same columns:
   `N, P, K, temperature, humidity, ph, rainfall, label`).
2. Run `python train_model.py` to retrain and overwrite `model.pkl`.
3. If you also want `index.html`'s in-browser predictions to reflect the retrained model,
   re-export the coefficients and rebuild it (ask Claude to regenerate `index.html` from
   the new `model.pkl`).
