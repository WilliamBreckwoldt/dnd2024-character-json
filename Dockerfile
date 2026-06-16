# Reproducible build + runtime for the D&D 2024 character-sheet generator.
# Pinning the base image and requirements.txt means it will still build years
# from now without dependency surprises.
FROM python:3.12-slim

WORKDIR /app

# Dependencies first, so this layer is cached unless requirements.txt changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project files.
COPY . .

# Validate every character against the spec, then fill the sheets.
# Generated PDFs are written to /app/output — mount a volume there to keep them:
#   docker run --rm -v "$PWD/output:/app/output" dnd-sheets
CMD ["sh", "-c", "python validate.py && python generate_sheets.py"]
