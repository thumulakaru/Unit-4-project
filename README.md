# Unit 4 Project: Physics Questions Sharing Social Media
![DALLE-E Image](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/DALL%C2%B7E%20-%20an%20IB%20physics%20student%20trying%20to%20find%20questions%20oil%20painting.png)
[^1]

[^1]: "an IB physics student trying to find questions oil painting" by DALL E 2, Open AI,
Accessed 1st May 2023

## Criteria A: Planning


## Problem definition(Client identification)

I am a high school student living in Karuizawa. In our school a quarter of our grade takes physics in International Baccaulaurate Diploma Program(IBDP). Due to restrictions from the curriculum the students are having a hard time to find proper questions that are alligned with IB standards. And whenever the students share questions with each other using SNS like messenger or instagram it's really hard to revisit the same question again and to understand the questions content at a glance because of the unorganised manner.  Also it is really hard to filter out the good and bad questions and also to pass it down to our juniors. Also it is really hard to see old questions. Because of these issues a need was risen for a social networking system to share physics questions within ourselves. I would like to have different users who can post questions. It has to be secure and thoroughly organised.

## Proposed Solution
Considering the client's the requirements, an adequate solution would be a SNS that would take the style of social-media webstie. Though one of the most common programming tools to build a website is Javascript it's client sided language[^2] which poses a threat to the security of the website through the easy access to the loopholes which could potentially result in using them for malicious purposes. To avoid this python is a better alternative as it is not client sided, open source and extensive[^3]. To host the website Flask would be a great option as it is highly scalable and provides great control over the code[^4]. As for the database it is better to use a DBMS(Database Management System) which is better to run with smallto medium http requests as the the website is small-scaled. Thus, SQLite is a viable option as it excels at small-medium http reequests and also can run independently after installation[^5]. To interface with SQLite SQLAlchemy would be a one of the best options as it is a seamless integration with web aplications like Flask. Also because it uses eager loading the performance speed is increased[^6]. As for the user interface Bootstrap5 is a very viable option as it is compatible with many of the mordered browsers(Cross-browser compatibility)[^7]. To ensure the security of the website JWT tokens are an adequate solution as it is a client sided token which makes the servers run smoother[^8].

[^2]: “Why Use Javascript in 2022? 8 Disadvantages and Advantages of Javascript.” Tino Agency, https://tino.design/blog/14-why-use-javascript-in-2022-8-disadvantages-and-advantages-of-javascript.

[^3]: "Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June
2021, https://pythongeeks.org/advantages-disadvantages-of-python 

[^4]: “6 Reasons Why Flask Is Better Framework for Web Application Development.” Able, https://able.bio/hardikshah/6-reasons-why-flask-is-better-framework-for-web-application-development--cd398f73. 

[^5]: S, Ravikiran A. “What Is Sqlite? and When to Use It?” Simplilearn.com, Simplilearn, 16 Feb. 2023, https://www.simplilearn.com/tutorials/sql-tutorial/what-is-sqlite#:~:text=SQLite%20is%20used%20to%20develop,some%20data%20within%20an%20application. 

[^6]: Johnston, Paul. “10 Reasons to Love Sqlalchemy.” Blogs by Pajhome, https://pajhome.org.uk/blog/10_reasons_to_love_sqlalchemy.html. 

[^7]: Prabhu, John. “Why Should You Use Bootstrap?: Responsive Front-End Development.” Tech Blogs by TechAffinity, 4 Jan. 2023, https://techaffinity.com/blog/why-use-bootstrap-for-frontend-design/. 

[^8]: Nwokwo, Chisom. “Why Should You Use JWT's?” Educative, https://www.educative.io/answers/why-should-you-use-jwts. 

**Design statement**

I will design a social media platform using Bootstrap, HTML, CSS and Flask which will use a SQLite database to store data for my schoolmates. The website will allow everyone to post pysics questions and descriptions and like and dislike posts to moderate content. Necessary data will be hashed inorder to keep the database secure. It will take approximately 1 month to complete and the website will be evaluated according to the following criterias: 

