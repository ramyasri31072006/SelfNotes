// In **Object-Oriented Programming (OOP)**, relationships describe how different classes/objects are connected to each other.

// ### Main types of relationships

// 1. **Association** – A general connection between two classes.
//    Example: `Teacher` teaches `Student`.

// 2. **Aggregation** – A **“has-a”** relationship where the contained object can exist independently.
//    Example: `Department` has `Teachers`. Even if the department is removed, teachers can still exist.

// 3. **Composition** – A stronger **“has-a”** relationship where the contained object depends on the parent.
//    Example: `House` has `Rooms`. If the house is destroyed, its rooms don't meaningfully exist separately.

// 4. **Inheritance** – An **“is-a”** relationship where one class inherits properties/behavior from another.
//    Example: `Dog` **is an** `Animal`.

// 5. **Dependency** – One class temporarily **uses** another class.
//    Example: A `Report` class uses a `Printer` to print a report.

// **Easy way to remember:**

// * Inheritance → **is-a**
// * Aggregation/Composition → **has-a**
// * Association → **knows/works-with**
// * Dependency → **uses**

/*Here is a quick guide to understanding the four types of relationships in Object-Oriented Design (Low-Level Design):

Association ("Uses-a" or "Has-a"):
A general relationship where one object uses or interacts with another.
Both objects have their own independent lifecycles.
Example: A Driver can drive a Car, but the driver can exist without the car, and the car can exist without the driver.

Composition ("Part-of" with strict lifecycle):
A strong "has-a" relationship where the child object cannot exist independently of the parent object. If the parent is destroyed, the child is also destroyed.
Example: A Car has an Engine. The Engine is created inside the Car and cannot exist without it (as seen in your code snippet).

Aggregation ("Part-of" with independent lifecycle):
A weaker "has-a" relationship where the child object can exist independently of the parent object.
Example: A Department has Professors. If the department is closed, the professors still exist.

Dependency ("Depends-on"):
A temporary relationship where one class uses another class, typically as a method parameter or local variable, but doesn't store it as a member field.
Example: A Car has a move(Fuel f) method. The car depends on Fuel to move, but doesn't own it.
Here is the corrected code demonstrating these relationships clearly based on your problem:*/

class Engine {
    // Engine cannot exist independently of a Car (Composition)
}

class Car {
    private Engine engine; // Composition: Car owns the Engine

    public Car() {
        this.engine = new Engine(); // Created inside Car
    }
}

class Driver {
    // Driver interacts with Car (Association)
    public void drive(Car car) { 
        System.out.println("Driving car");
    }
}

class Ride {
    private Driver driver;
    private Car car;

    public Ride(Driver driver, Car car) {
        this.driver = driver;
        this.car = car;
    }
}
// Dependency ("Uses-a"):
// Occurs when one class uses another temporarily (e.g., as a method parameter).
// In our code, Checkout takes PaymentMethod as a parameter in the process() method. It doesn't store it as an instance variable, so Checkout depends on PaymentMethod.

// Realization / Implementation ("Implements"):
// Occurs when a class implements an interface or a contract defined by another type.
// In our code, CardPayment implements the PaymentMethod interface using the implements keyword. Therefore, CardPayment has a Realization relationship with PaymentMethod.
// Based on this, the correct pair is Checkout-PaymentMethod -> Dependency, CardPayment -> Realization.

// Here is the corrected and clean code snippet for your reference:

interface PaymentMethod {
    void pay();
}

class CardPayment implements PaymentMethod { // Realization
    public void pay() {
        System.out.println("Paid using Card");
    }
}

class UPIPayment implements PaymentMethod { // Realization
    public void pay() {
        System.out.println("Paid using UPI");
    }
}

class Checkout {
    public void process(PaymentMethod method) { // Dependency
        method.pay();
    }
}

//------------------------------------------------------------------------------------------------------------------------------------------------
class Book {
    private String title;

    public Book(String title) {
        this.title = title;
    }
}

class Library {
    private List<Book> books; 

    public Library(List<Book> books) {
        this.books = books;
    }
}

class Member {
    public void borrow(Book book) { 
        System.out.println("Borrowed: " + book);
    }
}

// Library-Book (Aggregation): In the code, the Library class holds a reference to a List<Book>,
// but the Book objects are passed into the Library constructor from the outside. 
// This means Book instances can exist independently of the Library (if the library closes, the books aren't necessarily destroyed).
// This represents Aggregation (a "has-a" relationship with independent lifecycles).

// Member-Book (Association): In the Member class, the borrow(Book book) method takes a Book as a parameter.
// The Member is associated with the Book during the borrow action, meaning they interact with each other, but neither owns the other's lifecycle. 
// This represents Association.


//------------------------------------------------------------------------------------------------------------------------------------

// You are designing a media system:

// Playlist contains multiple Song objects
// Song can exist without a playlist
// A method temporarily plays a Song passed as parameter
// Question: Which option correctly represents the relationship types between Playlist–Song and Method–Song?

// Code Snippet

class Song {
    private String title;

    public Song(String title) {
        this.title = title;
    }
}

class Playlist {
    private List<Song> songs; 

    public Playlist(List<Song> songs) {
        this.songs = songs;
    }
}

class Player {
    public void play(Song song) { 
        System.out.println("Playing: " + song);
    }
}

// Correct Answer:

// Playlist-Song -> Aggregation, Method-Song -> Dependency  
// Explanation:
// Option B is correct, because Songs exist independently of Playlist, so it's Aggregation.  
// The method using Song as a parameter indicates temporary usage, which is Dependency.
