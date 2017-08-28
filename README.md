# Item Catalog Project
Udacity Full Stack Nanodegree

## Description
This application provides a list of computer parts within a variety of part categories as well as a user registration and authentication system. Registered users have the ability to post, edit and delete their own items but NOT the items of other users.


## Set Up
1. Clone the [Full Stack repository] containing the vagrant VM from (https://github.com/udacity/fullstack-nanodegree-vm).
2. Copy the contents of this repository into the `fullstack-nanodegree-vm/vagrant/catalog/` directory of the Full Stack repository.

## Running
1. From a terminal window `cd` into the `fullstack-nanodegree-vm/vagrant/catalog/` directory and type `vagrant up` to start the Vagrant virtual machine.

2. Type `vagrant ssh` to connect to the Vagrant virtual machine.

3. `cd` to `/vagrant/catalog` and type `python lotsofparts.py` to populate the database with example data

4. Type `python application.py` to start running the application.

5. Open your browser and go to (http://localhost:8000/) to access the application.

## JSON endpoints
`/catalog/<category_id>/json`
This endpoint generates a list of parts for a category ID

`/catalog/<category_id>/<part_id>/json`
This endpoint generates JSON data for a specific category and part ID.