## Success Criteria

1. The website must keep users separately with an encrypted login system.(Issue Tackled: "I would like to have different users who can post questions")
2. The website must allow posting of questions and viewing them.(Issue Tackled: "having a hard time to find proper questions" and "understand the questions content at a glance because of the unorganised manner")
3. The website must allow the user to like/dislike the posted questions to increase authenticity.(Issue Tackled: "filter out the good and bad questions")
4. The website will be able to sort the posts according to the number of likes and date posted.(Issue Tackled: "Also it is really hard to filter out the good and bad questions" and "it is really hard to see old questions")
5. The website will have a search function to search for posts.(Issue Tackled: "hard to revisit the same question again")
6. The website will allow users to change passwords.(Issue Tackled: "It has to be secure and thoroughly organised")

# Criteria B: Design


## System Diagram
![System Diagram](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/Sys_diag.png)

**Fig.2** *System diagram of Phy6hub*

## Data Storage
![ER Diagram](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/ER_diagram.png)

**Fig.2** *ER diagram of the Website


![users Data entry](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/users_data_entry.png)

**Fig.3** *Example data entry in the users table*

![posts Data Entry](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/posts_data_entry.png)

**Fig.4** *Example data entry in the posts table*

## UML Diagram
![UML Diagram](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/UML_diag.png)

**Fig.5** *UML Diagram of the website*

## Wireframe
![Wireframe Diagram](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/Wireframe_diag.jpg)

**Fig.6** *Wireframe of the website*

## Flow Diagrams

### Login System
![Flow Diagram for Login System](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/Login_system_flow_diag.png)

**Fig. 7** *Flow diagram of the login system. This flow diagran represents how the users are going to be logged in will be created a token to validate that they logged in properly. This makes sure that there is no unauthorised access.*

### Displaying Posts
![Flow Diagram for Displaying Posts](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/flow_diag_show_posts_flow_diag.png)

**Fig.8** *Flow diagram of the post displaying system. This is used to display posts in the dashboard according to what the user nededs at the moment.*

### Like/Dislike System
![Flow Diagram or the Like/Dislike System](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/like_or_dislike_flow_diag.png)

**Fig.9** *Flow Diagram of the like/dislike system. This summarises how the likes and dislikes system works.*


