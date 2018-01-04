# C# CHEAT SHEET


## 1- Basic Concepts

* **int** - integer.
* **float** - floating point number.
* **double** - double-precision version of float.
* **char** - a single character.
* **bool** - Boolean that can have only one of two values: True or False.
* **string** - a sequence of characters.

Convert.To*type*         Convert es parte de System namespace
*type* is the .NET type Convert.ToDouble(var) Convert.ToString(var)
  
`Char --> Comillas simples 'c'`

`String--> Comillas dobles "cadena"`

### CONCATENATION

```csharp
string a = "34";
"Value: " + a;

// Las variablaes con tipo implicito se deben inicializar 
var b = 32;   b <-- int

var num;        <-- Error
num = 42;

// Constante
const double PI = 3.14; 

// Arithmetic Operator
int x = 10 / 4;  // -->  2    Si ambos operandos son enteros el resultado tb
10 % 3 = 1    // -->  Resto o modulo 

// Assignment             
x += 3     -*/%
```

**Increment**   (Also work with decrement x--)

|Prefix                    | Postfix             |
|--------------------------|---------------------|
|`int x = 3;`              | `int x = 3;`        |
|`int y = ++x;`            | `int y = x++;`      |
|`// x is 4, y is 4`       | `// x is 4, y is 3` |

The prefix example increments the value of x, and then assigns it to y.
The postfix example assigns the value of x to y, and then increments x.


## 02- Conditional and Loops

### Relational Operators

`>=       ==        !=`


### IF ELSE
```csharp
if (x > y) 
      x -= y;

if (x == 8) {
}
else if (x == 18) {
}
else {
}
```
----------------------------------------

### Switch
```csharp
switch (numero)
{
    case 0:
        Console.WriteLine("Cero");
        break;
    case 1:
        Console.WriteLine("Uno");
        break;
    default:
        Console.WriteLine("Otro");
        break;
}
```
-----------------------------------------
### While

```csharp
While
  int num = 0;
  while(++num < 6)                while(num++ < 6) 
  {
  //Ejecuta 5 veces                Ejecuta 6 veces
  }
```
-----------------------------------------

### do while

```csharp
int x = 42;
do {
  Console.WriteLine(x);
  x++;
} while(x < 10);
```
The do-while loop executes the statements at least once, and then tests the condition.
The while loop executes the statement only after testing condition.

----------------------------------------
### For
```csharp
int x = 10;
for ( ; x > 0 ; )           increment x-=20;
{
  Console.WriteLine(x);
  x -= 3;
}
```
------------------------------------------

### BREAK AND CONTINUE
```csharp
int num = 0;
while (num < 20)
{
   if (num == 5)
     break;                                    // Finaliza el bucle
   Console.WriteLine(num);
   num++;
} 
// 0 1 2 3 4 
```
-----
```csharp
for (int i = 0; i < 10; i++) {
  if (i == 5)
    continue;                    // Finaliza la iteracion
  Console.WriteLine(i);
}
// 0 1 2 3 4 6 7 8 9
```
------------------------------------------------

### LOGICAL OPERATORS
| code | meaning | 
|------|---------|
| `&&` | and     |
|`||`  | or      |
| `!`  | not     |

------------------------------------------------

### CONDITIONAL OPERATOR 

`msg = (age >= 18) ? "Welcome" : "Sorry";`

------------------------------------------------


## 03-METHODS

```csharp
// return type name (paramethers)
int Sqr(int x)
{
  int result = x*x;
  return result;
}
```
void if method do not return
----------------------------------------------

### Parameters

Parameters behave within the method similarly to other local variables. They are created upon entering the method and are destroyed upon exiting the method.

```csharp
static void Func(int x)    --> x es parametro
{
  Console.WriteLine(x*2);
}

..main
Func(42)                        --> 42 es argumento 
```

### MULTIPLE PARAMETERS 

`static void Func(int a, int b, double c)   // Todos deben declarar tipo`

----------------------------------------------

### OPTIONAL PARAMETERS 

`static int Pow(int x, int p = 2 )     // siempre al final`

---------------------------------------------

### NAMED ARGS 

```csharp
static int Area(int h, int w)  // En la definicion (igual)

Area( w: 5, h: 8)      // Durante el llamado (dos puntos)  los Named pueden ir en cualquier orden
```
---------------------------------------------


### PASSING ARGUMENTS

#### *VALUE*

```csharp
static void Sqr(int x)
{
  x = x * x;
}
static void Main()
{
  int a = 3;
  Sqr(a);
  Console.WriteLine(a);              // Outputs 3, El metodo no modifica la variable, solo usa su valor
}
```

#### *REFERENCE*
Pass by reference copies an argument's memory address into the formal parameter. Inside the method, the address is used to access the actual argument used in the call. This means that changes made to the parameter affect the argument.

