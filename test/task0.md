```mermaid
---
title: High-Level Package Diagram
---
classDiagram
class PresentationLayer {
   <<Interface>>
   +Services
   +API
}
class BusinessLogicLayer {

   +User
   +Place
   +Review
   +Amenity
}
class PersistenceLayer {
   +DatabaseAccess
   +Repository
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
