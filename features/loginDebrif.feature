# Created by aaronbrn at 19/06/23
Feature: Login Debrif
  # Enter feature description here

  Scenario Outline: Login Debrif
    Given Launch Browser
    When Open Debrif Dev
    Then login with user credential "<email>" "<pwd>"

    Examples:
      | email            |pwd          |
      | qa@99minutos.com |Logistics.99m|