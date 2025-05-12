# Pet Care Management System (Odoo 17)

A comprehensive pet care management system built on **Odoo 17**. Designed for veterinary clinics, grooming salons, and pet care businesses to manage pets, appointments, health records, and finances in a streamlined workflow.

---

## 🚀 Features

### 🐾 Pet & Owner Management
- Pet profiles: breed, age, species, and health details
- Owner records: contact information and relationship to pets

### 📅 Appointment Scheduling
- Create, view, and manage pet appointments
- Appointment lines with selectable services (linked to products)
- Appointment type selection (Grooming, Vet Check-Up, Vaccination, etc.)
- Automated invoice generation from appointment lines

### 💳 Invoicing & Accounting
- Invoices are automatically created from appointments
- Integrated with Odoo's accounting module (`account.move`)
- Proper partner (owner) association on invoices

### 🧑‍💼 Role-Based Access Control
- **Pet Doctor**: View/manage medical appointments assigned to them
- **Groomer**: Access grooming menus and tasks
- **Pet Owner**: View only their pets and appointment history
- **Pet Manager**: Full access to all appointments and pet records

### 🔎 Smart Search View
- Filter by appointment status, type, pet, and more
- Group by date, pet, type, or status for fast data navigation

### 🔁 Cron Job
- Daily job that checks upcoming appointments and triggers notifications (email/SMS support ready)

---

## 🛠️ Technologies Used
- **Odoo 17** (backend, frontend, ORM, views)
- **Python 3.11**
- **PostgreSQL** for data storage

---

## 📸 Screenshots / Demo
> *You can add screenshots here or a link to a demo video.*

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
