### Load JSON

You can call `JsonReader.parse()` to parse a JSON string to Java object, and 
the following rules are applied:

* JSON value `true` or `false` is parsed as Java Boolean object with `true` or `false`.

* JSON value `"string"` is parsed as Java String.

* JSON value `null` is parsed as Java `null`.

* JSON value `12345` is parsed as Java Long with a long value.

* JSON value `123.45` or `1.2e3.4` is parsed as Java Double with a double value.

* JSON object `{"key": "value"}` is parsed as Java Map with generic type `Map<String, Object>`.

* JSON array `[1, 2, 3]` is parsed as Java List with generic type `List<Object>`.

You can cast the returned object if you know the extract type of JSON string:

```
Boolean b = (Boolean) reader.parse();
```

If you do not want to use the type-cast operation, you can use the generic method:

```
Boolean b = reader.parse(Boolean.class);
```

It is very useful to get an integer because jsonstream parses JSON number as Long or Double:

```
// wanted an integer number:
Long n = reader1.parse(Long.class);

// wanted a float number:
Double d = reader2.parse(Double.class);

// don't care the type of number:
Number x = reader3.parse(Number.class);
// got a Long or Double type, both are safe to convert to Number object.
```

### Using JsonObjectFactory and JsonArrayFactory

JsonReader creates `HashMap<String, Object>` and `ArrayList<Object>` when parse JSON object and JSON array. 
But you can specify your own `JsonObjectFactory` and `JsonArrayFactory` to return different underlying data type:

```
JsonBuilder jb = new JsonBuilder().useJsonObjectFactory(
        () -> {
            return new TreeMap<String, Object>();
        }
).useJsonArrayFactory(
        () -> {
            return new LinkedList<Object>();
        }
);
```
