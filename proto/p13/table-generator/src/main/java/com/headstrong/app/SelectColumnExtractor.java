package com.headstrong.app;

import java.util.ArrayList;
import net.sf.jsqlparser.JSQLParserException;
import net.sf.jsqlparser.parser.CCJSqlParserUtil;
import net.sf.jsqlparser.statement.select.Select;
import net.sf.jsqlparser.statement.select.SelectVisitor;
import net.sf.jsqlparser.statement.select.PlainSelect;
import net.sf.jsqlparser.statement.select.WithItem;
import net.sf.jsqlparser.statement.select.SetOperationList;
import net.sf.jsqlparser.statement.select.SelectItem;
import net.sf.jsqlparser.statement.Statement;
import net.sf.jsqlparser.statement.StatementVisitorAdapter;


public class SelectColumnExtractor extends StatementVisitorAdapter implements SelectVisitor {

    private ArrayList<String> mColumnNames;

    public ArrayList<String> getColumnNames(Statement statement) {
        mColumnNames = new ArrayList<String>();
        statement.accept(this);
        return mColumnNames;
    }

    @Override
    public void visit(PlainSelect plainSelect) {
        for (SelectItem selItem: plainSelect.getSelectItems()) {
            mColumnNames.add(selItem.toString());
        }
    }

    @Override
    public void visit(Select select) {
        select.getSelectBody().accept(this);
    }

    @Override
    public void visit(SetOperationList setOpList) {}

    @Override
    public void visit(WithItem withItem) {}

}
