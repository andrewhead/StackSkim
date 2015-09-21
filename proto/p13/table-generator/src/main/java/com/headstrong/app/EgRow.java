package com.headstrong.app;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;


public class EgRow {

    List<String> mColumnNames;
    List<Object> mCells;
    HashMap<String, Object> mMap = new HashMap<String, Object>();

    public EgRow(List<String> columnNames, Object... cells) {
        mColumnNames = columnNames;
        mCells = Arrays.asList(cells);
        for (int i = 0; i < mColumnNames.size(); i++) {
            mMap.put(mColumnNames.get(i), mCells.get(i));
        }
    }

    public List<Object> getCells() {
        return mCells;
    }

    public long getLong(int cellIndex) {
        return (Long) mCells.get(cellIndex);
    }

    public String getString(int cellIndex) {
        return (String) mCells.get(cellIndex);
    }

    public long getLong(String columnName) {
        return (Long) mMap.get(columnName);
    }

    public String getString(String columnName) {
        return (String) mMap.get(columnName);
    }

}
