# Created by aaronbrn at 15/06/23
Feature: Login
  # Enter feature description here

  Scenario Outline: Login Selfservices
    Given Launch in Browser
    When Open Selfservices Sandbox
    Then login with credential "<email>" "<pwd>"
    And Close Selfservices

    Examples:
      | email                  |pwd          |
      | mmhpruebas40@gmail.com |99Minutos.com|