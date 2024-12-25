### Pet Care Management System
A comprehensive pet care management system built on Odoo 17. This system helps manage pet-related appointments, pet health records, pet owners, and more. It's designed to automate and streamline the workflow for pet care professionals.

#### Features
- Pet Management: Track pet information such as breed, type, and health records.
- Owner Management: Manage pet owners, contact details, and health-related information.
- Appointment Scheduling: Schedule and manage appointments for pets with automatic email notifications.
- Health Records: Track pets' health data including vaccinations, medical history, and treatments.
- Role-Based Access Control:
  - Menus, views (tree and form), and CRUD operations (create, update, delete) are controlled based on user roles.
  - For example:
    - Pet Doctor: Access only menus relevant to their role and can view or manage appointments assigned to them.
    - Pet Manager: Access all menus and manage all appointments.
    - Pet Owner: View only their pets' information and appointments.
    - Groomer: Access menus and views specific to grooming appointments and manage only their assigned grooming tasks.
- Advanced Appointment Search View:
  - A customizable search view with the following features:
    - Filters for appointment state (e.g., Done, Canceled, Scheduled).
    - Filters for appointment types (e.g., Vet Check-up, Grooming, Vaccination, Other).
    - Grouping options, including:
      - By State
      - By Pet
      - By Appointment Type
      - By Appointment Date
    - Designed to facilitate quick filtering and grouping for efficient appointment management.
- Cron Job: Every day, the system checks for appointments scheduled for the next day and prepares to send notifications (email/SMS) to the pet owners.

### Technologies Used
- Odoo 17: Framework for the system.
- Python 3.11: Backend development.
- PostgreSQL: Database backend.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.