```csharp
static void Sqr(ref int x)      // The ref keyword is used both when defining the method and when calling it.
{
  x = x * x;
}
static void Main()
{
  int a = 3;
  Sqr(ref a);                        // The ref keyword is used both when defining the method and when calling it.
  Console.WriteLine(a); // Outputs 9
}
```

#### *OUTPUT*
```csharp
static void GetValues(out int x, out int y)
{
  x = 5;
  y = 42;
}
static void Main(string[] args)
{
  int a, b;
  GetValues(out a, out b);             // Transfer data out of the method
                                                    //Now a equals 5, b equals 42
}
```
----------------------------------------------------------------


### OVERLOADING (sobrecarga)

Method overloading is when multiple methods have the same name, but different parameters.
For example, you might have a Print method that outputs its parameter to the console window:

```csharp
static void Print(int a) {
  Console.WriteLine("Value: " + a);
}
static void Print(double a) {
  Console.WriteLine("Value: " + a);
}
static void Print(string label, double a) {
  Console.WriteLine(label + a);
}
static void Main(string[] args) {
  Print(11);                                      // Print funca con int y double y multiples parametros
  Print(4.13);
  Print("Average: ", 7.57);
}
```

When overloading methods, the definitions of the methods must differ from each other by the types and/or number of parameters.
When there are overloaded methods, the method called is based on the arguments. An integer argument will call the method implementation that accepts an integer parameter. A double argument will call the implementation that accepts a double parameter. Multiple arguments will call the implementation that accepts the same number of arguments.

-----------------------------------------------------------------

### RECURSION

```csharp
static int Fact(int num) {
  if (num == 1) {                  // The exit condition
    return 1;
  }
  return num * Fact(num - 1);
}
```


## 04- Classes and Objects

### VALUE AND REFERENCE TYPES

Value types     int x = 10;         on stack the value as it
Reference types (objects)   the data is stored in the heap because
it might need additional memory at runtime, while is memory 
address is stored in stack


|   Stack           |    Heap             |
|------------------:|:-------------------:|
|   `x->      10`     |                     |           
| `p1->  0x042b8`     |   -> Person object  |
      

-----------------------------------------------

### INSTATIATING
```csharp
class Person {
  int age;
  string name;
  public void SayHi() {
    Console.WriteLine("Hi");
  }
}
static void Main(string[] args)
{
  Person p1 = new Person();
  p1.age = 32;
  p1.SayHi();
}
```
-----------------------------------------------

### ENCAPSULATION

#### access modifiers: 
* **public**      makes the member accessible from the outside of                 
                the class. 
* **private**     makes members accessible only from within the          
                class and hides them from the outside.
* **protected**
* **internal**
* **protected internal**.

```csharp
class BankAccount
{
  private double balance=0;
  public void Deposit(double n)
  {
    balance += n;
  }
  public void Withdraw(double n)
  {
    balance -= n;
  }
  public double GetBalance()
  {
    return balance;
  }
}
```

This way member balance keeps private and it is not posible to 
modify it from outside the class

In summary, the benefits of encapsulation are:
- Control the way data is accessed or modified.
- Code is more flexible and easy to change with new requirements.
- Change one part of code without affecting other parts of code.

-------------------------------------------------------------

### CONSTRUCTORS

```csharp
class Person         
{
  private int age;
  private string name;
  public Person(string nm)    // Es un metodo con el mismo nombre que la clase
  {
    name = nm;
  }
  public string getName()
  {
    return name;
  }
}
static void Main(string[] args)
 {
  Person p = new Person("David");
  Console.WriteLine(p.getName());
}
//Outputs "David"
```

Constructors can be overloaded like any method by using different numbers of parameters.

--------------------------------------------------

### PROPERTIES

it is a good practice to encapsulate members of a class and provide access to them only through public methods.

A property is a member that provides a flexible mechanism to read, write, or compute the value of a private field. Properties can be used as if they are public data members, but they actually include special methods called accessors.
The accessor of a property contains the executable statements that help in getting (reading or computing) or setting (writing) a corresponding field. Accessor declarations can include a get accessor, a set accessor, or both. 
For example:

```csharp
class Person
{
  private int age; //field

  public int Name //property
  {
    // Accessors 
    get { return age; }      // Any of them could be omitted
    set {
      if (value > 0)       // This assumess custom logic
        age = value;
    }
  }
}
```

The Person class has a Name property that has both the set and the get accessors.
The set accessor is used to assign a value to the name variable; get is used to return its value. 
value is a special keyword, which represents the value we assign to a property using the set accessor. 
The name of the property can be anything you want, but coding conventions dictate properties have the same name as the private field with a capital letter.


### Auto-Implemented Properties