## Record of Tasks
| Task No  | Planned Action  | Planned Outcome | Time estimate  | Target completion date  | Criterion |
|:----------|:-------------------------|:----------|:----------|:----------|:----------|
| 1   | Development: Coding the login page |  Get a specific design for the login page   | 30 mins  | 2023.03.31    | C    |
| 2   | Development: Write the code to get dat from login screen    | Get data through the data   | 1 hr  | 2023.04.01    | C    |
| 3   | Planning: Write the problem definition    | Have a clear and direct problem definition   | 30 mins   | 2023.04.03   | A   |
| 4   | Design: Drawing ER diagrams  | Have a clear idea of how the database would look like   | 10 mins  | 2023.04.04    | B |
| 5   | Design: Drawing  Wirefram Diagram  | Have a clear idea of the structure of the website | 40 mins  | 2023.04.05    | B  | 
| 6   | Design: Researching SQLAlchemy    | Use good coding practices when coding   | 2 hrs | 2023.04.06    | B   |
| 7 | Design: Designing the flowchart for the liking system    |  Have a clear understanding of how the likes system work  | 20 mins   | 2023.04.07    | B  |
| 8 | Planning: Writing the problem definiton | Give more context to the need | 30 mins  | 2023.04.08    | A   |
| 9 | Planning: Write down the success criteria | Have more written context to what is going to be developed  | 30 mins  | 2023.04.09    | A  |
| 10 | Development: Coding the registration page | have a design for the registration page | 30 mins | 2023.04.10 | C |
| 11 | Development: Finalising a theme for the pages and applying them| Have consistency throughout the website | 2 hrs | 2023.04.11 | C|
| 12 | Development: Code the header and footer | Have a finished footer and header | 1 hr | 2023.04.12 | C|
| 13 | Development: Start writing the rationale for the proposed solution | Give more context on why certain tools are used | 30 mins | 2023.04.13 | A|
| 14 | Development: Did research about JSON tokens | Have a proper understanding about JSON tokens before using them in the code  | 4 | 2023.04.14 | C|
| 15 | Development: Writing the base functions for the database | Have a database handler that can be called | 30 mins | 2023.04.15 | C|
| 16 | Development: Started coding the SQLAlchemy part for user validation | Have a completed user validation | 30 mins | 2023.04.16 | C|
| 17 | Development: Code a template for the questions to be posted | Have a template for the questions to be displayed | 1 hr | 2023.04.17 | C|
| 18 | Development: Started working on new post entry page | Have a new post entry page | 30 mins | 2023.04.18 | C|
| 19 | Development: Did research on how search bars work in a database | Have a clear idea on how to make the searcg function | 30 mins | 2023.04.19 | C|
| 20 | Development: Started working on the profile page | Make some progress on this page | 1 hr | 2023.04.20 | C|
| 21 | Development: Finished coding the search function from the database | Have a working search function | 20 mins | 2023.04.21 | C|
| 22 | Development: Finished coding the valiidation function | Have a validation functions for email, title and content inputs | 30 mins | 2023.04.22 | C|
| 23 | Development: Start working on the JSON token validation | Have a base function that will be able to encrypt the user details and use it | 1 hr | 2023.04.23 | C|
| 24 | Development: Applied JSON tokens to the flask app| Secure the website when it is necessary | 1 hr | 2023.04.24 | C|
| 25 | Development: Debugging the Database Handler | Reduce the bugs in the program | 2 hrs | 2023.04.25 | C|
| 26 | Development: Worked on the sort function | Partially finish the sorting function | 1 hr | 2023.04.26 | C|
| 27 | Development: Finished the sort function | Have a function that is able to sort the posts according specific criterias | 1 hr | 2023.04.27 | C|
| 28 | Development: Finished coding the password change page | Have a completed web page for the password change  | 2 hrs | 2023.04.28 | C|
| 29 | Development: Finished database code for password change | Have a finished a function to change passwords| 30 mins | 2023.04.29 | C|
| 30 | Development: Cleaning up the code | To have the code finalised and easy to understand | 4 | 2023.04.30 | C|
| 31 | Implementation: Evaluation by the client | To have the website evaluated by the client and the relevant evidence documented | 1 hr | 2023.05.07 | E|
| 32 | Beta Testing: Evaluation by a peer | To have the website evaluated by a peer and the relevant evidence documented | 1 hr | 2023.05.07 | E|



## Test Plan

