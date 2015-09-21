package com.headstrong.app;

import java.util.List;
import java.util.ArrayList;


public class EgTable {

    private List<String> mColumnNames;
    private List<ColumnType> mColumnTypes;
    private List<EgRow> mRows = new ArrayList<EgRow>();

    public EgTable(List<String> columnNames, List<ColumnType> columnTypes) {
        mColumnNames = columnNames;
        mColumnTypes = columnTypes;
    }

    public void addRow(EgRow row) {
        mRows.add(row);
    }

    public EgRow getRow(int i) {
        return mRows.get(i);
    }

    public List<String> getColumnNames() {
        return mColumnNames;
    }

    public List<ColumnType> getColumnTypes() {
        return mColumnTypes;
    }

    public List<EgRow> getRows() {
        return mRows;
    }

}
