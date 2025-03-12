# VideoRecEngine - AI-Powered Video Recommendation System  

An advanced **AI-driven video recommendation engine** built using **FastAPI** and **PostgreSQL**, designed to provide personalized video suggestions based on user preferences and engagement patterns.  

---

## Project Overview  

VideoRecEngine leverages **machine learning** and **content-based filtering** to recommend videos tailored to individual users. Key features include:  

**Personalized Recommendations** – Analyzes user behavior for better suggestions  
**Category-Based Filtering** – Enables users to filter videos by interest  
**FastAPI for High Performance** – Asynchronous API handling for efficiency  
**PostgreSQL Database** – Ensures structured and scalable data storage  
**Alembic Migrations** – Manages database schema changes smoothly  

---

## Tech Stack  

- **Backend:** FastAPI (Python)  
- **Database:** PostgreSQL with SQLAlchemy ORM  
- **Migrations:** Alembic  
- **API Testing:** Postman / Curl  
- **Deployment:** Uvicorn  

---

## Prerequisites  

Ensure you have the following installed before running the project:  

- Python 3.8+  
- PostgreSQL database  
- Virtual environment (recommended)  

---

## Installation & Setup  

### Clone the Repository  

```bash
git clone <repository-url>
cd VideoRecEngine
```

---

### Set Up Virtual Environment  

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### Install Dependencies  

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables  

Create a `.env` file in the root directory and add the following:  

```env
DATABASE_URL=postgresql://user:password@localhost/video_rec_db
```

---

### Run Database Migrations  

```bash
alembic upgrade head
```

---

### Start the FastAPI Server  

```bash
uvicorn main:app --reload
```

---

## API Endpoints  

### Get Personalized Video Feed  

```http
GET /feed?username={username}
```

**Example Response:**  

```json
{
    "user": "john_doe",
    "recommended_videos": [
        {"id": 101, "title": "AI in 2025", "category_id": 1, "url": "https://video.example.com/101"},
        {"id": 202, "title": "Cybersecurity Trends", "category_id": 2, "url": "https://video.example.com/202"}
    ]
}
```

---

### Get Category-Based Video Feed  

```http
GET /feed?username={username}&category_id={category_id}
```

---

## Algorithm & Approach  

The recommendation engine utilizes **content-based filtering** and **user engagement analysis**:  

### Data Collection & Processing  

- Collects user interactions (likes, views, ratings)  
- Stores structured data in PostgreSQL  

### Feature Engineering  

- Analyzes video metadata (title, description, category)  
- Encodes categorical features for model training  

### Recommendation Model  

- Uses **cosine similarity** and **ranking methods** for recommendations  
- Implements **popularity-based fallback** for new users  

---

## Future Enhancements  

🔹 **Collaborative Filtering** – Improve recommendations using user similarity  
🔹 **Machine Learning Model** – Train deep learning models for better predictions  
🔹 **Scalability** – Deploy using **Docker** and **Kubernetes** for high availability  

---

## License  

This project is licensed under the **MIT License**.  
