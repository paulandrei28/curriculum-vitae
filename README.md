# Curriculum Vitae Application

Premium Flask application that presents my curriculum vitae as an interactive website with a Wordle easter egg and analytics tracking.

## Run

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:10000` in your browser.

## Features

- **Tabbed Experience**: Experience, projects, skills, and education sections
- **Featured Projects**: NexuShop microservices platform, Automated Trading Platform, and RWOTD Progressive Web App
- **Learning Projects**: Secondary section showcasing educational and practice projects
- **Direct Links**: GitHub and LinkedIn profile links
- **Downloadable Resume**: PDF curriculum vitae available for download
- **Wordle Easter Egg**: Recruiter-friendly Wordle game hidden in the bottom-right corner with programming-themed word bank
- **Analytics Tracking**: Google Analytics 4 integration to track visits, CV downloads, and game interactions
- **Mobile Responsive**: Fully responsive design with touch-friendly Wordle controls for mobile devices

## Configuration

### Google Analytics 4

To enable analytics tracking, replace the placeholder `G-XXXXXXXXXX` in `templates/curriculum_vitae_homepage.html` with your GA4 tracking ID:

```html
<!-- Line 11 in templates/curriculum_vitae_homepage.html -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YOUR_TRACKING_ID"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-YOUR_TRACKING_ID');
</script>
```

### Tracked Events

The application tracks the following events in Google Analytics:
- **Page Views**: Automatically tracked on page load
- **CV Download**: Tracked when the "Download PDF" button is clicked
- **Game Open**: Tracked when the Wordle easter egg button is clicked

## Deployment

The application is deployed on Render and accessible at `https://paulsiposcv.onrender.com`

## Project Structure

```
curriculum-vitae/
├── app.py                          # Flask application
├── curriculum_vitae_content.py     # CV data and projects
├── templates/
│   └── curriculum_vitae_homepage.html
├── static/
│   ├── assets/                     # Images and icons
│   ├── documents/                  # PDF resume
│   ├── scripts/
│   │   ├── curriculum_vitae_tabs.js
│   │   └── wordle_game.js          # Wordle game logic
│   └── styles/
│       ├── curriculum_vitae_styles.css
│       └── wordle_game.css         # Wordle styling
├── Procfile                        # Render deployment config
└── requirements.txt
```

## Technologies

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Analytics**: Google Analytics 4
- **Deployment**: Render
- **Game**: Vanilla JavaScript (no dependencies)
