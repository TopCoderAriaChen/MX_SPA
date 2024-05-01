# MX Online Learning Platform - Single Page Application(SPA)

The MX Online Learning Platform is a comprehensive solution designed for facilitating online education. It encompasses user management, course creation, enrollment processes, and interactive learning sessions, tailored to the needs of administrators, teachers, support staff, and students.


## Contents

- Project Overview
- Key Features
- Getting Started
- System Architecture
- License
- Contributors


### Project Overview

The platform is carefully designed to accommodate multiple user roles, each with distinct accessprivileges and responsibilities:

- **Admin**: This is the top-level role in the system hierarchy. Admins have the authority to manage all aspects of the platform. They ensure that all operations from user management to system settings are running smoothly.
  - *System Owner*: The ultimate authority with access to all system settings and configurations.
  - *Campus Admin*: Manages campus-specific settings and information.
  - *Course Admin*: Oversee course-related administrative tasks.
  - *User Admin*: Responsible for the management of user accounts.
  - *Order Admin*: Handles financial transactions and course enrollments.
  - *Lecture Admin*: Focuses on managing lectures and related content within courses.

- **Support**: These are specialized admins with a subset of administrative permissions, focusing on course content, user management, order processing, and lecture administration.

- **Teacher**: Teachers are content creators and educators who are responsible for developing course materials and engaging with students. They can:
  - Create courses and upload detailed course information.
  - Add live lecture sessions and manage their scheduling.
  - Upload educational materials that students can access and download for learning purposes.

- **Student**: The primary learners on the platform who can:
  - Browse the course catalog to view available courses.
  - Purchase and enroll in courses with the option to complete financial transactions through the platform.
  - Access their enrolled courses, attend lectures, and study through provided materials.

Students experience a seamless enrollment process, which involves browsing courses, purchasing them, and then being enrolled by an admin or support role once payment is confirmed. They then gain access to all the lectures and learning resources within each course.


### Key Features

- **Dynamic User Management**: The platform allows for the creation, updating, and deletion of user accounts across various roles. Detailed permissions can be set for different types of admins, ensuring that each has access only to the appropriate tools and information they need to perform their roles effectively.

- **Comprehensive Course Management**: Admins and teachers can create courses, set prices, manage enrollments, and upload materials. Each course can be equipped with a unique code, detailed description, and relevant images to attract and inform prospective students.

- **Interactive Order Processing**: Support roles can track orders and confirm payments, allowing for the smooth enrollment of students into their chosen courses. This process also includes order time tracking and payment management.

- **Robust Learning Management**: At the heart of the platform is the learning experience. Students can access a variety of lectures within each course, each containing live session links and downloadable materials, providing a rich and flexible educational experience.

- **Enrollment Workflow**: Students follow a clear path from course discovery to learning. They browse courses, make a purchase, and upon payment confirmation, are enrolled by an admin or support member. They can then embark on their learning journey, with each lecture and its materials guiding their progress.


### Getting Started

Follow these instructions to set up and run the project on your local machine:

#### Prerequisites

Before you begin, ensure you have the following installed:
- Node.js
- Python 3.x
- Docker
- MongoDB

#### Setup Instructions

To run this project locally:

1. Clone the repository from GitHub.
2. Connect to the MongoDB.
3. Follow the backend setup instructions.
4. Follow the frontend setup instructions.
5. Use Docker to build and run the containers necessary for the application.
5. Start the Flask app to serve the backend API.

##### Backend Setup

1. **Clone the Repository**  
   Begin by cloning the MX_SPA repository from GitHub to your local machine.

   ```shell
   git@github.com:TopCoderAriaChen/MX_SPA.git
   cd MX_SPA
   ```

2. **Initialize Backend Environment**  
   Navigate to the backend directory and set up your Python virtual environment.

   ```shell
   cd backend
   source ./venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Python packages**
    After activating the virtual environment, install the required Python packages.

   ```shell
   pip install -r requirements.txt
   ```

4. **Database Configuration and Initialization**  
   After connected with MongoDb, run the initialization script to create and seed your database with initial data.

   ```shell
   python init-db.py
   ```

5. **Launch Backend Server**  
   Start the Flask server to begin serving the backend API.

   ```shell
   python server.py
   ```

###### Frontend Setup

1. **Navigate to the Frontend Directory**  
   In a new terminal window, switch to the frontend directory.

   ```shell
   cd ../frontend
   ```

2. **Install Dependencies**  
   Install the project's node dependencies.

   ```shell
   pnpm install
   ```

3. **Run the Development Server**  
   Start the frontend development server.

   ```shell
   pnpm dev
   ```

4. **Access the Application**  
   Once the servers are running, open your web browser and go to `http://localhost:8080` to view the application.


### System Architecture

Leveraging a Python Flask backend, Vue.js frontend, and MongoDB for data persistence, the platform's architecture is designed for performance, scalability, and ease of maintenance. Docker is used to streamline deployment and ensure consistency across environments.


### License

This project is licensed under the MIT License. See the LICENSE file in the repository for full licensing details.