When you do not need any custom logic, C# provides a fast and effective mechanism for declaring private members through their properties.
For example, to create a private member that can only be accessed through the Name property's get and set accessors, use the following syntax:
`public string Name { get; set; }`

As you can see, you do not need to declare the private field name separately - it is created by the property automatically. Name is called an auto-implemented property. Also called auto-properties, they allow for easy and short declaration of private members.
We can rewrite the code from our previous example using an auto-property:

```csharp
class Person
{
  public string Name { get; set; }
}
static void Main(string[] args)
{
  Person p = new Person();
  p.Name = "Bob";
  Console.WriteLine(p.Name);
}
// Outputs "Bob"
```

## 05-Arrays

```csharp
int[ ] myArray = new int[5];  // Number of elements the array should hold

myArray[0] = 23;
```
------

### Initial values 

```csharp
string[ ] names = new string[3] {"John", "Mary", "Jessica"};
double[ ] prices = new double[ ] {3.6, 9.8, 6.4, 5.9};              // Can omit the number
//if its explicit on inital values
string[ ] names = {"John", "Mary", "Jessica"}; // Can even omit the new operator
```
-----------------------------

```csharp
int[] a = new int[5];

for (int k = 0; k < 5; k++) {
    a[k] = k * 3;
}

foreach (int k in a) {             // Often use (var k in a)
     console.WriteLine(k);
}
```
-----------------------------------------------------------------

### MULTIDIMENSIONAL ARRAYS 

```csharp
int[ , ] matriz = new int[10, 5];
matriz[3, 4] = 54;

int[ , ] matorx = { { 3, 4 }, { 5, 6 }, { 4, 8 } };
Console.WriteLine(matorx[2, 1]);               // 8
```
-----------------------------------------------------------------

### JAGGED ARRAYS

A jagged array is an array whose elements are arrays. So it is basically an array of arrays.
The following is a declaration of a single-dimensional array that has three elements, each of which is a single-dimensional array of integers:

`int[ ][ ] jaggedArr = new int[3][ ];`

Each dimension is an array, so you can also initialize the array upon declaration like this:

```csharp
int[ ][ ] jaggedArr = new int[ ][ ] 
{
  new int[ ] {1,8,2,7,9},
  new int[ ] {2,4,6},
  new int[ ] {33,42}
};

// You can access individual array elements as shown in the example below:
int x = jaggedArr[2][1]; //42
``` 

This accesses the second element of the third array.
A jagged array is an array-of-arrays, so an int[ ][ ] is an array of int[ ], each of which can be of different lengths and occupy their own block in memory. 
A multidimensional array (int[,]) is a single block of memory (essentially a matrix). It always has the same amount of columns for every row.

--------------------------------------------------------------

### ARRAY PROPERTIES AND METHODS

* arr.Length --> longitud
* arr.Rank --> dimension

Estos necesitan System.Linq
* arr.Reverse()
* arr.Max( )
* arr.Min( )
* arr.Sum( )

----------------------------------------------------------------

### WORKING WITH STRINGS

Strings

It’s common to think of strings as arrays of characters. In reality, strings in C# are objects.
When you declare a string variable, you basically instantiate an object of type String.
String objects support a number of useful properties and methods:
Length returns the length of the string.
IndexOf(value) returns the index of the first occurrence of the value within the string.
Insert(index, value) inserts the value into the string starting from the specified index.
Remove(index) removes all characters in the string after the specified index.
Replace(oldValue, newValue) replaces the specified value in the string.
Substring(index, length) returns a substring of the specified length, starting from the specified index. If length is not specified, the operation continues to the end of the string.
Contains(value) returns true if the string contains the specified value.

The examples below demonstrate each of the String members:

```csharp
string a = "some text";
Console.WriteLine(a.Length);
//Outputs 9

Console.WriteLine(a.IndexOf('t'));
//Outputs 5

 a = a.Insert(0, "This is ");
Console.WriteLine(a);
//Outputs "This is some text"

a = a.Replace("This is", "I am");
Console.WriteLine(a);
//Outputs "I am some text"

if(a.Contains("some"))
  Console.WriteLine("found");
//Outputs "found"

a = a.Remove(4);
Console.WriteLine(a);
//Outputs "I am"

a = a.Substring(2);
Console.WriteLine(a);
//Outputs "am"
``` 

You can also access characters of a string by its index, just like accessing elements of an array:

```csharp
string a = "some text";
Console.WriteLine(a[2]);
//Outputs "m"
```


## 06-More on Classes

### DESTRUCTORS

As constructors are used when a class is instantiated, destructors are automatically invoked when an object is destroyed or deleted. 
Destructors have the following attributes:
- A class can only have one destructor.
- Destructors cannot be called. They are invoked automatically.
- A destructor does not take modifiers or have parameters. 
- The name of a destructor is exactly the same as the class prefixed with a tilde (~).

For Example:

```csharp
class Dog
{
  ~Dog() 
  {
    // code statements
  }
}
```

Destructors can be very useful for releasing resources before coming out of the program. This can include closing files, releasing memory, and so on.

This can be useful, for example, if your class is working with storage or files. The constructor would initialize and open the files. Then, when the program ends, the destructor would close the files.

------------------------------------------------------------

### STATIC MEMBERS
(Belong specifically to the class instead of instance)

```csharp
class Cat {
public const  int EYES = 2;   // By definition const members are                   
                                             // statics
public static int count=0;   // Only one proertie for all instances
  public Cat() {                       // and belong to the class
    count++;
  }
}

static void Main(string[] args)
{
  Cat c1 = new Cat();
  Cat c2 = new Cat();
  Console.WriteLine(Cat.count);  // Solo accesibles desde el                   
}                                                   //   nombre de clase
```

--------------

### Static Constructors
Constructors can be declared static to initialize static members of the class.
The static constructor is automatically called once when we access a static member of the class.
For example:

```csharp
class SomeClass {
  public static int X { get; set; }
  public static int Y { get; set; }
 
  static SomeClass() {
    X = 10;
    Y = 20;
  }
}
```

The constructor will get called once when we try to access SomeClass.X or SomeClass.Y.

------------

### Static methods

```csharp
class Dog
{
  public static void Bark() {
    Console.WriteLine("Woof");
  }
}
static void Main(string[] args)
{
  Dog.Bark();    //
}
```
Cualquier metodo llamado directamente desde un metodo statico (Como Main) tiene que ser estatico tambien.

--------------------------------------------------------

### The **this** Keyword

The this keyword is used inside the class and refers to the current instance of the class, meaning it refers to the current object.
One of the common uses of this is to distinguish class members from other data, such as local or formal parameters of a method, as shown in the following example:

```csharp
class Person {
  private string name;
  public Person(string name) {
    this.name = name;
  }
}
```

Here, this.name represents the member of the class, whereas name represents the parameter of the constructor.
Another common use of this is for passing the current instance to a method as parameter: `ShowPersonInfo(this);`

-------------

### The **readonly** Modifier

The readonly modifier prevents a member of a class from being modified after construction. It means that the field declared as readonly can be modified only when you declare it or from within a constructor.
For example:

```csharp
class Person {
  private readonly string name = "John"; 
  public Person(string name) {
    this.name = name; 
  }
}
```
If we try to modify the name field anywhere else, we will get an error.
There are three major differences between readonly and const fields. 
First, a constant field must be initialized when it is declared, whereas a readonly field can be declared without initialization, as in:
```csharp
readonly string name; // OK
const double PI; // Error
```
Second, a readonly field value can be changed in a constructor, but a constant value cannot.
Third, the readonly field can be assigned a value that is a result of a calculation, but constants cannot, as in:
```csharp
readonly double a = Math.Sin(60); // OK
const double b = Math.Sin(60); // Error! 
```
---------------------------------------------------

### INDEXERS

Indexers

Declaration of an indexer is to some extent similar to a property. The difference is that indexer accessors require an index. 
Like a property, you use get and set accessors for defining an indexer. However, where properties return or set a specific data member, indexers return or set a particular value from the object instance. 
Indexers are defined with the this keyword.
For example:

```csharp
class Clients {
  private string[] names = new string[10];

  public string this[int index] {
    get {
      return names[index];
    }
    set {
      names[index] = value;
    }
  }
}
```

As you can see, the indexer definition includes the this keyword and an index, which is used to get and set the appropriate value.
Now, when we declare an object of class Clients, we use an index to refer to specific objects like the elements of an array:

```csharp
Clients c = new Clients();
c[0] = "Dave";
c[1] = "Bob";

Console.WriteLine(c[1]);
//Outputs "Bob"  
 ```

You typically use an indexer if the class represents a list, collection, or array of objects.

--------------------------------------------

### OPERATOR OVERLOADING (Defining custom actions for operators)

Overloaded operators are methods with special names, where the keyword operator is followed by the symbol for the operator being defined. 
Similar to any other method, an overloaded operator has a return type and a parameter list.
For example, for our Box class, we overload the + operator:

The method above defines an overloaded operator + with two Box object parameters and returning a new Box object whose Height and Width properties equal the sum of its parameter's corresponding properties.
Additionally, the overloaded operator must be static.
Putting it all together:
```csharp
class Box {
  public int Height { get; set; }
  public int Width { get; set; }
  public Box(int h, int w) {
    Height = h;
    Width = w;
  }
  public static Box operator+(Box a, Box b) {
    int h = a.Height + b.Height;
    int w = a.Width + b.Width;
    Box res = new Box(h, w);
    return res;
  }
}
static void Main(string[] args) {
  Box b1 = new Box(14, 3);
  Box b2 = new Box(5, 7);
  Box b3 = b1 + b2;

  Console.WriteLine(b3.Height); //19
  Console.WriteLine(b3.Width); //10
}
```

