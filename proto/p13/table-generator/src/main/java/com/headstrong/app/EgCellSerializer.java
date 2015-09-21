package com.headstrong.app;

import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonObject;

import java.lang.reflect.Type;


public class EgCellSerializer implements JsonSerializer<EgCell> {

    @Override
    public JsonElement serialize(EgCell cell, Type typeOfSrc, 
        JsonSerializationContext context) {
        JsonObject object = new JsonObject();
        object.add("data", context.serialize(cell.getData()));
        object.add("satisfies", context.serialize(cell.getSatisfiesExpressions()));
        return object; 
    }

}
