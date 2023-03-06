Getting Started With Djagno Blog With Django Framework
===================================

This blog is made with django framework and the django version is 4.0.1. It's a intermediate level of blogging. For now I have included this features only. In future I will develop more.

## Screenshots

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/1.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/2.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/3.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/4.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/5.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/6.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/7.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/8.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/9.png)

![Django Blog](https://raw.githubusercontent.com/tajbinkhan/django-blog/main/screenshots/10.png)

# New Update
* Post Duplication

# Features on this blog
* User Registration
* User Login & Logout
* User Profile
* Create, Update, Edit & Delete Posts
* Comments
* Search
* User Change Password
* Password Reset
* Customized Admin Panel
* Social Authentication
* User Email Verification
* Add Multiple Email Account
* User Account Deletion From Profile
* HTML Email Template
* Advanced CKEditor

## Installation

Install Django Blog with pip

Clone the project.
```bash
  git clone https://github.com/tajbinkhan/django-blog.git
```
Go to the project directory (if you are a windows user).
```bash
  cd django-blog
```
In command panel, run this command.
```bash
  pip install -r requirements.txt
```
After successfull installation, you need to start the migration to create table in the database.
```bash
  python manage.py makemigrations
  python manage.py migrate
```
After migration, start the server by running this command.
```bash
  python manage.py runserver
```

## Versions
Added new features to **Django Blog**

### v4.7
* Post Can Be Duplicated.
* Minor Bug Fixed.

### v4.6 (Admin Panel New Design)
* New Highly New Customization Design.
* New Icon to Understand Better and Look More Professional.
* New Plugin Called Jazz Admin Is Installed to Give This Professional Look.

### v4.5 (Big Update)
* Email Messages Can Be Customized From Admin Panel.
* Shortcodes Are Being Used In The Message.
* HTML Email Template Integration From Admin Panel.
* Website CSS File Optimized.
* New Editor Installed (ckeditor).
* More Option Is Available In The Editor.
* Code Optimized.
* Comment Can Be Updated From Front-end (Admin only).
* Comment Can Be Deleted From Front-end (Admin only).

### v4.4
* Some CSS Issue Fixed.
* Security Level Upgraded.
* Email Notification Has Advanced Features.
* User Will Be Notified If He/She Change Password of Their Account.

### v4.3
* Admin Panel Modification.
* User Can Delete Their Own Account From Their Profile.
* Social Account Verification Has Been Removed.

### v4.2
* New User Registration Email Notification.
* New Comment on Blog Post Notification.

### v4.1
* Messages are shown when post update, delete or created.
* Post form fields updated.
* Template customization update.
* Email notification.

### v4.0
* Django Allauth Feature Added.
* New Profile Customization.
* Facebook, Google Authentication Added.
* Verification System Added.

### v3.9
* Social Authentication Added.

### v3.8
* Session Timeout Added.
* Login success message display.
* Search option bug fixed.

### v3.7
* 404 error page added.
* Invalid URL shows the error page.

### v3.6
* In this version the uploaded image will be resized and reduce the image size for site speed up.

### v3.5
* User can reset his/her password through reset password form.
* User will receive a password reset mail on their registered account on the site.
* User can change password in profile.
* There is some bug in search list and that is fixed.

### v3.4
* Create post, create category, can comment now in available in the front-end(Only for superuser)
* Category can be created in create post form.
* Category can be manage in the front-end.

## Tech Stack

**Language**: HTML5, CSS3, JavaScript, Python

**Framework**: Django Web Framework, BootStrap 4

## Authors

- [Webphics](https://www.webphics.com)
## License

[MIT](https://choosealicense.com/licenses/mit/)