All arithmetic and comparison operators can be overloaded. For instance, you could define greater than and less than operators for the boxes that would compare the Boxes and return a boolean result. Just keep in mind that when overloading the greater than operator, the less than operator should also be defined.


## 07- Inheritance and Polymorphism

### Inheritance

Let's define our base class Animal:
```csharp
class Animal {
  public int Legs {get; set;}
  public int Age {get; set;}
}

// Now we can derive class Dog from it:
class Dog : Animal {
  public Dog() {
    Legs = 4;
  }
  public void Bark() {
    Console.Write("Woof");
  }
}
```
Note the syntax for a derived class. A colon and the name of the base class follow the name of the derived class.
All public members of Animal become public members of Dog. That is why we can access the Legs member in the Dog constructor.
Now we can instantiate an object of type Dog and access the inherited members as well as call its own Bark method.
```csharp
static void Main(string[] args) {
  Dog d = new Dog();
  Console.WriteLine(d.Legs);
  // Outputs 4

  d.Bark();
  //Outputs "Woof"
}
```

A base class can have multiple derived classes. For example, a Cat class can inherit from Animal.
Inheritance allows the derived class to reuse the code in the base class without having to rewrite it. And the derived class can be customized by adding more members. In this manner, the derived class extends the functionality of the base class.

C# no soporta herencia multiple, pero se puede lograr con interfaces

-----------------------------------------------------------------------

### PROTECTED MEMBERS

protected

Up to this point, we have worked exclusively with public and private access modifiers.
Public members may be accessed from anywhere outside of the class, while access to private members is limited to their class. 
The protected access modifier is very similar to private with one difference; it can be accessed in the derived classes. So, a protected member is accessible only from derived classes.
For example:

```csharp
class Person {
  protected int Age {get; set;}
  protected string Name {get; set;}
}
class Student : Person {
  public Student(string nm) {
    Name = nm;
  }
  public void Speak() {
    Console.Write("Name: "+Name);
  }
}
static void Main(string[] args) {
  Student s = new Student("David");
  s.Speak();
  //Outputs "Name: David"
}
```

As you can see, we can access and modify the Name property of the base class from the derived class.
But, if we try to access it from outside code, we will get an error:
```csharp
static void Main(string[] args) {
    Student s = new Student("David");
  s.Name = "Bob"; //Error
}
```

--------------

### Sealed    (Sellado)

A class can prevent other classes from inheriting it, or any of its members, by using the sealed modifier.
For example:
```csharp
sealed class Animal {
  //some code
}
class Dog : Animal { } //Error
```

In this case, we cannot derive the Dog class from the Animal class because Animal is sealed.
The sealed keyword provides a level of protection to your class so that other classes cannot inherit from it.

---------------------------------------------------------------

Derived class constructor and destructor

Constructors are called when objects of a class are created. With inheritance, the base class constructor and destructor are not inherited, so you should define constructors for the derived classes.
However, the base class constructor and destructor are being invoked automatically when an object of the derived class is created or deleted. 
Consider the following example:

```csharp
class Animal {
  public Animal() {
    Console.WriteLine("Animal created");
  }
  ~Animal() {
    Console.WriteLine("Animal deleted");
  }
}
class Dog: Animal {
  public Dog() {
    Console.WriteLine("Dog created");
  }
  ~Dog() {
    Console.WriteLine("Dog deleted");
  }
}
```
We have defined the Animal class with a constructor and destructor and a derived Dog class with its own constructor and destructor.

Let's create a Dog object:
```csharp
static void Main(string[] args) {
  Dog d = new Dog();
}
/*Outputs
Animal created
Dog created
Dog deleted
Animal deleted
*/
```

Note that the base class constructor is called first and the derived class constructor is called next.
When the object is destroyed, the derived class destructor is invoked and then the base class destructor is invoked.
You can think of it as the following: The derived class needs its base class in order to work, which is why the base class constructor is called first.

---------------------------------------------------------

### POLYMORPHISM

Polymorphism

Consider having a program that allows users to draw different shapes. Each shape is drawn differently, and you do not know which shape the user will choose. 
Here, polymorphism can be leveraged to invoke the appropriate Draw method of any derived class by overriding the same method in the base class. Such methods must be declared using the virtual keyword in the base class.
For example:
```csharp
class Shape {
  public virtual void Draw() {
    Console.Write("Base Draw");
  }
}
```
The virtual keyword allows methods to be overridden in derived classes.
Virtual methods enable you to work with groups of related objects in a uniform way.

--------------------------------------------------------------

### ABSTRACT CLASSES

Abstract Classes

