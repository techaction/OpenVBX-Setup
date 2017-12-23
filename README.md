# OpenVBX Setup


### Introduction


OpenVBX is an online phone management system developed by Twilio, and which a
user can self-host.  This allows the user to have maximum flexibility in
managing a phone system, determining where calls into a number will be routed
and what the results of these calls will be.


In our work the Technology Action Project has used OpenVBX in building
resilient phone systems for hotlines and dispatch use cases.  The goal of
these systems is to provide maximum anonymity for users of the system while
also providing an easy to use interface through which a phone system can be
built.


On the Twilio development roadmap is a framewwork called Twilio Studio, which
is meant to bring the functionality of OpenVBX into the Twilio user console.
While this does present some conveniences, such as not having to run a server,
in our specific use case, one of users that are at risk of repression, this
limits options of hosting and the ways in which the application can be opened
up to other trusted users for management.


In the initial versions of Twilio Studio the use will be confined to one account,
limiting additional administrators from being able to make dynamic changes to
the system.  Additionally, by hosting this functionality on Twilio it prevents
the users from choosing to host the service through structures like Tor
Hidden Services, cjdns mesh nets or other anonymity networks.  Further, in
hosting the functionality on Twilio the only way to manage the infrastructure
is to log in to Twilio, which risks compromising the IP addresses of users.


Unlike other systems like FreePBX, OpenVBX is easily learned and can be taught
to unskilled users in a matter of hours.  It is also easy to set up, allowing
for systems to be deployed and taken down when necessary, essential in
contexts in which political repression is possible.  We will be including
documentation for how to use and configure an OpenVBX server in the near
future.


Also on a potential development roadmap may be custom modules, dockerized
setups and code customizations.  The version that we are currently hosting
in this repository contains some modifications to the code base to allow
for easy user setup and the setting of passwords, a feature which is reliant
on having to run a separate email server in the original version.


Check https://techaction.io for updates on this project.


### Installation


For the purposes of this project we have forked the OpenVBX repository from the
new maintenance fork created by gegere which can be found [here](https://github.com/gegere/OpenVBX)


We have made some changes to the underlying PHP to allow for easy setting and
resetting of user passwords based on the pull request to the Twilio repository
documented [here](https://github.com/ocsnetworks/OpenVBX/commit/36cb6958f5721082ab10799de5411547acf21e13)


For installation we recommend using Ubuntu Server 16.04 which can be found
[here](https://www.ubuntu.com/download/server)


After installation clone this repository

`git clone https://github.com/techaction/OpenVBX-Setup.git`


Then cd into the directory

`cd OpenVBX_Setup`


Execute the script to install

`python3 openVBXsetup.py`


This is not an unattended installation, and will, at various points, require
interaction by the user, mostly for the purpose of being able to provide
passwords.

During installation make sure to write down the database name, database user
and database password for use during the post installation configuration
process.


### Post installation


After the system has installed go to the IP address, or domain, of the server
and make sure that the checks pass.


If all checks are passed initiate the post installation configuration process
through the web frontend.  For this you will need to know the email address of
the primary administrative user, a password for that user and the database name,
database user, and database name for the database that you set up during the
running of the installation script.


If you would like to run the system through https, which everyone should,
please follow these relatively straight forward directions
[https://www.techrepublic.com/article/how-to-install-and-use-lets-encrypt-on-a-ubuntu-server-for-ssl-security/](https://www.techrepublic.com/article/how-to-install-and-use-lets-encrypt-on-a-ubuntu-server-for-ssl-security/)
