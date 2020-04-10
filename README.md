# Django_jwt
   A django rest framework API with CRUD operations and JWT token authentication


## Steps to run the server:
1. Install all the requirements from the requirements.txt file by running the following command:
    - pip install requirements.txt
2. To run the server type the following command:
    - python manage.py runserver
 
 ## APIs documentation
 
 ### User Authorization Endpoints ( Using JWT token)
      It is better to check this on postman for better understanding
      
   <table>
    <tr>
        	<th>S.No.</th>
   		<th>Route</th>
   		<th>Method</th>
   		<th>Access</th>
   		<th>Description</th>
   	</tr>
   	<tr>
           <td>1.</td>
           <td>api/token/</td>
           <td>POST</td>
           <td>public</td>
           <td>Enter the credentials and you will get two tokens. Access and Refresh</td>
       </tr>    
    <tr>
           <td>2.</td>
           <td>api/token/refresh/</td>
           <td>POST</td>
           <td>private</td>
           <td>After the expiration, enter the refresh token in the body and you will get the new access token</td>
       </tr>      
  </table>
  
  
  
  ### CRUD Operations Endpoints
        This can be checked both in frontend as well as in Postman
   <table>
   	<tr>
   		<th>S.No.</th>
   		<th>Route</th>
   		<th>Method</th>
   		<th>Access</th>
   		<th>Description</th>
   	</tr>
   	<tr>
           <td>1.</td>
           <td>api/book/</td>
           <td>GET,POST</td>
           <td>private</td>
           <td>Gives a list of books and can also add them</td>
       </tr>
   	 <tr>
           <td>2.</td>
           <td>api/book/:book_id/</td>
           <td>GET</td>
           <td>private</td>
           <td>Get the details</td>
       </tr>
   	 <tr>
           <td>3.</td>
           <td>api/book/:book_id</td>
           <td>PUT</td>
           <td>private</td>
           <td>Edit the details</td>
       </tr>
     </table>