As described in the previous example, polymorphism is used when you have different derived classes with the same method, which has different implementations in each class. This behavior is achieved through virtual methods that are overridden in the derived classes.
In some situations there is no meaningful need for the virtual method to have a separate definition in the base class.
These methods are defined using the abstract keyword and specify that the derived classes must define that method on their own. 
You cannot create objects of a class containing an abstract method, which is why the class itself should be abstract.
We could use an abstract method in the Shape class:
```csharp
abstract class Shape {
   public abstract void Draw();
}
```

As you can see, the Draw method is abstract and thus has no body. You do not even need the curly brackets; just end the statement with a semicolon.
The Shape class itself must be declared abstract because it contains an abstract method. Abstract method declarations are only permitted in abstract classes.
Remember, abstract method declarations are only permitted in abstract classes. Members marked as abstract, or included in an abstract class, must be implemented by classes that derive from the abstract class. An abstract class can have multiple abstract members.

### Abstract Classes

An abstract class is intended to be a base class of other classes. It acts like a template for its derived classes.
Now, having the abstract class, we can derive the other classes and define their own Draw() methods:
```csharp
abstract class Shape {
  public abstract void Draw();
}
class Circle : Shape {
  public override void Draw() {
    Console.WriteLine("Circle Draw");
  }
}
class Rectangle : Shape {
  public override void Draw() {
    Console.WriteLine("Rect Draw");
  }
}
static void Main(string[] args) {
  Shape c = new Circle();
  c.Draw();
  //Outputs "Circle Draw"
}
```

Abstract classes have the following features:
- An abstract class cannot be instantiated.
- An abstract class may contain abstract methods and accessors.
- A non-abstract class derived from an abstract class must include actual implementations of all inherited abstract methods and accessors.

It is not possible to modify an abstract class with the sealed modifier because the two modifiers have opposite meanings. The sealed modifier prevents a class from being inherited and the abstract modifier requires a class to be inherited.

-----------------------------------------------------------

### INTERFACES

Interfaces

An interface is a completely abstract class, which contains only abstract members.
It is declared using the interface keyword:
```csharp
public interface IShape
{
  void Draw();
}
```
All members of the interface are by default abstract, so no need to use the abstract keyword. 
Also, all members of an interface are always public, and no access modifiers can be applied to them.
It is common to use the capital letter I as the starting letter for an interface name.
Interfaces can contain properties, methods, etc. but cannot contain fields (variables).

PUEDE tener metodos y propiedades (esas definidas con get y set) pero NO variables

-------

When a class implements an interface, it must also implement, or define, all of its methods.
The term implementing an interface is used (opposed to the term "inheriting from") to describe the process of creating a class based on an interface. The interface simply describes what a class should do. The class implementing the interface must define how to accomplish the behaviors.
The syntax to implement an interface is the same as that to derive a class:
```csharp
public interface IShape {
  void Draw();
}
class Circle : IShape {
  public void Draw() {
    Console.WriteLine("Circle Draw");
  }
}
static void Main(string[] args) {
  IShape c = new Circle();
  c.Draw();
  //Outputs "Circle Draw"
}
```

Note, that the override keyword is not needed when you implement an interface.
But why use interfaces rather than abstract classes? 
A class can inherit from just one base class, but it can implement multiple interfaces!
Therefore, by using interfaces you can include behavior from multiple sources in a class.
To implement multiple interfaces, use a comma separated list of interfaces when creating the `class: class A: IShape, IAnimal, etc`.

----------------------------------------------------

### NESTED CLASSES

Nested Classes

C# supports nested classes: a class that is a member of another class.
For example:

```csharp
class Car {
  string name;
  public Car(string nm) {
    name = nm;
    Motor m = new Motor();
  }
  public class Motor {
    // some code
  }
}
```
The Motor class is nested in the Car class and can be used similar to other members of the class.
A nested class acts as a member of the class, so it can have the same access modifiers as other members (public, private, protected).

-----------------------------------------------------

### NAMESPACES

