### Concepts

jsonstream can parse JSON string to coresponding Java object, and serialize Java object to JSON string.

josnstream contains 3 object to make API simple:

* JsonReader: Object to parse JSON string to Java object.
* JsonWriter: Object to serialize Java object to JSON string.
* JsonBuilder: A factory to create JsonReader or JsonWriter much easier.

Note that JsonReader and JsonWriter are not thread-safe. You MUST create new instance every time when 
parsing JSON string or serializing from Java object. But JsonBuilder just store some configurations, 
so it is should be shared as global object once it was created.

### Parsing Example

To parse a JSON string as a simple value:

```
// global builder:
JsonBuilder builder = new JsonBuilder();
// get a stream from somewhere:
Reader stream = new StringReader("true");
JsonReader reader = builder.createReader(stream);
System.out.println(reader.parse());
// print Boolean object: true
```

### Serializing Example

To serialize a Java object to a JSON string:

```
// global builder:
JsonBuilder builder = new JsonBuilder();
// write to a stream:
Writer stream = new StringWriter();
JsonWriter writer = builder.createWriter(stream);
writer.write(true);
// NOTE the provided 'stream' does not closed by JsonWriter,
// you have to close it manually:
stream.close();
System.out.println(stream.toString());
// print JSON string: "true"
```
