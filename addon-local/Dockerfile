ARG BUILD_FROM
FROM $BUILD_FROM
COPY run.sh /run.sh
COPY govee /app/govee
COPY assets /app/assets/
COPY AmazonRootCA1.pem /app/
RUN chmod +x /run.sh /app/govee
CMD [ "/run.sh" ]
