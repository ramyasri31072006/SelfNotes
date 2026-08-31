// You are designing a vehicle system:

// Vehicle is a base class
// Car and Bike extend it
// A method takes Vehicle and calls start()
// Each subclass provides its own implementation
// Question: Which option correctly represents the OOP concepts used in this design?

// Code Snippet
abstract class Vehicle { 
    abstract void start();
}

class Car extends Vehicle { 
    void start() {
        System.out.println("Car starts");
    }
}

class Bike extends Vehicle {
    void start() {
        System.out.println("Bike starts");
    }
}

class Service {
    public void run(Vehicle v) { 
        v.start();
    }
}

//ANS :Inheritance + Polymorphism + Abstraction  


// ----> can object will be created for abstract class?

// No, you cannot create an object (instantiate) directly from an abstract class in Java.

// An abstract class is meant to be a blueprint. It can have abstract methods (without a body) that must be implemented by its subclasses.
// Because these methods lack implementation, allowing an object of the abstract class to be created would lead to runtime errors when calling those methods.

// You can only create objects of its concrete subclasses (like Car or Bike), which provide the specific implementations.

// Here is how the corrected code looks with a Main class demonstrating object creation of the subclasses:

abstract class Vehicle { 
    abstract void start();
}

class Car extends Vehicle { 
    void start() {
        System.out.println("Car starts");
    }
}

class Bike extends Vehicle {
    void start() {
        System.out.println("Bike starts");
    }
}

class Service {
    public void run(Vehicle v) { 
        v.start();
    }
}

public class Main {
    public static void main(String[] args) {
        // Vehicle v = new Vehicle(); // Error: Cannot instantiate the type Vehicle
        
        Vehicle myCar = new Car(); // Valid: Polymorphism
        Vehicle myBike = new Bike(); // Valid: Polymorphism
        
        Service service = new Service();
        service.run(myCar);
        service.run(myBike);
    }
}


-----> is car can be created using vehicle type?

Yes, absolutely! You can create a Car object using the Vehicle reference type, like this:

Vehicle myCar = new Car();
This is a core feature of Polymorphism in Object-Oriented Programming. Because Car inherits from Vehicle, a Car is-a Vehicle.
This allows a parent class reference variable to point to a child class object.

When you call v.start() inside the Service class, Java uses dynamic method dispatch (runtime polymorphism) to execute the specific start() method 
belonging to the Car class rather than the abstract Vehicle class.

Here is the complete code demonstrating this:

abstract class Vehicle { 
    abstract void start();
}

class Car extends Vehicle { 
    void start() {
        System.out.println("Car starts");
    }
}

class Bike extends Vehicle {
    void start() {
        System.out.println("Bike starts");
    }
}

class Service {
    public void run(Vehicle v) { 
        v.start(); // Polymorphism in action
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle myCar = new Car(); // Car created using Vehicle reference type
        Service service = new Service();
        
        service.run(myCar); // Output: Car starts
    }
}


