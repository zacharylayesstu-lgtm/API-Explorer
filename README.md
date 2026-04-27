# Day 1: Introduction to APIs with Python

## Python API Explorer Project

Today we are starting a new project where we will learn how Python can get information from the internet using an **API**.

By the end of this project, you will build a program that can search for information online and display it in a clean way for the user.

For Day 1, our goal is to understand what an API is and how to make our first API request using Python.

---

## What is an API?

An **API** stands for **Application Programming Interface**.

That sounds complicated, but the idea is simple:

> An API lets one program ask another program for information.

For example:

- A weather app asks a weather API for the forecast.
- A sports app asks an API for scores.
- A game website might ask an API for player stats.
- A Python program can ask an API for Pokémon data.

In this project, we will use Python to ask an API for information and then display the results.

---

## What is JSON?

Most APIs send information back in a format called **JSON**.

JSON looks a lot like Python dictionaries and lists.

Example:

```json
{
  "name": "pikachu",
  "id": 25,
  "height": 4,
  "weight": 60
}