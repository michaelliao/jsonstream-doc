### Overview

jsonstream is a Java library that can be used to convert between Java objects and JSON string.

### Goals for jsonstream

* Provide an easy way to convert JSON string to Java object;
* Fully customizable when converting to JavaBean;
* Built-in validation when convert JSON string to JavaBean;
* Fully customizable when serializing Java object to JSON string;
* Simple API and no dependency except commons-logging.

### Using jsonstream

You can write one line of code to parse a JSON string to Java object:

```
Object parsed = new JsonBuilder().createReader("[true, 123]").parse();
```

Check [User Guide](user_guide.html) to see more examples.

### Requirement

jsonstream requires JDK 1.8 or higher. Both source code and generated classes are set to `1.8`.
