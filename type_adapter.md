### Type Adapter

You can use custom type of JavaBean when deserializing from JSON string. For example:

```
{
    "id": 123,
    "name": "Michael",
    "registered": "2015-01-05"
}
```

JSON string can be converted to custom type, e.g., `java.time.LocalDate`:

```
class User {
    int id;
    String name;
    LocalDate registered;
}
```

When JsonReader tries to convert a JSON string to a Java type, it tries to find a 
proper `TypeAdapter` to convert value. You must register all `TypeAdapter`s you used 
when construct a `JsonBuilder`. There are several built-in `TypeAdapter`s you can use:

```
JsonBuilder builder = new JsonBuilder()
    .registerTypeAdapter(LocalDate.class, new DateTypeAdapter())
    .registerTypeAdapter(LocalTime.class, new TimeTypeAdapter());
JsonReader reader = builder.createJsonReader(json_str);
User user = reader.parse(User.class);
System.out.println(user.registered); // LocalDate value
```

See [API Docs](apidocs/index.html) for built-in `TypeAdapter`s.

### Write a TypeAdapter

A custom `TypeAdapter` is a class that implements `TypeAdapter<T>`. See `DateTypeAdapter` 
as example:

[DateTypeAdapter](https://github.com/michaelliao/jsonstream/blob/master/src/main/java/com/itranswarp/jsonstream/adapter/DateTypeAdapter.java)
