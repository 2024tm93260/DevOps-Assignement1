FROM python:3.11-slim

# Install X11 libraries for Tkinter to work (optional: may not work on headless CI)
RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "ACEest_Fitness.py"]
