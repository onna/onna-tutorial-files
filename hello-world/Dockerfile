# Try: https://github.com/pypa/virtualenv/issues/1558
FROM python:3.7-slim-buster
LABEL maintainer "Onna Docs Team<sven@onna.com>"

ENV VIRTUAL_ENV=.venv
# hadolint ignore=DL3008
RUN useradd --create-home appuser \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends gettext-base \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /home/appuser
USER appuser
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies and cleanup
COPY --chown=appuser:appuser requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf requirements.txt

# Copy needed files
COPY --chown=appuser:appuser check-auth.py .
COPY --chown=appuser:appuser run.sh .
COPY --chown=appuser:appuser auth.py .

# Run the appp
RUN chmod +x check-auth.py \
    && chmod +x run.sh

#ENTRYPOINT ["bash" ]
ENTRYPOINT [ "./run.sh" ]