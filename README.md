# EG3301R Pre-Crawler Device for Infants, Team EIM-306, National University of Singapore


# Year 2 Academic Year 2021-2022, Semester 2 to Year 3 Academic Year 2022-2023, Semester 1 

This is our team project for the module CS2113T Software Engineering & Object-Oriented Programming in which we designed and developed a Pre-Crawler Device for Infants. It is an assistive rehabilitation system designed to support infants with Cerebral Palsy and other neuromotor disorders during early-stage motor development. The goal of the project was to create a safe, automated device that guides infants through repeated crawling motions, helping to stimulate neuroplasticity and promote foundational motor skills during a critical developmental period.

## Master Control (send.py ; app.py)

The send.py script utilises the socket API which can be used to send messages across a network and provides a form of inter-process communication. This script acts as a socket server, awaiting connection to a client, which is the second script, app.py, via a port with a configurable number.

When the two scripts are running simultaneously, send.py continuously sends a message “0” to the
app.py. If either the emergency button or the reset button are pressed, this script changes the content of the
original message depending on which button was pressed first, and sends the updated message, “1”, to
app.py, prompting app.py to perform the relevant action.

## Build automation using Gradle

* This project uses Gradle for build automation and dependency management. It includes a basic build script as well (i.e. the `build.gradle` file).
* If you are new to Gradle, refer to the [Gradle Tutorial at se-education.org/guides](https://se-education.org/guides/tutorials/gradle.html).

## Testing

### I/O redirection tests

* To run _I/O redirection_ tests (aka _Text UI tests_), navigate to the `text-ui-test` and run the `runtest(.bat/.sh)` script.

### JUnit tests

* A skeleton JUnit test (`src/test/java/seedu/duke/DukeTest.java`) is provided with this project template. 
* If you are new to JUnit, refer to the [JUnit Tutorial at se-education.org/guides](https://se-education.org/guides/tutorials/junit.html).

## Checkstyle

* A sample CheckStyle rule configuration is provided in this project.
* If you are new to Checkstyle, refer to the [Checkstyle Tutorial at se-education.org/guides](https://se-education.org/guides/tutorials/checkstyle.html).

## CI using GitHub Actions

The project uses [GitHub actions](https://github.com/features/actions) for CI. When you push a commit to this repo or PR against it, GitHub actions will run automatically to build and verify the code as updated by the commit/PR.

## Documentation

`/docs` folder contains a skeleton version of the project documentation.

Steps for publishing documentation to the public: 
1. If you are using this project template for an individual project, go your fork on GitHub.<br>
   If you are using this project template for a team project, go to the team fork on GitHub.