FROM python:3.10

WORKDIR /usr/src/app

# COPY REQUIREMENT
COPY application/requirements.txt setup.py ./

# INSTALL REQUIREMENT
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install -e .

# COPY SRC TO WORKDIR
COPY application/normalisation/src ./application/normalisation/src

# EXECUTE HANDLER
CMD [ "python", "./application/normalisation/src/point_entree.py" ]


