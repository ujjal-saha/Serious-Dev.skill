# Python packages

Install with `pip install <name>` inside a virtual environment. Add the package to `requirements.txt`.
Check first whether the standard library already does the job: `csv`, `json`, `pathlib`, `argparse`, `sqlite3`, `datetime`, `urllib`, `tomllib`, `zipfile`, `hashlib`, `secrets`, `logging`, `unittest`, `concurrent.futures`, `statistics`.

## Web and HTTP

| Package | Install | Use it for |
|---|---|---|
| requests | pip install requests | HTTP calls, GET, POST, REST API, download a file |
| httpx | pip install httpx | async HTTP client, HTTP/2, modern replacement for requests |
| beautifulsoup4 | pip install beautifulsoup4 | parse HTML, scrape web pages, find tags (import bs4) |
| lxml | pip install lxml | fast XML and HTML parsing, XPath |
| playwright | pip install playwright (then run: playwright install) | browser automation, JavaScript pages, screenshots, website testing |
| yt-dlp | pip install yt-dlp | download video or audio from YouTube and other sites |
| flask | pip install flask | small web app, simple API server |
| fastapi | pip install fastapi uvicorn | fast API server, async, automatic API docs |
| django | pip install django | full web framework, admin panel, database ORM |
| streamlit | pip install streamlit | quick web dashboard or data app UI |

## Data and files

| Package | Install | Use it for |
|---|---|---|
| numpy | pip install numpy | arrays, fast math, matrices |
| pandas | pip install pandas | tables, dataframes, read CSV, clean and group data |
| scipy | pip install scipy | scientific math, statistics, optimization, signal processing |
| openpyxl | pip install openpyxl | read and write Excel xlsx files |
| pypdf | pip install pypdf | read, merge, split PDF files |
| reportlab | pip install reportlab | create PDF files from code |
| python-docx | pip install python-docx | read and write Word docx files (import docx) |
| python-pptx | pip install python-pptx | create PowerPoint pptx files (import pptx) |
| pyyaml | pip install pyyaml | read and write YAML files (import yaml) |
| jinja2 | pip install jinja2 | text and HTML templates |

## Images, audio, video, OCR

| Package | Install | Use it for |
|---|---|---|
| pillow | pip install pillow | open, resize, crop, convert images (import PIL) |
| opencv-python | pip install opencv-python | computer vision, camera, video frames, image processing (import cv2) |
| pytesseract | pip install pytesseract (also needs the Tesseract program) | OCR, read text from images |

## Charts

| Package | Install | Use it for |
|---|---|---|
| matplotlib | pip install matplotlib | charts, plots, graphs saved as images |
| plotly | pip install plotly | interactive charts, dashboards |

## Machine learning and AI

| Package | Install | Use it for |
|---|---|---|
| scikit-learn | pip install scikit-learn | classic machine learning, classify, cluster, regression (import sklearn) |
| torch | pip install torch (heavy, ask first) | deep learning, neural networks (PyTorch) |
| transformers | pip install transformers | pre-trained language and vision models, Hugging Face |
| spacy | pip install spacy | fast NLP, named entities, language pipelines |
| openai | pip install openai | call OpenAI API models |
| anthropic | pip install anthropic | call Claude API models |

## Command line, config, validation

| Package | Install | Use it for |
|---|---|---|
| click | pip install click | command-line tools with options and sub-commands |
| typer | pip install typer | command-line tools using type hints |
| rich | pip install rich | colored terminal output, tables, progress bars, pretty print |
| tqdm | pip install tqdm | progress bar for loops |
| pydantic | pip install pydantic | validate data, settings, typed models |
| python-dotenv | pip install python-dotenv | load settings from a .env file |
| jsonschema | pip install jsonschema | validate JSON against a schema |

## Dates, text, small helpers

| Package | Install | Use it for |
|---|---|---|
| python-dateutil | pip install python-dateutil | parse date strings, relative dates, time deltas |
| rapidfuzz | pip install rapidfuzz | fuzzy string matching, similar text, typos |
| tenacity | pip install tenacity | retry a failing call with wait and back-off |
| psutil | pip install psutil | CPU, memory, disk, running processes |
| pyautogui | pip install pyautogui | control mouse and keyboard, screenshots |

## Databases, cloud, scheduling, security

| Package | Install | Use it for |
|---|---|---|
| sqlalchemy | pip install sqlalchemy | SQL database ORM and queries |
| pymongo | pip install pymongo | connect to MongoDB |
| redis | pip install redis | connect to Redis cache or queue |
| boto3 | pip install boto3 | Amazon AWS, S3 files, cloud services |
| paramiko | pip install paramiko | SSH and SFTP, remote commands |
| apscheduler | pip install apscheduler | run jobs on a schedule, cron in Python |
| schedule | pip install schedule | simple job scheduling, run every N minutes |
| cryptography | pip install cryptography | encryption, certificates, secure keys |
| pyjwt | pip install pyjwt | create and check JWT login tokens (import jwt) |
| bcrypt | pip install bcrypt | hash passwords safely |

## Testing

| Package | Install | Use it for |
|---|---|---|
| pytest | pip install pytest | write and run tests |