| Type | Description | Process | Anticipated Outcome |
| ---- | ----------- | ------- | ------------------- |
|   Unit Testing   |   User Registration   |   1.Open Website<br> 2.Click on the register button <br>3.Put "bob" as the username, bob@gmail.com as the email and "bob@1234" for both password fields <br>4. Click the register button on the screen.                                                   |The user should be redirected into the login page with a flash message stating that the user has been registered successfully.    |
|   Unit Testing   | User Login            | 1.Open Website<br />2. Put "bob" as the username and "bob@1234" as the password<br />3. Click the login button on the login card                                                                                                                                        | The user should be redirected to the dashboard page of the page if the user exists and the password matches the hash in the database.                                                                            
|   Unit Testing   | User Logout                 | 1.Open Website and login using the above credentials <br> 2. Click the logout button in the top bar of the dashboard                                                                                                                                | The user should be redirected to the dashboard page of the page if the user exists and the password matches the hash in the database.                                                                            
| Integration Testing  | Login and Registration     | 1.Open Webiste<br />2.Follow the above instuctions for registering a new user. <br />3.Follow the instruction and login to the website properly. <br />                                                                                     | If the user followed the instructions properly and registered for a user, they should be able to login to the website without a problem                                    | 
| Unit Testing         | Changing Password          | 1.Open Website and login with the instructions given above<br/> 2. Click the button "my profile" in the header<br />3. Inpute the previous password in the relevant field and enter "changeme1" into both the new password and confirm new passwords sections.<br />4. Input the current password of the current user and put "changeme" for new and confirm password. <br />5. Click Confirm                          | If the user followed the instructions properly and no errors were displayed in the page during the process, the user should be able to logout and log back into the same user with the same username but with password "changeme". |
| Unit Testing         | Adding new post            | 1.Open Website and login using the above credentials. <br />2.Click New Post on the header in the dashboard. <br />3. Put in "My first question" as the Title, "State the 2nd law of Newton" as the Content.<br />4.Click the submit button | If there were no errors shown in the web page the user should be redirected to the dashboard, where they can see all of their posts which will include the one that they just posted.                                                                                 |
| Unit Testing         | Like/Dislike a post        | 1.Open Website and login with the instructions given above.<br />2.Click on the like button of a post<br />4.Click on the dislike button of another post                                                                                                                                                     | The user should be able to see the like count of the post increase by 1 for the first post and decrease by 1 for the second one.                                                                                 |
| Intergration Testing | Adding Post / Viewing Post | 1.Open Website and login using the above instructions. <br />2.Create a new post following the instructions above<br />4.Click the home button.                                                                                                                                                           | The user should be able to see the post they just created on the top of the dashboard.|
| Unit Testing         | Sorting System by like/posted time             | 1.Open Website and login using the above instructions. <br />2. Click the sort by likes button. <br/>3. Click the sort by date button.|                                                                                                                                                       | The user should be able to see posts sorted by the highest like count after the 2nd step and after the 3rd step they should be able to see the oldest post first and the latest post by the end.
| Unit Testing	        | Search system | 1. Open website and login using the above instrutions.<br/> 2. Enter a new post using the instructions giving <br/>3. Click on the search bar and enter "My first question" and press the "enter" button on the keyboard. | The user should be able to see a question |                                                                                                                         
| Code Review          | Reviewing Code             | Going through the code and making sure unused parts are removed, variables are named properly and comments are placed appropriated                                                                                                                                           | Easy to understand and easy to debug code for future development.                                                                                                                                                
                                                           

# Criteria C: Development

## Existing Tools

| Libraries    |
| ------------ |
| Datetime     |
| Flask        |
| Jinja2       |
| Passlib.hash |
| dotenv       |
| Sqlalchemy   |

## References

### [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

Bootstrap 5's official documentation is what I referenced many of my ui elements. Snippets of code for cards, headers, buttons, text, icons and footer has been taken from this and was modified to fit the UI design.


### [ChatGPT](chat.openai.com)

ChatGPT is a large language model developed by OpenAI, based on the GPT (Generative Pre-trained Transformer) architecture. It helped me with understaing the logic behind certain parts of codes and formulate sentences to communicate certain messages to the user better.

***Disclaimer*** *No part of this program include code blocks directly copied from ChatGPT*


### [Tabnine AI Code completion](https://www.tabnine.com/)

Tabnine is an AI code assistant. Tabnine is powered by multiple language-specialized machine learning models that were pre-trained from the ground up on code. This helped to me improve the speed of my programming by giving me predictions for variable names, recalling a variable in the same programme etc.

***Disclaimer*** *No part of this program include code blocks directly generated by Tabnine*

### [Codepen](https://codepen.io/)

CodePen is a social development environment for front-end designers and developers. Build and deploy a website, show off your work, build test cases to learn and debug, and find inspiration.

***Disclaimer**** *Only the forms were inspired by Codepen*

## List of techniques used

