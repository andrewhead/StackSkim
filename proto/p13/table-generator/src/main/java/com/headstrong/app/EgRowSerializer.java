package com.headstrong.app;

import com.google.gson.JsonArray;
import com.google.gson.JsonSerializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonSerializationContext;

import java.lang.reflect.Type;


public class EgRowSerializer implements JsonSerializer<EgRow> {

    @Override
    public JsonElement serialize(EgRow row, Type typeOfSrc, 
        JsonSerializationContext context) {
        JsonArray array = new JsonArray();
        for (Object cell:row.getCells()) {
            array.add(context.serialize(cell));
        }
        return array;
    }

}
