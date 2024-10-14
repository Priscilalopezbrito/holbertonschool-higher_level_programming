```mermaid
---
title: Class Diagram for Business Logic Layer
---
classDiagram

class BaseClass {
    + id: str
    + created: DateTime
    + updated: DateTime
}

class User {
   + firstName : str
   + lastName : str
   + email : str
   - password : str
   + typeOfUser: bool
    register()
    updateProfile()
    deleteProfile()
}
class Place {
   + title : str
   + description : str
   + price : float
   + latitude : float
   + longitude : float
  
   createPlace()
   updatePlace()
   deletePlace()
   listPlace()
}
class Review {
   + place : str
   + user : str
   + rating : float
   + comment : str
   createReview()
   updateReview()
   deleteReview()
   listReview()
  
}
class Amenity {
      + name : str
      + description : str
      createAmenity()
      updateAmenity()
      deleteAmenity()
      listAmenity()
}


   BaseClass --|> Amenity
   BaseClass --|> Place
   BaseClass --|> User
   BaseClass --|> Review
   
   %% Inheritance
   User --> Place : Owner
  
   %% Association
   User --> Review : User reviews
  
   %% Composition
   Place o-- Amenity : Has
  
   %% Association
   Place --> Review : Contains
