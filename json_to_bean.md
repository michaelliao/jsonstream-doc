### JSON to Bean

It is make sense that you want to get a JavaBean object from a JSON string if the JSON string is representing 
like JavaBean definition:

```
public class User {
    int id;
    String name;

    String email;

    String getEmail() { return this.email; }
    void setEmail(String email) { this.email = email; }
}
```

You can get `User` object directly from `JsonReader.parse()` method:

```
jsonStr = "{ \"id\": 10001, \"name\": \"Michael\", \"email\": \"test@example.com\" }";
JsonReader jsonReader = jsonBuilder.createReader(jsonStr);
User user = jsonReader.parse(User.class);
// user.id ==> 10001
// user.name ==> "Michael"
// user.getEmail() ==> "test@example.com"
```

jsonstream requires a public Java class with default constructor. Both fields and getter/setter methods 
are recognized as JavaBean properties. Getters and setters have a higher priority than fields. All the 
fields and getters/setters do not need to be public, but MUST NOT be static.

Nested JavaBeans are processed correctly, and JSON array can be set to `List` or Java array as a property 
of JavaBean. For example, a JSON string:

```
{
    "id": 123,
    "name": "Michael",
    "tags": ["Music", "Football", "Running"],
    "address": {
        "street": "No.1 Road",
        "zipcode": "12345"
    }
}
}
```

Can be parsed as JavaBean:

```
public class Address {
    String street;
    String zipcode;
}

public class User {
    int id;
    String name;
    String[] tags; // <-- ["Music", "Football", "Running"]
    Address address; // <-- { "street": "No.1 Road", "zipcode": "12345" }
}
```

By a single line of code:

```
User user = jsonReader.parse(User.class);
```
