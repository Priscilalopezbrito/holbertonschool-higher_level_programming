```mermaid
---
title: Sequence Diagrams for API Calls
---
sequenceDiagram
   actor User
   participant PresentationLayer
   participant BusinessLogicLayer
   participant PersistenceLayer


   %% User
   User->>PresentationLayer: Register User
   PresentationLayer->>BusinessLogicLayer: Validate and Save User
   BusinessLogicLayer->>PersistenceLayer: Save User
   PersistenceLayer-->>BusinessLogicLayer: Success
   BusinessLogicLayer-->>PresentationLayer: Success
   PresentationLayer-->>User: User Registered


   %% Place
   User->>PresentationLayer: Create Place
   PresentationLayer->>BusinessLogicLayer: Validate and Save Place
   BusinessLogicLayer->>PersistenceLayer: Save Place
   PersistenceLayer-->>BusinessLogicLayer: Success
   BusinessLogicLayer-->>PresentationLayer: Success
   PresentationLayer-->>User: Place Created


   %% Review
   User->>PresentationLayer: Submit Review
   PresentationLayer->>BusinessLogicLayer: Validate and Save Review
   BusinessLogicLayer->>PersistenceLayer: Save Review
   PersistenceLayer-->>BusinessLogicLayer: Success
   BusinessLogicLayer-->>PresentationLayer: Success
   PresentationLayer-->>User: Review Submitted


   %% Fetch List of Places
   User->>PresentationLayer: Fetch Places
   PresentationLayer->>BusinessLogicLayer: Retrieve places
   BusinessLogicLayer->>PersistenceLayer: Fetch Places
   PersistenceLayer-->>BusinessLogicLayer: Return Places
   BusinessLogicLayer-->>PresentationLayer: Success
   PresentationLayer-->>User: List of Places
