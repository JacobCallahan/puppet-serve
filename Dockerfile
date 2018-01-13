FROM ruby

RUN apt-get update && apt-get install -y gcc ruby-dev
RUN gem install puppet-forge-server
RUN mkdir modules
COPY modules/ modules/

CMD puppet-forge-server -m /modules
