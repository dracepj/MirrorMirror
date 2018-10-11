# This script needs to be run with sudo so we can globally install dependencies
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

echo "We will run updates & upgrades first for Raspbian & the R-PI... this will"
echo "probably take quite a while."
# Run all the update commands
apt-get -y clean
# This is a third-party created kernel & firmware updater
apt-get -y install rpi-update
apt-get -y update
apt-get -y upgrade
apt-get -y dist-upgrade
rpi-update

# Let's get Erlang, which is required by RabbitMQ
apt-get install -y erlang
apt-get install -y rabbitmq-server

# Now let's get the python dependencies
pip3 install guizero
pip3 install pika


echo "You should reboot now."