1. Object-Oriented Programming(OOP)
2. Object Relation Mapping(ORM): SQLAlchemy
3. Flask Library/Routes
4. Javascript/Python inside HTML
5. CSS Styling
6. For loops to display posts
7. if statements
8. Password Hashing
9. Token-based authentication
10. Interacting with Databases(SQLAlchemy to SQLite3 databases)
11. Arrays and Lists
12. Text Formatting
13. DRY Programming Technique

## Development

### Containers

After inspecting many social media pages and after some discussions with my peers I was able to figure out that it is very easy to develop forms using containers for taking user inputs. Thus, I decided to use containers when I was using forms which were placed in login, registration and new post pages. Here is a snippet of the code.

```html
<form style="border:1px solid #ccc" method="post">
	<div class="container">
	{# Code of the sign in fields inside the card is omitted for demonstration puposes#}
	</div>
</form>
	
```

![Login page Container](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/login_container.png)

**Fig.10** *This is the above mentioned "containers". All the elements are displayed are placed inside a container.*

### JSON tokens(Success Criteria #1)

One of the success criterias was to have an encrypted login system. The issue with using cookies for me was that I could not store the username nor the user id without it being open to threats like the user modifying them through various methods. My classmates(Bernard-LTW and Alsa2) introduced me to this session tokens. They could contain details and would expire after the session ends which the developer is able to specify. These tokens are able to protect the user details as it is hashed using a special secret key that the only the developer has the control to change. The first edition of this website creates a token when a user successfully logged in the flask endpoint executes a function named `generate_token` from the file `token_manager.py`.
```py
# This function creates a session token for a given duration and stores an encrypted version of the username
def generate_token(username, token_duration): # token duration should be in minutes
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    ttl = token_duration * 60 + unix_timestamp
    token = jwt.encode({'username': username, 'datetime': ttl}, token_encryption_key, algorithm='HS256')
    return token
```

After the above code returns the generated token it is stored into the session variable and returned to the user.
```py
session['token'] = create_token(username, 120)
```

Since the user has the token in their browser it is called in the flask endpoint to get the username of the current user to do necessary actions.

```py
@app.route("/new_post", methods=['GET', 'POST'])
def new_post():
    try:
        token = session['token']
    except KeyError:
        return redirect(url_for('login'))
     #Continues function
```

In the above code I used python built-in function `try` and `KeyError`to check if the user got the token because if it is not it would return a keyerror and redirect the user to the login page. After that using the JWT2 library the token is checked if the session has not expired yet.

```py
def check_token(token): #check if token is valid and not expired
    try:
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
        current_time = datetime.utcnow().timestamp()
        if decoded_token['datetime'] < current_time:
            return False
        else:
            return True
    except Exception:
        return False
```

The main function then recieves a boolean value of whether the user is in a valid session and will allow if they are to do the action. This system closes the loophole of modifying cookies and completes the hashed authentication system criteria.

### Header and Footers

To have a consistent UI design in the webpage to make it easier for the user to navigate through the webpage I decided to use the `header` and `footer` tags of HTML5. This also makes it easier for the user to navigate through the website due to its consistent design.

```.html
<header class="p-3 mb-3 border-bottom fixed-top" style="width: 100%; display: flex; justify-content: space-between; background-color: #000000;">
  <div class="d-flex align-items-center">
    <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 link-body-emphasis text-decoration-none">
      <img src="https://icons.veryicon.com/png/o/education-technology/educational-icon/physics-4.png" alt="" width="100" height="100">
        <h1  class="ms-3 mb-0" style="color:#FFFFFF;">Phy6hub</h1><h4 style="color:#FFFFFF";>Connect with the cosmos</h4>
    </a>
  </div>
  <div class="d-flex align-items-center">
    <ul class="nav me-3">
      <li class="nav-item">
        <a class="nav-link link-secondary" href="/dashboard"><img src="../static/home_icon.png"></a>
      </li>
        <li class="nav-item">
        <a class="nav-link link-body-emphasis" href="/my_profile"> <img src="../static/profile_icon.png"></a>
      </li>
    </ul>
    <div class="d-flex" style = "padding-right: 30px">
     <a href = "/new_post"><button type="button" class="btn btn-primary me-2 btn-lg" style="background-color: #39FF14; border: #39FF14">New Post</button></a>
        <a href="/logout"><button type="button" class="btn btn-danger btn-lg">Logout</button></a>
    </div>
  </div>
</header>
```

