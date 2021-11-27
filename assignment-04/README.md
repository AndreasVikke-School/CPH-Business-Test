# Assignment 4

## 1. Mockito powerups

Answer the following questions about Mockito. Use code examples in your explanations.

* **How do you verify that a mock was called?**

Mockito has a verify function that you can call on a mock. You can also through this method verify method calls through that mock. Full code example listed below. 

``
Mockito.verify(someMock).someMethod();
`` 

* **How do you verify that a mock was NOT called?**

Also through the verify method, you can pass an additional parameter, detailing how many times a mock should be called. You can do this two ways, either using times(0) or never().

`` 
Mockito.verify(someMock, Mockito.times(0)).someMethod();
``

``
Mockito.verify(someMock, Mockito.never()).someMethod();
`` 

* **How do you specify how many times a mock should have been called?**

With the first function mentioned In the question above, we use the times method, when using times(0) we say it should never be called, if we change that number to 5, we verify that the method is called 5 times. 

* **How do you verify that a mock was called with specific arguments?**

This is also done with the verify method, simply by adding the parameters in the parenthesis like so:

``
Mockito.verify(someMock).someMethod("param");
`` 

* **How do you use a predicate to verify the properties of the arguments given to a call to the mock?**

Predicate in general meaning is a statement about something that is either true or false. In programming, predicates represent single argument functions that return a boolean value. 

In Java, predicates are implemented with the predicate<T> interface. It contains a test(T t) method that evaluates the predicate on the given argument. You can also use lambda functions and pass through the predicate, removing the need for the test method. We’ll try and use the simplest explanation possible. 

An example for a predicate is shown below, where we have our overridden test method from the predicate interface, that takes an integer as argument, and returns true if the passed argument is larger than five. In the main method we can then pass a list of integers through the predicate and print the results out.
```
class BiggerThanFive<E> implements Predicate<Integer> {

    @Override
    public boolean test(Integer v) {

        Integer five = 5;

        return v > five;
    }
}
```

```
public class JavaPredicateExample {

    public static void main(String[] args) {

        List<Integer> nums = List.of(2, 3, 1, 5, 6, 7, 8, 9, 12);

        BiggerThanFive<Integer> btf = new BiggerThanFive<>();
        nums.stream().filter(btf).forEach(System.out::println);
    }
}
```

With this example, where this can easily be converted to a lambda function, it is cleaner to just create the predicate inline as so:
````
public class JavaPredicateExample2 {

    public static void main(String[] args) {

        List<Integer> nums = List.of(2, 3, 1, 5, 6, 7, 8, 9, 12);

        Predicate<Integer> btf = n -> n > 5;

        nums.stream().filter(btf).forEach(System.out::println);
    }
}
````
Gives the same result, just cleaner. 

## 2. At least one

We decided to use option A: snake game. The assignment description is as follows: 

Using TDD, make at least one of the following three tasks, A, B or C. Whatever you choose, include coverage report (e.g. Jacoco) and mutation testing (e.g. PITest), and static analysis (e.g. Findbugs, PMD, CheckStyle).

A: Snake game: Make a classic snake game using TDD. To remind you the (minimum) rules of snake (you can make more features if you like):

* You control a the direction of a continuously moving snake, going up, down, left or right – the snake cannot stop moving.
* At any point in time, there is an apple somewhere on the playing field.
* When the snake’s head runs into the apple, the snake’s body gets longer.
* The snake dies if it runs into its own body, or a wall (if your game has walls). If the game doesn’t have walls, the snake should wrap around (like in Pacman).
* The winning state is to run out of space.
* Choose a point system of your liking. Inspiration:
  * Point(s) added for each apple eaten
  * Point(s) subtracted when starving (e.g. no apple eaten for an amount of time)

**TODO: Add pictures of code coverage and assignment work** 