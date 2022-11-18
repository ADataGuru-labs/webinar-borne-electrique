FROM python:3.10

WORKDIR /usr/src/app

# COPY REQUIREMENT
COPY requirements.txt setup.py ./

# INSTALL REQUIREMENT
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install -e .

# COPY SRC TO WORKDIR
COPY src ./src

# EXECUTE HANDLER
CMD [ "python", "./src/normalisation/point_entree.py" ]


