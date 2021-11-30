![alt text](https://github.com/k1nd0ne/VolWeb/blob/main/.images_readme/title.png)

Volweb is a digtialforensic memory analysis platform. The goal of VolWeb is to improve the efficiency of memory forensics by providing a centralized, visual and enhanced platform for incident responder and digital forensics investigators.
VolWeb is based on volatility3, and this platform will evolve with the framework development.

![alt text](https://github.com/k1nd0ne/VolWeb/blob/main/.images_readme/investigation.png)


**Volweb is still in Beta version and will evolve quickly.** 
Communications of updates will be released via twitter and by following the releases on github.

## Features ✅
The platform is currently supporting the following features: 

- Investigation creation and dump upload
- IoC import
- IoC extraction with linked process
- process tree
- process scan
- process dump
- process env
- process cmdline
- process privileges
- process dump
- network scan
- hashdump
- dlllist
- filescan
- Timeline Explorer
- User Authentication
- User Management
- Automatic Report Generation


## Getting Started 🛠️
Volweb is fully dockerized and ready to be deployed on a production server. 
In order to deploy Volweb, you will need to follow these steps: 

Clone the repository. 

```
git clone https://github.com/k1nd0ne/VolWeb
```

Then, edit the **docker/volweb.env** file and add the secret information according to your need to the following fields: 

```
 POSTGRES_USER=USER_HERE
 POSTGRES_PASSWORD=PASSWORD_HERE
 DJANGO_SECRET=SECRET_KEY_HERE
```

Next, add your ssl certificate into the **nginx/ssl** folder (generated via certbot for example).

```
cp fullchain.pem privkey.pem ./volweb-cert/docker/nginx/ssl
```

Build the docker and run it.

```
docker-compose build
docker-compose up -d
```

Create a superuser account: 

```
docker exec -it $(docker ps -aqf "name=django") python manage.py createsuperuser
```

The ngnix logs can be found in the **/ngnix/log** folder.

## Reset

/!\ This procedure will delete all the memory dump and database items and reset the volweb platform /!\

```
docker-compose down --rmi all --volumes
```

```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

## Important Note

To be able to see names of the forensic investigators, you’ll need to fill in the First Name and Last name fields in the User section from the Django administration panel.

![alt text](https://github.com/k1nd0ne/VolWeb/blob/main/.images_readme/Note.png)

## Issues ⚠️
If you have found an issue, please raise it. 
I'll perform 1 sprint every month to fix discovered bugs.

### Need to contact me? 
Contact me at k1nd0ne@mail.com for any questions regarding this tool.

# Next Release goals 
- Integrate Volatility results directly inside the database (Currently in JSON).
- Better file & process dump management (integration with celery)
- Add missing module for the windows memory analysis.
- Fix various discovered bugs.

# Global goals
- Mac OS support
- Linux support
- Visual confirmation of what to not look (legit process highlight integration)
- Import multiple IOC from a CSV
- Export IOCs to a CSV for qualification and integration to Threat Intelligence Platforms
