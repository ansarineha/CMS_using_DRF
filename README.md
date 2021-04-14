# CMS_using_DRF

I have developed  a Content Management System API using Django Rest Framework which is used to manage the creation and modification of digital content.
The CMS is having two level of user role "Admin" and "User".

### User Credentials to check the API:
email: user1@gmail.com </br>
password: Pass@123

email:user2@gmail.com </br>
password: Pass@123

### URLs & Inputs for checking API:
1. Login api: </br>
   http://127.0.0.1:8000/api/auth/login/ </br>
   input: </br>
   { </br>
   "email":"user1@gmail.com", </br>
   "password":"Pass@123" </br>
   } </br>

2. Logout api: </br>
   http://127.0.0.1:8000/api/auth/logout/ </br>
   input: </br>
   { </br>
   "email":"user1@gmail.com" </br>
   } </br>
   
3. To view all the users: </br> 
   http://127.0.0.1:8000/api/contents/content-list </br> 
   
4. To view all the contents: </br> 
   http://127.0.0.1:8000/api/contents/content-list </br> 
   
5. To view details of a content: </br>
   http://127.0.0.1:8000/api/contents/content-detail/3 (pk) </br>
   
6. To create content: </br>
   http://127.0.0.1:8000/api/contents/content-create </br>
   input: </br>
   { </br>
   "id": 3, </br>
   "title": "Custom Notification Alert", </br>
   "body": "This is newly created content", </br>
   "summary": "newly created", </br>
   "attachment": null, </br>
   "categories": "Web", </br>
   "created_by": { </br>
               "email": "user3@gmail.com", </br>
               "password":"Pass@1234", </br>
               "first_name": "", </br>
               "last_name": "", </br>
               "profile": { </br>
                        "phone": "8286765000", </br>
                        "pincode": "600037", </br>
                        "roles": "Author", </br>
                        "photo": null </br>
                        } </br>
                } </br>
} </br>

7. To update content: </br>
   http://127.0.0.1:8000/api/contents/content-create/2 (pk) </br>
    input: </br>
    { </br>
    "id": 2, </br>
    "title": "Updated", </br>
    "body": "This is updated content", </br>
    "summary": "updated created", </br>
    "attachment": null, </br>
    "categories": "Web", </br>
    "created_by": { </br>
                "email": "user3@gmail.com", </br>
                "password":"Pass@1234", </br>
                "first_name": "", </br>
                "last_name": "", </br>
                "profile": { </br>
                          "phone": "8286765000", </br>
                          "pincode": "600037", </br>
                          "roles": "Author", </br>
                          "photo": null </br>
            } </br>
} </br>
} </br>

8. To delete content: </br>
   http://127.0.0.1:8000/api/contents/content-delete </br>
   
9. To search content: </br>
   http://127.0.0.1:8000/api/contents/content-search </br>
   
   
   
   
   
