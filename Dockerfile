FROM python:3.10

WORKDIR /usr/src/app

# COPY REQUIREMENT
COPY requirements.txt ./

# INSTALL REQUIREMENT
RUN pip install --no-cache-dir -r requirements.txt

# COPY SRC TO WORKDIR
COPY src .

# EXECUTE HANDLER
CMD [ "python", "./point_entree.py" ]


