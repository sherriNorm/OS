Fist step is to set up the EC2 machine Configure the security setting so that it can traffic on ports: 80, 22, 443, 5432, 8000, and all traffic. Launch an EC2 instance (Ubuntu) Connect to SSH into EC2: Run: ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP>

Run commands sudo apt update -y sudo apt install python3 -y pip3 install flask pymysql flask-cors

Set up RDS PostgreSQL: Make sure the RDS instance allows all traffic from the EC2 instance (public access). psql -h <RDS_End_Point> -U <RDS_User> -d <RDS_Database_Name>

Add an inbound rule to the RDS security group: Type: PostgreSQL Source: EC2 Security Group (or 0.0.0.0/0 for testing)

Then we need to go to DBeaver and donwload database from kaggle mkdir webapp_sherzod cd webapp_sherzod python3 -m venv venv source venv/bin/activate nano app.py input backend app.py

 Setup S3 for Frontend Hosting
Step 1: Create an S3 Bucket
Enable Static Website Hosting

Upload your frontend index.html file

Step 2: Update Permissions
Make objects publicly readable

Set the bucket policy for public read access (for testing):

run python3 app.py
