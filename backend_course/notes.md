# Playlist:
    https://www.youtube.com/playlist?list=PLN4aKSfpk8TTD3g83qIK4PiNsImxWK-6x
# Imp Lecture:
    https://www.youtube.com/watch?v=usqT1kMmDBg&list=PLN4aKSfpk8TTD3g83qIK4PiNsImxWK-6x&index=5  [REST APIs Theory]

### What happens when you type maps.google.com ?
- Checks browser cache
- Checks OS cache
- Checks Router cache
- Checks ISP cache
- With the IP, the browser initiates a TCP connection with the server
- The browser sends a request to the server(It is a web server)
- The server responds with the static contents(HTML, CSS, JS, images, json etc)
- The browser loads the HTML content.

### HTTP Methods
Get - Retrieve Information
HEAD - Retrieve Resource Headers
POST - Submit data to the server
PUT - save an object at the location OR Updating the entire data
PATCH - Used for partial update of data
DELETE - Delete the object at the location

### REST
Rest, Or Representational State Transfer is an architectural style for providing standards between computer systems on web, making it easier for systems to communicate with each other.
REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server.
- Its a way to design APIs
- There are some properties that APIs should follow inorder to become restful apis
- APIs tells you what is the request and corresponding response structure.

### REST Design Principles
Uniform Interface:
    - All API requests for the same resource should look the same, no matter where the request comes from. 
    - The REST API should ensure that the same piece of data, such as the name or email address of a user, belongs to only one uniform resource identifier(URI). 
    - Resources shouldn't be too large but should contain every piece of information that the client might need.
Server-client decoupling
Statelessness
Cacheability:
    - When possible, resources should be cacheable on the client or server side.
    - Server responses also need to contain information about whether caching is allowed for delivered resource.
    - The goal is to improve performance on the client side, while increasing scalability on the server side.
Layered System Architecture:
    - In REST APIs, the calls and responses go through different layers.
    - As a rule of thumb, don't assume that the client and server applications connect directly to each other.
    - There may be a number of different intermediaries in the communication loop.

### Separation of Client and Server
- In the REST architectural style, the implementation of the client and the implementation of the server can be done independently w/o each knowing about the other.
- This means that the code on the client side can be changed at any time w/o affecting the operation of server, and the code on the server side can be changed w/o affecting the operation of the client.
- As long as as each side knows what format of messages to send to the other, they can be kept modular and separate.
- Separating the user interface concerns from the data storage concerns, we improve the flexibility of the interface across platforms and improve scalability by simplifying the server components
- Additionally, the separation allows each component the ability to evolve independently
- By using a REST interface, different clients hit the same REST endpoints, perform the same actions, and receive the same responses.

### Statelessness
- Systems that follow the REST paradigms are stateless, meaning that the server does not need to know anything about what state the client is in and vice-versa
    - It does not store the last request from the user
    - It does not store any information about the previous requests(neither client nor server)
    - It only cares about the current request
- In this way, both the server and client can understand any messages received, even w/o seeing previous messages.
- The constraint of statelessness is enforced through the use of resources, rather than commands.
- Resources are the nouns of the Web- they describe any object, document, or thing that you may need to store or send to other services.
- Ques : Can we store session data ? How do we know if a user is logged in or not ?

### APIs
- APIs stands for Application Programming Interface.
- An API is a software intermediary that allows two applications to talk to each other.
- In other words, an API is the messenger that delivers your request to the provider that you are requesting it from and then delivers the response back to you.

### Creating Restful APIs Format
- <http_method>/pet/{petID}       Find pet by ID
Example:
- <GET>/pet/{petID}               Find pet by ID
- <PUT>/pet                       Update an existing pet
- <DELETE>/pet/{petID}            Deletes a pet
- <POST>/pet/{petID}/uploadImage  uploads an image

- These are the rest apis end point. So, by looking at the end-points people should be able to figure out what is the purpose of a that end-point.

### RESPONSE comes via REST APIs
- XML
- JSON (Used by majority)

### RESPONSE CODES
- 2xx : Successful
    - 200 : Success/OK
    - 201 : Created            [Resource is Created]
    - 204 : No Content         [When you do not want to send any content back to the user]
        - Request is successful, but there is no response i can send to you
- 4xx : Request Failed         [There is something wrong with the request that you are making]
    - 400 : Bad Request
        - Provided invalid data (like an invalid phone number)
    - 401 : Unauthorized
        - You are trying to make a purchase and you are not signed in
    - 403 : Forbidden
        - You are not allowed to access a particular resource. Like admins are allowed to success sth, while normal users are allowed to access sth else
    - 404 : Not Found
        - You provided a petID and pet for that ID does not exist
- 5xx : Server Failure         [There is some mistake on the server side]
    - 500 : Internal Server Error
    - 501 : Not Implemented
        - If you have not implemented a service
    - 502 : Bad Gateway
    - 503 : Service Unavailable
    - 504 : Gateway Timeout

### Check your understanding
- Added a user : 201
- Get a user : 200
- Delete a user : 204
- Update a user : 200            [Because you will send back the data of the updated user]
- Invalid mobile number : 400
- Invalid authentication token : 401    [ you are unauthorized]
- Divided by 0 at server : 500
- Get user for user id that is not present : 404

## Tools useful in writing APIs
### 1. Swagger    (swaggerhub.com)
- Documentation of the APIs
- What is the structure of the request ?
- What are the API end points, that are available ?
- What is the structure of the response ?
### 2. Postman
- How to test your APIs ?
    - Frontend might be created very late.
    - So, we need to test our API from the backend side. How we can do that ?
        - POSTMAN is used for that purpose
            - GET
            - https://api.github.com/users

## Alternatives to REST : GRAPHQL, SOAP, gRPC, FALCOR
- SOAP : obsolete
- gRPC : We will see later
### GRAPHQL (Graph Query Language)
- It allows client to define the structure of data required, and exactly same structure of data is returned from the server.
- Hence preventing excessively large amount of data from being returned.
- Analogy: You are in a restaurant
    - If you have a buffet service. Then it is kind of REST Service. Because all the dishes are present in front of you.And you are not allowed to choose. Waiter comes and serves you whatever he has. So, you are not allowed to choose, what you want.
    - Where as if you order, you get to choose what you want. (It is graphql)
- It is useful in the cases when there is lot of data. Example if facebook creates REST end points and in one request it returns all the data for the user, then it is too much. With graphql, depending on the page you are at, you can actually process the response that you want only this much information.