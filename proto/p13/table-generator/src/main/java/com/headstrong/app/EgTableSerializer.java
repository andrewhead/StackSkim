package com.headstrong.app;

import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonObject;

import java.lang.reflect.Type;


public class EgTableSerializer implements JsonSerializer<EgTable> {

    @Override
    public JsonElement serialize(EgTable table, Type typeOfSrc, 
        JsonSerializationContext context) {
        JsonObject object = new JsonObject();
        object.add("columnNames", context.serialize(table.getColumnNames()));
        object.add("columnTypes", context.serialize(table.getColumnTypes()));
        object.add("rows", context.serialize(table.getRows()));
        return object; 
    }

}