As you can see from the above code I have used the `<header>` tag which includes icons and buttons for actions like logout, create a new post. Here's an image of how it looks like when running.

![Image of Header](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/header.png)

**Fig.11** *This is the above mentioned header. All the icons in this are linked to a webpage*

### Base Template(Pattern Recogniton, Abstraction)

As I mentioned above the header and footer needs to be present in many of the web pages. But adding this entire piece of code again and again to every single web page makes my code very repitetive and very lengthy. Thus, I was inspired by one of my classmate's solution for this which was using a base template. This template file will be the only file that includes the header and footer. The way I decided to design this file was to start off as a normal html file and the in the `<body>` I added a piece of Jinja code to import the elements from other html files.

```.html
{% block content%}{% endblock %}
```

This creates an empty space that is able to have html code inside. Using this I only have to extend the base template to the necessary html file and define the `block` which are the elements that needs to be shown in the webpage.


Here's the code for extending the base template.
```.html
{% extends "base_template.html" %}
```

Here's the code for defining the block in the necessary html file.
```.html
{% block content%}
{# HTML code is omitted due to length#}
{% endblock %}
```

When this file is load into the browser the variables in the file and the base template are put together and displayed.

### Post insert and representation(Succes Criteria #2)
The client requires to insert the posts and display the posts. To insert a new post I used a simple form embedded with basic valdation. The data is then inserted into a databaase. Which in intself are very easy tasks. Here is an image of the form that I used to collect the data. 

![Post insert form](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/new_entry.png)

**Fig.12** *This is the form that is ued to input the data into the form.*

The harder part of this client requirement was to display the posts as they needed to be repeateted infinitely depending on the number of posts. Thus, including the same piece of code many times I decided to use `jijna2` extension for `html`and repeat an array given to the website. The given posts array is run through `{% for post in posts %}` to get each element inside the array. Here is the full code that I used to represent all the posts that was entered to the database.

```.html
{% for post in posts %}
		<div class="post">
            <div class="title" style="color: white">{{ post.title }}</div>
			<div class="user_and_datetime" style="color: white">Posted by {{ post.user }} at {{ post.time }}</div>
			<div class="content" style="color: white">{{ post.content }}</div>
			<a href="/add_attract/{{post.id}}"><button formmethod="get" class="btn btn-outline-success btn-sm w-auto">Attract</button></a>
			<span class="badge bg-secondary">{{ post.likes }}</span>
            <a href="/add_repel/{{post.id}}"><button formmethod="get" class="btn btn-outline-danger btn-sm w-auto">Repel</button></a>
		</div>
    {% endfor %}
```
Also in the above code I used OOP(Object Oriented Programming) to make it easier for further development of the website as it is easy to understand for the developer.

Here is an image of what the final output looks like:

![Post Image](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/post_image.png)

**Fig.13** *This is the post that user would see. The two posts are taken from the database.*


### Like/Dislike System(Success Criteria #3)
The client also required to have a way to sort the questions with how helpful they are. To implement this I decided to add a like/dislike system to the posts. Each post in the database have a like counter and when the like/dislike button is clicked the database gets updated. And thrugh this the new like count is displayed with a reload of the page.

This is the code for the like/dislike system in the webpage.

```.html
<p style="color: white"> <i>What should we do to this question's velocity towards the IB students?</i></p>
            <a href="/add_accl/{{post.id}}"><button formmethod="get" class="btn btn-outline-success btn-sm w-auto">Accelerate</button></a>
			<span class="badge bg-secondary">{{ post.likes }}</span>
            <a href="/add_dece/{{post.id}}"><button formmethod="get" class="btn btn-outline-danger btn-sm w-auto">Decelerate</button></a>
```

