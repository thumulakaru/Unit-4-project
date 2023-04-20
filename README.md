# Unit 4 Project: Physics Questions Sharing Social Media

## Criteria A: Planning

## Problem definition(Client identification)

I am a high school student living in Karuizawa. In our school quarter of our grade takes physics in International Baccaulaurate Diploma Program(IBDP). Due to restrictions from the curriculum the students are having a hard time to find proper questions that are alligned with IB standards. And whenever the students share questions with each other using SNS like messenger or instagram it's really hard to revisit the same question again and also to pass it down to our juniors. Because of these issues a need was risen for a social networking system to share physics questions within ourselves.

## Proposed Solution
Considering the client's the requirements, an adequate solution would be a SNS that would take the style of social-media webstie. Though one of the most common programming tools to build a website is Javascript it's client sided language[^2] which poses a threat to the security of the website through the easy access to the loopholes which could potentially result in using them for malicious purposes. To avoid this python is a better alternative as it is not client sided, open source and extensive[^3].

[^2]: “Why Use Javascript in 2022? 8 Disadvantages and Advantages of Javascript.” Tino Agency, https://tino.design/blog/14-why-use-javascript-in-2022-8-disadvantages-and-advantages-of-javascript.

[^3]:  

**Design statement**

I will design a social media platform using Bootstrap, HTML, CSS and Flask which will use a SQLite database to store data for my schoolmates. The website will allow everyone to post pysics questions and descriptions and like and dislike posts to moderate content. Necessary data will be hashed inorder to keep the database secure. It will take approximately 1 month to complete and the website will be evaluated according to the following criterias: 

## Success Criteria

1. The website must keep users separately with an encrypted login system.
2. The website must allow posting of questions.
3. The website must allow to like the posted questions to increase authenticity.
4. The website will be able to sort the posts according to the number of likes and date posted.
5. The website will have a search function to search for post.
6. The website will allow users to change passwords.

# Criteria B: Design
| Task No  | Planned Action  | Planned Outcome | Time estimate  | Target completion date  | Criterion |
|:----------|:-------------------------|:----------|:----------|:----------|:----------|
| 1   | Coding the login page |  Get a specific design for the login page   | 30 mins  | 2023.03.31    | C    |
| 2   | Write the code to get dat from login screen    | Get data through the data   | 1 hr  | 2023.04.01    | C    |
| 3   | Write the problem definition    | Have a clear and direct problem definition   | 30 mins   | 2023.04.03   | A   |
| 4   |   Drawing ER diagrams  | Have a clear idea of how the database would look like   | 10 mins  | 2023.04.04    | B |
| 5   | Drawing  Wirefram Diagram  | Have a clear idea of the structure of the website | 40 mins  | 2023.04.05    | B  | 
| 6   | Studying SQLAlchemy    | Use good coding practices when coding   | 2 hrs | 2023.04.06    | C   |
| 7 | Designing the flowchart for the liking system    |  Have a clear understanding of how the likes system work  | 20 mins   | 2023.04.07    | B  |
| 8 | Writing the problem definiton | Give more context to the need | 30 mins  | 2023.04.08    | A   |
| 9 | Write down the success criteria | Have more written context to what is going to be developed  | 30 mins  | 2023.04.09    | A  |
| 10 | Coding the registration page | have a design for the registration page | 30 mins | 2023.04.10 | C |
| 11 | Finalising a theme for the pages and applying them| Have consistency throughout the website | 2 hrs | 2023.04.11 | C|
| 12 | Code the header and footer | Have a finished footer and header | 1 hr | 2023.04.12 | C|
| 13 | Start writing the rationale for the proposed solution | Give more context on why certain tools are used | 30 mins | 2023.04.13 | A|
| 14 | Did some research about JSON tokens | Have a proper understanding about JSON tokens before using them in the code  | 4 | 2023.04.14 | C|
| 15 | Writing the base functions for the database | Have a database handler that can be called | 30 mins | 2023.04.15 | C|
| 16 | Started coding the SQLAlchemy part for user validation | Have a completed user validation | 30 mins | 2023.04.16 | C|
| 17 | Design a template for the questions to be posted | Have a template for the questions to be displayed | 1 hr | 2023.04.17 | C|
| 18 | Started working on new post entry page | Have a new post entry page | 30 mins | 2023.04.18 | C|
| 19 | Did research on how search bars work in a database | Have a clear idea on how to make the searcg function | 30 mins | 2023.04.19 | C|
| 20 | Started working on the profile page | Make some progress on this page | 1 hr | 2023.04.20 | C|
| 21 | 2 | 3 | 4 | 2023.04.21 | 6|
| 1 | 2 | 3 | 4 | 2023.04.22 | 6|
| 1 | 2 | 3 | 4 | 2023.04.23 | 6|
| 1 | 2 | 3 | 4 | 2023.04.24 | 6|
| 1 | 2 | 3 | 4 | 2023.04.25 | 6|
| 1 | 2 | 3 | 4 | 2023.04.26 | 6|
| 1 | 2 | 3 | 4 | 2023.04.27 | 6|
| 1 | 2 | 3 | 4 | 2023.04.28 | 6|
| 1 | 2 | 3 | 4 | 2023.04.29 | 6|
| 1 | 2 | 3 | 4 | 2023.04.30 | 6|
| 1 | 2 | 3 | 4 | 2023.05.01 | 6|
| 1 | 2 | 3 | 4 | 2023.05.02 | 6|
| 1 | 2 | 3 | 4 | 2023.05.03 | 6|
| 1 | 2 | 3 | 4 | 2023.05.04 | 6|
| 1 | 2 | 3 | 4 | 2023.05.05 | 6|
| 1 | 2 | 3 | 4 | 2023.05.06 | 6|
| 1 | 2 | 3 | 4 | 2023.05.07 | 6|
| 1 | 2 | 3 | 4 | 2023.05.08 | 6|
| 1 | 2 | 3 | 4 | 2023.05.09 | 6|
| 1 | 2 | 3 | 4 | 2023.05.10 | 6|
| 1 | 2 | 3 | 4 | 2023.05.11 | 6|


## System Diagram

**Fig.1** *System diagram of the Japanese Vocab Revision App*

## Data Storage

**Fig.2** *ER diagram of the Website

## UML Diagram

**Fig.3** *UML Diagram of the website

## Wireframe

**Fig.4** *Wireframe of the website*

## Record of Tasks

| Task No | Planned Action | Planned Outcome | Time estimate | Target completion date | Criterion |
| ------- | -------------- | --------------- | ------------- | ---------------------- | --------- |
| 1       |                |                 | 1 hr          |                        | A         |

## Flow Diagrams



## Test Plan

| Type | Description | Process | Anticipated Outcome |
| ---- | ----------- | ------- | ------------------- |
|      |             |         |                     |

# Criteria C: Development

## Existing Tools

| Software/Development Tools | Coding Structure Tools | Libraries |
| -------------------------- | ---------------------- | --------- |
|                            |                        |           |

## List of techniques used

1. THe hell

## Computational Thinking

#### Decomposition

In computational thinking, decomposition refers to breaking a complex problem or system into parts that are easier to
conceive, understand, program, and maintain.

#### Pattern recognition, generalization and abstraction

#### Algorithms

An algorithm is a step-by-step procedure for solving a problem or performing a task. Development

# Criteria D: Functionality

## Demonstration Video

[Click here for the Video]()

# Appendix
