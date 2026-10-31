# Bon Secours College – Premium 3D Virtual Campus

A Streamlit web app with an embedded Three.js campus-driving concept.

## Included
- Premium dark maroon campus UI
- 3D campus grounds, entrance arch, internal roads, paths, trees and illustrative blocks
- Car, college bus and walk modes
- WASD / arrow-key controls and touch buttons
- Third-person, driver and top camera modes
- Day/night toggle
- Destination list with jump-to-location controls
- Mini campus overview map

## Important accuracy note
This is a detailed concept reconstruction based on publicly described campus facilities and a plausible campus layout. It is **not** a verified architectural or survey-grade replica. Publicly accessible information does not provide authoritative building footprints, exact road geometry, or a complete measured site plan. Do not treat the illustrative block positions as exact. To make it truly accurate, replace the scene geometry with an official campus master plan, measured building dimensions, or properly licensed aerial/survey imagery.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## GitHub upload
Upload `app.py`, `requirements.txt`, `README.md`, and `.gitignore` to the root of a GitHub repository.

## Deploy on Streamlit Community Cloud
1. Visit https://share.streamlit.io/
2. Select **Create app**.
3. Choose your GitHub repository and branch.
4. Set **Main file path** to `app.py`.
5. Select **Deploy**.

The 3D engine is loaded from public CDNs with automatic fallback (cdnjs, jsDelivr, then unpkg). The deployed browser needs an internet connection to reach at least one of these CDNs. If all are blocked, the app displays a retry message instead of silently failing.

## Controls
- W / ↑: accelerate
- S / ↓: reverse
- A / ← and D / →: steer
- Space: brake
- R: reset vehicle
- C: change vehicle
- Sidebar navigation: switch tour, drive and walk modes