### Sorting System(Success Criteria #4)
The client wanted a way to revisit the past questions and good questions easier. Thus, I decided to add a sorting system. And the posts are sorted using the date posted and the number of likes. To do this I created an algorithm that sorts the posts out and that algorithm is combined with the sorting function for the search function in success criteria #5. The reason for this is that both of them were quite similar to each other and rather than running multiple functions to output the posts I just combined them. This is one of the main ocassions that I used the DRY principal as I avoided a part where it was possible to repeat.

The algorithm for this is the function,`search_posts_by_x()` in the `db_handler.py`. The algorithm is quite simple. In the website there's two buttons to either sort by date or likes and to remove the sort filter. The code to get the user option is as follows:
```.html
@app.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        token = session["token"]
        username = get_username_from_token(token)
        # Defining the variable 'sort_by' 
        sort_by = request.args.get('sort_by', default="", type=str)
        # Run only when the user is given an input
        if request.method == "GET":
            search_in = request.args.get("search")
            # To avoid running into an error when querying
            if search_in is None:
                # To avoid running into an error when querying
                search_in = ""
            posts = db.search_posts_by_x(sort_by, search_in)
            return render_template("post_template.html",username = username, posts = posts)

    except KeyError:
        flash(("User timed out. Please try again", "danger"))
        return redirect(url_for("login"))
```

As you can see in the above piece of code the `sort_by` variable is defaultly set to empty so that all the posts will be displayed from newest first. If the user were to select one of the sorting options the `sort_by` variable have a value of either `"like"` or `"time"` which is given as an input to the function `search_posts_by_x()` in the `db_manager.py` file. The function is as shown below:

```.py
    def search_posts_by_x(self, sort_by_feature, query):
        # For search function
        all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).all()
        
        # Beginning of sort function
        if sort_by_feature == "":
			# The filter function had to be used to avoid an error
            all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).all()

        elif sort_by_feature == "like":
            all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).order_by(posts.likes.desc()).all()

        elif sort_by_feature == "time":
            all_posts = self.session.query(posts).filter(posts.title.like("%" + query + "%" )).order_by(posts.likes).order_by(posts.datetime).all()

        # To read the datetime and convert it to a different format for the user to view
        for post in all_posts:
            user = self.session.query(users).filter_by(id=post.user_id).first()
            timestamp = datetime.datetime.fromtimestamp(post.datetime)
            post.time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            post.user = user.username
        return all_posts
```

### Search Function(Success Criteria #5)

One of the other requirements of the client was to easily find the same post that they viewed earlier for which I decided to add a search function to the webpage. And for this I used the same function as last time which was `search_posts_by_x` located in the `db_handler.py`.

The function takes the input from the user through the website using a `GET` request. And that input is run through the database and checks for similar titles. Which will then be outputted after a little processing.

I used a form with the `GET` method to get this input. Bootstrap was used in the process to make it visually more appealing. The code for that as follows:
```.html
<div class="input-group rounded">
                <form method="get">
                  <input type="search" class="form-control bg-dark text-white" placeholder="Search" aria-describedby="search-addon" name = "search"/>
                    <button><i class="bi bi-search"></i></button>
                </form>
            </div>
```

The algorithm for this is given in the Success Criteria #4 description above. As a programmer I do not want to repeat myself thus, I won't be including it here.

### Change Password(Success Crieteria #6)

FInally my client also wanted to have the option to change the password. To achieve this I created a change password function that is able to change the password when the old and new passwords are given. The function is implemented `/change_password` endpoint in the `app.py` file.

The data taken from the webpage is validated and since it is not repetetitive I coded it directly into the endpoint file. Here is the validation that it is run through(The else sentences are ommitted to shorten the length of the code):
```.py
                if check_password(old_pw, user.password):
                    if validate_password(new_pw_1):
                        if new_pw_1 == new_pw_2:
                            temp_pass = hash_password(new_pw_1)
                            db.change_password(username, temp_pass)
                            flash(("Password changed successfully", "success"))
                            return redirect(url_for("dashboard"))
```

