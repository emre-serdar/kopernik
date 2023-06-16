# Kopernik Project

This project aims to provide a solution for transferring satellite images from a Raspberry Pi, collected using a Python Selenium robot, to an existing WordPress website. The solution involves implementing a Django REST API and deploying it on AWS EC2 and RDS. The WordPress website is migrated from HostGator to AWS, utilizing the same EC2 instance and RDS instance to create a more streamlined and efficient system. The satellite images are fetched from the Django API using Vanilla JS on the WordPress pages.

## System Diagram

![Kopernik System Diagram](https://github.com/emre-serdar/kopernik/blob/main/KopernikSystemDiagram.png)

The system diagram provides an overview of the architecture and components involved in the project.

## Problem Statement

The existing system relied on a Python Selenium robot to transfer satellite images, which did not consistently perform well. This project aims to address the limitations of the previous system and provide a more reliable and efficient solution.

## Achievements

The Kopernik project has accomplished the following:

- Developed a Django REST API to facilitate the transfer of satellite images from a Raspberry Pi to the WordPress website.
- Deployed the Django API Server on AWS EC2 using Nginx & Gunicorn on the Linux platform.
- Migrated the WordPress website from HostGator to AWS, resulting in improved performance and server response time.
- Implemented Vanilla JS on the WordPress pages to fetch and display the satellite images from the Django API.
- Created a more streamlined and compact system by utilizing the same EC2 instance and RDS instance for both the Django API and the WordPress website

## Deployment

To deploy the Kopernik project, follow the steps below:

1. Set up the Django REST API on the AWS EC2 instance:

   - Install the required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Configure the Django settings with your database credentials and other necessary configurations.

   - Run the Django migrations to set up the database:

     ```bash
     python manage.py migrate
     ```

   - Start the Django development server:

     ```bash
     python manage.py runserver
     ```

     The API endpoints will be accessible at `django.emreserdar.com/satellite/list`.

2. Migrate the WordPress website from HostGator to AWS:

   - Export the WordPress database from HostGator using `mysqldump`:

     ```bash
     mysqldump -u <username> -p<password> <database> > data.sql
     ```

   - Import the database dump into AWS RDS using `pgloader`:

     ```bash
     pgloader mysql://[username]:[password]@localhost/[database_name]
     ```

   - Update the necessary configurations in the WordPress settings to connect to the AWS RDS database.

3. Fetch satellite images from the Django API on WordPress pages:

   - Include the following code snippet in the WordPress pages where satellite images should be displayed:

     ```html
     <!-- Example for NOAA15 Archive -->
     <div id="meteor_row" class="row">&nbsp;</div>

     <div id="myModal" class="modal">
       <span class="close">&times;</span>
       <h2 id="modal-title"></h2>
       <img class="modal-content" id="img01">
     </div>

     <script async="">
       // JavaScript code to fetch and display satellite images from the Django API
     </script>
     ```

     Customize the JavaScript code according to your API endpoint and data structure.

4. Access the WordPress website and verify that the satellite images are being fetched from the Django API successfully.

## Deployment Details

- Deployed the Django API Server on AWS EC2 using Nginx & Gunicorn on the Linux platform.
- Connected to the shared RDS server, resulting in a 40% reduction in server response time.

## Contributors

- [Emre Serdar](https://github.com/emre-serdar)


Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the [Apache-2.0 license](LICENSE).
