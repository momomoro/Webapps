Homework 5 Feedback
===================

Commit graded: c89ee39738a29b950537bbd79373f84a1f3b7f5c

### Committing your work (10/10)

  * **-0** Your commits could be much more granular and your messages more descriptive. For example, in [this commit], the message is 'updated edit feature' but it's unclear form that message *what* changes you made.

### Specification fulfillment (5/20)

  * **-5** User profiles do not contain all required pieces of information: first name, last name, age, bio.

  * **-5** Following/unfollowing was not completely implemented.

  * **-5** Users should be able to upload profile photos while editing their profile.

### Validation (20/20)

### Coverage of technologies (20/50)

  * **-10** Image upload was not implemented, so adequate use of dynamic image upload and display was not demonstrated.

  * **-10** Profiles with age/bio were not implemented, so adequate use of one-to-one relationships was not demonstrated.

  * **-10** Following was not implemented, so adequate use of many-to-many relationships was not demonstrated.

  * **-0** You should not be inheriting from the user class if you are using a OneToOneField for it. Not only does this mess with the migrations (I had some trouble getting your application to run), but it duplicates the feature of connecting users to profiles.

### Design (0/0)

  * You shouldn't have links to Profile and Logout if you are not already logged in; it's confusing.

### Additional comments

---

#### Total score: 55

Late days used: 3

---

Graded by: Shannon Lee (sjl1@andrew.cmu.edu)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/wmilner/blob/grades/hw5_wmilner.md
