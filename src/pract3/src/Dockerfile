#docker build -t cas_ub .
#docker run --name cas_ub cas_ub
FROM ubuntu
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl
RUN curl -OL https://dlcdn.apache.org/cassandra/4.0.12/apache-cassandra-4.0.12-bin.tar.gz
RUN tar -xzvf apache-cassandra-4.0.12-bin.tar.gz
RUN echo PATH="${PATH}:/apache-cassandra-4.0.12/bin:/apache-cassandra-4.0.12/tools/bin" >> /etc/bash.bashrc
RUN chmod +x apache-cassandra-4.0.12/bin/cassandra.in.sh && ./apache-cassandra-4.0.12/bin/cassandra.in.sh
CMD ["./apache-cassandra-4.0.12/bin/cassandra", "-R", "-f"]