# The-Luislang-Lives

The script is used to create tags in Tenable Vulnerability Management 

# How the tool works

The tool creates the following asset tags in Tenable Vulnerabiliy Management by reading input form an Excel Spread Sheet. Each worksheet in the spreadsheet will be populated with data for the relevant tags.

![worksheet](https://github.com/user-attachments/assets/8fc7e678-396c-49b8-a23f-db296d9e17f5)

## Tags based on IPv4

Tags based can be based on CIDR or IPv4 ranges comma separated.

![tags_ipv4](https://github.com/user-attachments/assets/951e23ff-12b2-4054-8781-bd7934c4bf22)

## Tags Based on Operating System

The tag is applied using filter operating_system is equal to. 

For example to tag all Windows Server Operating systems we add microsoft windows server in the operating_system column

![os Example](https://github.com/user-attachments/assets/4868e7b3-3a6a-44a6-a05f-e8463d34b1b0)

This tag will be applied to all Windows Server Operating systems.

![image](https://github.com/user-attachments/assets/73ef51aa-fdca-4527-b437-4be19ce46c69)

The worksheet is prepoulated with examples as a reference. Remove lines if not required.

![tags_by_operating_System](https://github.com/user-attachments/assets/23a0bb1f-70b9-4ae5-a90c-df026e1db313)

## Tags Based on FQDN

The tag is create on FQDN contains. For example, if you want to tag all your servers in the production environment and the naming convention is "server1-prod-internal" you add prod.internal as the value

![image](https://github.com/user-attachments/assets/583b3b01-339c-4ad4-8a6d-b4e58c217e87)

# Prerequistes

## Create Python virtual environment

1. Download files from Github
3. Change api_config.sh to excutable : chmod +x api_config.sh
4. run ./api_config.sh
5. Activate python virtual environment : source pytenable/bin/activate

## Create API User

1. Create a user in Tenable Vulnerability Manager and assign the 'Scan Manager role'

   ![create_user_1](https://github.com/user-attachments/assets/810013bb-a275-4fee-9540-af2da78aba3a)


2. Diable all authentication apart from API. complete the User creation

   ![user config 3](https://github.com/user-attachments/assets/06dc9b42-4fa4-4522-ae01-550d9fcba0f0)
   

4. Click more under API Keys


   ![generate API key 1](https://github.com/user-attachments/assets/9b29f765-96a9-4571-9a28-a6df08f1d102)


5. Click Generate API Key
   
   ![api key 2](https://github.com/user-attachments/assets/18a860b6-06e6-43e6-8e11-163e04362a77)

6. Copy API key somehwere safe for later use

   ![copy api key](https://github.com/user-attachments/assets/11e46937-544e-424c-8ef5-31a5d1a0807d)

## Modify Spreadsheet

1. Modify spreadsheet with the relvant values
2. Copy spreadsheet to the working folder.




  


