# Created by aaronbrn at 19/06/23
Feature: Login Debrif
  # Enter feature description here

  Scenario Outline: Login Debrif
    Given Launch Browser
    When Open Debrif Dev
    Then login with user credential "<email>" "<pwd>"
    Then Select the "<station>"
    Then Veloz without an app "<email_user>" "<type_Of_User>"


    Examples:
      | email            |pwd          | station |email_user|type_Of_User|
      | qa@99minutos.com |Logistics.99m| MX1     |lendaly   |99 Minutos  |