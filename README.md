# ubiquitous-candidate



## 🤖 AI Recruitment Assistant

A multi-agent AI system for HR that automates candidate selection based on the resume, incorporating - resume parsing, candidate matching, and industry trend insights for smarter recruitment decisions.


## ⚙️ Installations

```bash
git clone https://github.com/rrahulg/ubiquitous-candidate.git
cd ubiquitous-candidate
conda create --name agents
conda activate agents
pip install -r requiremnts.txt
```

``` ini
make sure your .env file contains
GEMINI_API_KEY = "your_google_api_key"
GROQ_API_KEY = "Your_groq_api_key"
PHIDATA_API_KEY = "Your_phi_api_key"
password = 'google app key for sending email'
```

``` powershell
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16

```

## 📂 Project Structure

```
.
├── agents/
│   ├── __init__.py
│   ├── action_agent.py
│   ├── greeting_agent.py
│   ├── kb_agent.py
│   └── web_search_agent.py
├── data/
│   ├── data.json
├── knowledge_base/
│   ├── __init__.py
│   ├── json_kb.py
│   └── website_kb.py
├── logs/
│   ├── 03_31_2025_15_02_16.log/
│       └──  03_31_2025_15_02_16.log
├── tools/
│   ├── __init__.py
│   ├── data_json_generator.py
│   └── logger.py
├── main.py
├── .gitignore
├── config.py
├── .env
├── requirements.txt
└── README.md
```
## 🧠 Refrence Architecture
![Refrence architecture of agentic workflow](./Recruiting%20agent%20refence%20architecture.png)

## 🚀 Run the App
``` cmd
 python main.py 
 ```