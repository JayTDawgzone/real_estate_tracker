# real_estate_tracker
A tool for tracking real estate and rental properties.

#### Requirements:

* Django==2.2.4
* django-environ==0.4.5
* Pillow==7.1.2
* psycopg2==2.8.5
* psycopg2-binary==2.8.5
* pytz==2020.1
* sqlparse==0.3.1

#### How to run:
1. Create a virtual enviroment and activate it
2. Activate the environment and install requirements.txt
3. Run ```python manage.py runserver```




### Summary

This Django application was designed for a real-estate investor that wanted a tool to manage their many properties and share them with potential buyers.

Users with admin credentials are able to view and manage confidential information about each property including: job tracking, expenses, mortgage information, and net operating income. Regular visitors only see a standard real estate listing with basic information about the property.

The admin section gives the user front-end access to the SQL database to easily search for records, upload forms and images, and manage their properties.

### Visitor view

Visitors to the website will only be able to see listings that have been approved by an admin. They are able to view these properties and submit inquiries related to these properties. Inquiries are then received and reviewed by Admins.

**Viewer Search Functionality**

![viewer-search](https://user-images.githubusercontent.com/55102118/87850774-a1ed5280-c8a7-11ea-9c0e-11e5df13cb2e.png)

**Viewer Listing Example**

![viewer-listing](https://user-images.githubusercontent.com/55102118/87850777-a3b71600-c8a7-11ea-9f72-670f733fcbb5.png)

### Admin View

Admins are able to view confidential information related to their properties, upload documents and images, add expense information, and push listings to public view. The admin section allows front-end access to the SQL database to manage their properties.


**Admin Listing View**

![admin-listing](https://user-images.githubusercontent.com/55102118/87850781-a6b20680-c8a7-11ea-87a6-2bb96c0e3ebb.png)




**Admin Database**

![admin-section](https://user-images.githubusercontent.com/55102118/87850779-a4e84300-c8a7-11ea-9446-283f5646ac59.png)
