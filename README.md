# fyp
wow!!!!!!!!!!!!

### 1. Setup Environment Variables

1. Make a copy of `.env.example`.
2. Rename the copy to `.env`.
3. Fill in the required values in the `.env` file.

### 2. Build and Run Docker Containers

1. Download Docker Desktop

2. Build the Docker containers:
    ```sh
    docker-compose build
    ```
3. Start the Docker containers:
    ```sh
    docker-compose up -d
    ```

### 3. Access the Application

1. Open your web browser and navigate to the frontend URL.
2. If this is your first startup, The backend will take a few minutes to process the training data and set up the vector database. The frontend will automatically detect if the backend is ready.
2. Login with the default user credentials at the Login page:
    - **Username**: `user`
    - **Password**: `naoto`
3. Go to `/chat` to access the chat functionality.


## Clearing data to reset application after first startup
1. Delete `backend/chroma_db` to clear vector database
2. Delete `backend/modelling/extracted_text.txt` to delete extracted text
3. Delete project Docker volumes for project to clear message history