When you create a blank project, it has the following structure:
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SoloLearn {
  class Program {
    static void Main(string[] args) {
    }
  }
}
```
Note, that our whole program is inside a namespace. So, what are namespaces?
Namespaces declare a scope that contains a set of related objects. You can use a namespace to organize code elements. You can define your own namespaces and use them in your program. 
The using keyword states that the program is using a given namespace. 
For example, we are using the System namespace in our programs, which is where the class Console is defined:
```csharp
using System;
...
Console.WriteLine("Hi");
```

Without the using statement, we would have to specify the namespace wherever it is used:
`System.Console.WriteLine("Hi");`
 

The .NET Framework uses namespaces to organize its many classes. System is one example of a .NET Framework namespace.
Declaring your own namespaces can help you group your class and method names in larger programming projects.
  

## 08-Structs, Enums, Exceptions and Files

### Structs

A struct type is a value type that is typically used to encapsulate small groups of related variables, such as the coordinates of a rectangle or the characteristics of an item in an inventory. The following example shows a simple struct declaration:
```csharp
struct Book {
  public string title;  
  public double price;
  public string author;
}
```
Structs share most of the same syntax as classes, but are more limited than classes.
Unlike classes, structs can be instantiated without using a new operator.
```csharp
static void Main(string[] args) {
  Book b;
  b.title = "Test";
  b.price = 5.99;
  b.author = "David";

  Console.WriteLine(b.title);
  //Outputs "Test"
}
``` 

Structs do not support inheritance and cannot contain virtual methods.


Structs can contain methods, properties, indexers, and so on. Structs cannot contain default constructors (a constructor without parameters), but they can have constructors that take parameters. In that case the new keyword is used to instantiate a struct object, similar to class objects.
For example:

```csharp
struct Point {
  public int x;
  public int y;
  public Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
static void Main(string[] args) {
  Point p = new Point(10, 15);
  Console.WriteLine(p.x);
  // Outputs 10
 }
```

### Structs vs Classes
In general, classes are used to model more complex behavior, or data, that is intended to be modified after a class object is created. Structs are best suited for small data structures that contain primarily data that is not intended to be modified after the struct is created. Consider defining a struct instead of a class if you are trying to represent a simple set of data. 
All standard C# types (int, double, bool, char, etc.) are actually structs.

--------------------------------------------------------------

### ENUMS

Enums

The enum keyword is used to declare an enumeration: a type that consists of a set of named constants called the enumerator list.
By default, the first enumerator has the value 0, and the value of each successive enumerator is increased by 1.
For example, in the following enumeration, Sun is 0, Mon is 1, Tue is 2, and so on:
`enum Days {Sun, Mon, Tue, Wed, Thu, Fri, Sat};` 

You can also assign your own enumerator values:
`enum Days {Sun, Mon, Tue=4, Wed, Thu, Fri, Sat};`

In the example above, the enumeration will start from 0, then Mon is 1, Tue is 4, Wed is 5, and so on. The value of the next item in an Enum is one increment of the previous value.
Note that the values are comma separated.
You can refer to the values in the Enum with the dot syntax.
In order to assign Enum values to int variables, you have to specify the type in parentheses:
```csharp
enum Days { Sun, Mon, Tue, Wed, Thu, Fri, Sat }; 

static void Main(string[] args) {
  int x = (int)Days.Tue;
  Console.WriteLine(x);
  //Outputs 2
}
```

Basically, Enums define variables that represent members of a fixed set.
Some sample Enum uses include month names, days of the week, cards in a deck, etc.


Enums are often used with switch statements.
For example:
```csharp
enum TrafficLights { Green, Red, Yellow };

static void Main(string[] args) {
  TrafficLights x = TrafficLights.Red;
  switch (x) {
    case TrafficLights.Green:
      Console.WriteLine("Go!");
      break;
    case TrafficLights.Red:
      Console.WriteLine("Stop!");
      break;
    case TrafficLights.Yellow:
      Console.WriteLine("Caution!");
      break;
  }
  //Outputs "Stop!"
}
```

-----------------------------------------------------

### EXCEPTION HANDLING
```csharp
int result=0;
int num1 = 8;
int num2 = 4;
try {
  result = num1 / num2;
}
catch (DivideByZeroException e) {
  Console.WriteLine("Error");
}

catch (Exception e) {
   Console.WriteLine("e.Message);
}
finally {
  Console.WriteLine(result);
}
```

The code that might generate an exception is placed in the try block. If an exception occurs, the catch blocks is executed without stopping the program.
The type of exception you want to catch appears in parentheses following the keyword catch. 
We use the general Exception type to handle all kinds of exceptions. We can also use the exception object e to access the exception details, such as the original error message (e.Message)

The finally block can be used, for example, when you work with files or other resources. These should be closed or released in the finally block, whether an exception is raised or not.

The following exception types are some of the most commonly used: `FileNotFoundException, FormatException, IndexOutOfRangeException, InvalidOperationException, OutOfMemoryException`.


---------------------------------------------------------

### WORKING WITH FILES

#### Writing to Files

The System.IO namespace has various classes that are used for performing numerous operations with files, such as creating and deleting files, reading from or writing to a file, closing a file, and more.
The File class is one of them. For example:
```csharp
string str = "Some text";
File.WriteAllText("test.txt", str);
```
`The WriteAllText()` method creates a file with the specified path and writes the content to it. If the file already exists, it is overwritten. 
The code above creates a file test.txt and writes the contents of the str string into it.
To use the File class you need to use the System.IO namespace: using System.IO;

#### Reading from Files

You can read the content of a file using the ReadAllText method of the File class:
```csharp
string txt = File.ReadAllText("test.txt");
Console.WriteLine(txt); 
```

This will output the content of the test.txt file.
The following methods are available in the File class:
* AppendAllText() - appends text to the end of the file.
* Create() - creates a file in the specified location.
* Delete() - deletes the specified file.
* Exists() - determines whether the specified file exists.
* Copy() - copies a file to a new location.
* Move() - moves a specified file to a new location.

All methods automatically close the file after performing the operation.
  
  
## 09- Generics


Generics allow the reuse of code across different types.
For example, let's declare a method that swaps the values of its two parameters:
```csharp
static void Swap(ref int a, ref int b) {
  int temp = a;
  a = b;
  b = temp;
}
```
Our Swap method will work only for integer parameters. If we want to use it for other types, for example, doubles or strings, we have to overload it for all the types we want to use it with. Besides a lot of code repetition, it becomes harder to manage the code because changes in one method mean changes to all of the overloaded methods.
Generics provide a flexible mechanism to define a generic type.
```csharp
static void Swap<T>(ref T a, ref T b) {
  T temp = a;
  a = b;
  b = temp;
}
```
In the code above, T is the name of our generic type. We can name it anything we want, but T is a commonly used name. Our Swap method now takes two parameters of type T. We also use the T type for our temp variable that is used to swap the values.
Note the brackets in the syntax <T>, which are used to define a generic type.


### Generic Methods

Now, we can use our Swap method with different types, as in:
```csharp
static void Swap<T>(ref T a, ref T b) {
  T temp = a;
  a = b;
  b = temp;
}
static void Main(string[] args) {
  int a = 4, b = 9;
  Swap<int>(ref a, ref b);
  //Now b is 4, a is 9

  string x = "Hello";
  string y = "World";
  Swap<string>(ref x, ref y);
  //Now x is "World", y is "Hello"
}
```

When calling a generic method, we need to specify the type it will work with by using brackets. So, when `Swap<int>` is called, the T type is replaced by int. For `Swap<string>`, T is replaced by string. 
If you omit specifying the type when calling a generic method, the compiler will use the type based on the arguments passed to the method.
Multiple generic parameters can be used with a single method. 
For example: `Func<T, U>` takes two different generic types.


---------------------------------------------------

### GENERIC CLASSES


Generic types can also be used with classes.
The most common use for generic classes is with collections of items, where operations such as adding and removing items from the collection are performed in basically the same way regardless of the type of data being stored. One type of collection is called a stack. Items are "pushed", or added to the collection, and "popped", or removed from the collection. A stack is sometimes called a Last In First Out (LIFO) data structure.
For example:
```csharp
class Stack<T> {
  int index=0;
  T[] innerArray = new T[100];
  public void Push(T item) {
    innerArray[index++] = item; 
  }
  public T Pop() {
    return innerArray[--index]; 
  }
  public T Get(int k) { return innerArray[k]; }
}
```

The generic class stores elements in an array. As you can see, the generic type T is used as the type of the array, the parameter type for the Push method, and the return type for the Pop and Get methods.
Now we can create objects of our generic class:
```csharp
Stack<int> intStack = new Stack<int>();
Stack<string> strStack = new Stack<string>();
Stack<Person> PersonStack = new Stack<Person>();
```
We can also use the generic class with custom types, such as the custom defined Person type.
In a generic class we do not need to define the generic type for its methods, because the generic type is already defined on the class level.

-----------------------------------------------------------------

### COLLECTIONS

The .NET Framework provides a number of generic collection classes, useful for storing and manipulating data.
These classes are contained in the System.Collections.Generic namespace.
List is one of the commonly used collection classes:

```csharp
List<string> colors = new List<string>();
colors.Add("Red");
colors.Add("Green");
colors.Add("Pink");
colors.Add("Blue");

foreach (var color in colors) {
  Console.WriteLine(color);
}
/*Outputs
Red
Green
Pink
Blue
*/
```

We defined a List that stores strings and iterated through it using a foreach loop. 
The List class contains a number of useful methods:
Add adds an element to the List.
Clear removes all elements from the List.
Contains determines whether the specified element is contained in the List.
Count returns the number of elements in the List.
Insert adds an element at the specified index.
Reverse reverses the order of the elements in the List.
So why use Lists instead of arrays?
Because, unlike arrays, the group of objects you work with in a collection can grow and shrink dynamically.

----------------------

### Collections

Commonly used generic collection types include:
* `Dictionary<TKey, TValue>` represents a collection of key/value pairs that are organized based on the key.
* `List<T>` represents a list of objects that can be accessed by index. Provides methods to search, sort, and modify lists.
* `Queue<T>` represents a first in, first out (FIFO) collection of objects.
* `Stack<T>` represents a last in, first out (LIFO) collection of objects.

Choose the type of collection class based on the data you need to store and the operations you need.
