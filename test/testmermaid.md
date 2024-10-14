```mermaid

classDiagram
  class WebShopping {
    <<package>>
  }

  class MobileShopping {
    <<package>>
  }

  class PhoneShopping {
    <<package>>
  }

  class MailShopping {
    <<package>>
  }

  class Payment {
    <<use>>
  }

  class ShoppingCart {
    <<access>>
  }

  class Customer {
    <<import public>>
  }

  class Inventory {
    <<import public>>
  }

  %% Package Merges
  WebShopping --> Payment : <<use>>
  MobileShopping --> Payment : <<use>>
  PhoneShopping --> Payment : <<use>>
  MailShopping --> Payment : <<use>>
  Payment --> ShoppingCart : <<access>>

  %% Imports
  Payment --> Customer : <<import private>>
  ShoppingCart --> Inventory : <<import public>>
  ShoppingCart --> Customer : <<import public>>

  %% Package Merges
  WebShopping <|-- MobileShopping : <<merge>>
  WebShopping <|-- PhoneShopping : <<merge>>
  WebShopping <|-- MailShopping : <<merge>>