After the validation the data is put to the database function. Which is as follows:
```.py
    def change_pswd(self, username, new_pwd):
        user = self.get_user(username)
        user.password = new_pwd
        self.session.commit()
```

### Initialising Database and Inserting Dummy Data

Throughout the development cycle inserting dummy data is an important part as it helps me(the developer) to get check if the functions are working properly by predicting an output. Thus, I initialised the database and added dummy data so that I would be able to predict certian outputs.
Here is the code for the inserting dummy data:
```.py
from db_handler import database_handler as dbh
from db_handler import create_base
from password_handler import hash_password
from models import users, posts
from sqlalchemy.orm import Session


db = dbh("networking.db")
create_base()


def dummy_insert_user():
    unames = ["alice123", "bob123"]
    emails = ["alice@example.com", "bob@example.com"]
    passwords = ["alice123", "bob123"]
    for uname, password, email in zip(unames, passwords, emails):  # Zip function is used to iterate the data
        new_user = users(username=uname, password=hash_password(password), email=email)
        db.session.add(new_user)
    db.session.commit()


def dummy_insert_post():
    titles = ["First Post", "Second Post"]
    contents = ["What is the basis of Physics?", "Who is the father of the Physics?"]
    user_ids = [2, 3]
    times = [1683100545.492104, 1683100565.254593]
    for title, content, user_id, time in zip(titles, contents, user_ids, times):
        new_post = posts(title=title, content=content, user_id=user_id, likes=0, datetime=time)
        db.session.add(new_post)
    db.session.commit()


dummy_insert_user()
dummy_insert_post()
``` 
The above function creates two users and two posts which makes it easier for me to test my code in later stages. This also reduced the time that I have to spend manually adding data to see if my ccode works properly.


# Criteria D: Functionality

## Demonstration Video

[Click here for the Video]()

# Criteria E: Evaluation

## Evaluation by the client

| Success Criteria                                                                                                                          | Met? | Description                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------|------|-----------------------------------------------------------------------------------------------------------------|
| The website must keep users separately with an encrypted login system.| Yes  | Users are seperated using a hashed system and a token system.                                                |
| The website must allow posting of questions and viewing them. | Yes  | A user is able to post a new post via the endpoint, `/new_post`. |
| The website must allow the user to like/dislike the posted questions to increase authenticity.                                                                                    | Yes  | The website allows users to like and dislike via `/add_accl/` and `/add_dece/` endpoints.                                        |
| The website will be able to sort the posts according to the number of likes and date posted.| Yes  | The website allows the user to sort posts by time and likes in the `/dashboard` endpoint.|
| The website will have a search function to search for post.| Yes  | Users are able to search in the endpoint, `dashboard`.|
| The website will allow users to change passwords.| Yes  | The website allows the user to change their password at the `/change_password` endpoint. |

## Evaluation by Peer



## Extensibility

The client was very satisfied with the final result. After some discussion with the client it was concluded that the following extensions could be added in the future:

1. Prediction System for the search bar - A prediction system will be added based on the previous inputs of the user and by querying the database to make the search process smooth. This could be easily done with easily adding a new table in the database. 

2. Commenting System - A commeting system is to be added to give more freedom for everyone to discuss their opinions about question and to post the answers. Another table in the database could easily do this.

# Appendix

![Client-Developer agreement](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/success_criteria_approval.png)

**Appendix.1** *Client and the Developer agreeing to the success criteria*

![Client Evalutation Image](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/client_eval.png)

**Appendix.2** *Client evaluation of the website after depolying*

![Peer Evalutation image](https://github.com/thumulakaru/Unit-4-project/blob/main/assets/peer%20eval.png)

**Appendix.3** *Peer evaluation of the website after depolying*
