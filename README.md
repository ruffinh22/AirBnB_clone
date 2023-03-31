# AirBnB clone - The console

![AirBnB clone](hbnb.png)

![Structure](structure.png)
"Back-End Structure"

## Requirements

python3(version 3.85)
## Description of the Project

This is the first step towards building a full web application: the AirBnB clone.

It consists of a command interpreter to manipulate data without a visual interface, like in a Shell which is perfect for development and debugging

The tasks are linked and would help to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage
* create all unittests to validate all our classes and storage engine

## Testing

Use this command to test all models and files:

```
python3 -m unittest discover tests
```

## Description of the Command Interpreter

The command interpreter is similar to the Shell. It’s exactly the same but limited to a specific use-case. 

In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (show, all, etc…)
* Update attributes of an object
* Destroy an object

## How to start the console

```
git clone https://github.com/ruffinh22/AirBnB_clone.git
```
```
cd AirBnB_clone
```
```
python3 console.py
```
OR
```
./console.py
```

## How to use the console

### Commands

Command | What it does | Usage
--- | --- | ---
**create** | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id | create \<class name\>
**show** | Prints the string representation of an instance based on the class name and id | show \<class name\> \<id\>
**destroy** | Deletes an instance based on the class name and id (save the change into the JSON file) | destroy \<class name\> \<id\>
**all** | Prints all string representation of all instances based or not on the class name | all \<class name\> or all
**update** | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) | update \<class name\> \<id\> \<attribute name\> "\<attribute value\>"

### Examples

Command | Usage Example
--- | ---
**create** | create BaseModel
**show** | show BaseModel 1234-1234-1234
**destroy** | destroy BaseModel 1234-1234-1234
**all** | all BaseModel
**update** | update BaseModel 1234-1234-1234 email "aibnb@mail.com"

### Classes

Classes | Attributes
--- | ---
**BaseModel** | `id`, `created_at`, `updated_at`
**User** | `email`, `password`, `first_name`, `last_name`
**State** | `name`
**City** | `state_id`, `name`
**Amenity** | `name`
**Place** | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids`
**Review** | `place_id`, `user_id`, `text`

## Contributors

[ruffin hounsounnon](https://github.com/ruffinh22)
