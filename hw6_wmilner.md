Homework 6 Feedback
===================

Commit graded: 3901e5128314eaf209f76006a18c99939c27f2e6

### Committing your work (7/10)
  * **-3** Commits should represent complete, incremental changes in your solution. Make sure that you are committing often. 

### Specification fulfillment (5/20)
  * **-10** Stream refresh was not implemented in the global stream, meaning new posts are added dynamically every five seconds without refreshing the whole page.
  * **-5** Comments should be added via Ajax, meaning that the comments are added without the entire page refreshing.

### Validation (18/20)
  * **-2** Your application crashes when I press the comment button without having typed anything in. It should not allow empty comments, but still recover gracefully. 

### Coverage of technologies (24/50)
  * **-20** Stream refresh were not implemented, demonstration of related technologies (JavaScript and Ajax) were not adequately demonstrated.
  * **-3** Inappropriate relation between comments and posts. Comments have a many-to-one relationship to posts (many comments belong to one post and one post has many comments), meaning that this relationship should be represented by a ForeignKey on the comment model linking to the post.
  * **-3** A POST request would be better suited for adding comments. POST requests are expected to change state on the server, while GET requests are not supposed to modify server state.

### Design (0/0)
  * **-0** The manner of bringing up comments is somewhat un-intuitive. 

### Additional comments

---

#### Total score: 54

Late days used: 3

---

Graded by: Divya (dmouli@andrew.cmu.edu)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/wmilner/blob/grades/hw6_wmilner.md

